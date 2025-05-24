# from langgraph.graph import StateGraph
# from typing import TypedDict
# from langgraph.graph import StateGraph, START, END
# import random
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

def setup_node(state: agenstate9) -> agenstate9:
    """ this is the setup node """
    return{
        "name": "hi there " + state['name'],
        "random_number": random.randint(state['lower_bound'], state['upper_bound'])
    }
def guess_node(state: agenstate9) -> agenstate9:
    """ this is the guess node, the graph will take hints like higher or lower to guess the number """
    guess_number=random.randint(state['lower_bound'], state['upper_bound'])
    return{
        "guess_number": guess_number,
        "attempts": state['attempts']+1,
        "guesses": state['guesses'] + [guess_number]
    }
def hint_node(state: agenstate9) -> agenstate9:
    """ this is the hint node, the graph will take hints like higher or lower to guess the number """
    if state['random_number'] > state['guess_number']:
        state["lower_bound"]=state['guess_number']
        return "higher"
    elif state['random_number'] < state['guess_number']:
        state["upper_bound"]=state['guess_number']
        return "lower"
    else:
        return "correct"
  
    