from langgraph.graph import StateGraph
from typing import TypedDict
from langgraph.graph import StateGraph, START, END
import random
# class agentstate8(TypedDict):
#     name: str
#     number: list[int]
#     counter: int

# def greeting_node(state: agentstate8) -> agentstate8:
#     """ this is the greeting node """
#     return{
#         "name": "hi there " + state["name"] ,
#         "counter": 0
#     }

# def random_node(state: agentstate8) -> agentstate8:
#     """ this generates a random number from 0-10"""
#     return{
#         "number": state["number"] + [random.randint(0,10)],
#         "counter": state["counter"] + 1
#     }
    
# def should_continue(state: agentstate8) -> agentstate8:
#     """ function to do what to do next"""
#     if state["counter"] < 5:
#         print("entering loop", state["counter"])
#         return "loop"
#     else:
#         print("exiting loop", state["counter"])
#         return "exit"


# graph8=StateGraph(agentstate8)
# graph8.add_node("greeting_node", greeting_node)
# graph8.add_node("random_node", random_node)
# graph8.add_conditional_edges(
#     "random_node",   #source node
#     should_continue, #ACTION NODE
#     {
#         "loop": "random_node",
#         "exit": END
#     }
# )
# graph8.add_edge("greeting_node", "random_node")
# graph8.set_entry_point("greeting_node")
# app=graph8.compile()  #compile the graph
# result=app.invoke({"name": "SHAYAN", "number": [], "counter": 0})
# print(result)


#excerise

 #we have to have the graph guess a number between 1-20 and the graph will take hints like higher or lower to guess the number


class agenstate9(TypedDict):
    name: str
    guesses: list[int]
    attempts: int
    lower_bound: int
    upper_bound: int
    random_number: int
    hint: str

def setup_node(state: agenstate9) -> agenstate9:
    return {
        "name": f"Welcome, to the game {state['name']}",
        "guesses": [],
        "attempts": 0,
        "lower_bound": 1,
        "upper_bound": 20,
        "random_number": random.randint(1, 20),
        "hint": "try again"
    }

def guess_node(state: agenstate9) -> agenstate9:
    """ this is the guess node, the graph will take hints like higher or lower to guess the number """
    possible_guesses=[i for i in range(state['lower_bound'], state['upper_bound']+1) if i not in state['guesses']]
    if possible_guesses:
        guess_number=random.choice(possible_guesses)
    else:
        guess_number=random.randint(state['lower_bound'], state['upper_bound'])
    print("the number guessed is now ", guess_number," we are on the attempt", state['attempts'], "in the range", state['lower_bound'], "to", state['upper_bound'])
    return{
        "attempts": state['attempts']+1,
        "guesses": state['guesses'] + [guess_number],
    }
def hint_node(state: agenstate9) -> agenstate9:
    """ this is the hint node, the graph will take hints like higher or lower to guess the number amd update the bounds """
    latest_guess=state['guesses'][-1]
    if latest_guess>state['random_number']:
        state["hint"]="the number you guesses is higher than the random number"
        state["upper_bound"]=min(state['upper_bound'], latest_guess-1)
        print(f"the hint is {state['hint']}")
    elif latest_guess<state['random_number']:
        state["hint"]="the number you guesses is lower than the random number"
        state["lower_bound"]=max(state['lower_bound'], latest_guess+1)
        print(f"the hint is {state['hint']}")
    else:
        print(f"the hint is {state['hint']}")   
    return state

def should_continue(state: agenstate9) -> agenstate9:
    """ this is the should continue node """
    latest_guess=state['guesses'][-1]
    if state['attempts']>7:
        print("the game is over you hav reacged tge max number of attepts")
        return "over"
    elif state['random_number']==latest_guess:
        print("congratulations you guessed the number"+str(state['random_number']))
        return "over"
    else:
        print(f"this is your {state['attempts']} attempt/7 attempts")
        return "continue"
            



graph = StateGraph(agenstate9)
graph.add_node("setup_node", setup_node)
graph.add_node("guess_node", guess_node)
graph.add_node("hint_node", hint_node)    

# Set up the flow
graph.add_edge("setup_node", "guess_node")
graph.add_edge("guess_node", "hint_node")
graph.add_conditional_edges(
    "hint_node",
    should_continue,
    {
        "continue": "guess_node",
        "over": END
    }
)
graph.set_entry_point("setup_node")
app=graph.compile()
app.invoke({"name": "Shayan", "guesses": [], "attempts":0, "lower_bound": 1, "upper_bound": 20})