# from langgraph.graph import StateGraph
# from typing import TypedDict
# from langgraph.graph import StateGraph, START, END



# class agentstate6(TypedDict):
#     operation: str
#     number1: int
#     number2: int
#     finalnumber: int

# def add_node(state: agentstate6) -> agentstate6:
#     """ this is the add node1 """
#     return{
#         "finalnumber": state["number1"] + state["number2"]
#     }

# def subtract_node(state: agentstate6) -> agentstate6:
#     """ this is the subtract node1 """
#     return{
#         "finalnumber": state["number1"] - state["number2"]
#     }

# def decide_next_node(state: agentstate6) -> agentstate6:
#     """ this is the decide next node """
#     if state["operation"] == "add":
#         return "add_operation"
#     elif state["operation"] == "subtract":
#         return "subtraction_operation"

# graph6=StateGraph(agentstate6)
# graph6.add_node("add_node", add_node)
# graph6.add_node("subtract_node", subtract_node)
# graph6.add_node("router", lambda state:state)
# graph6.add_edge(START, "router")
# graph6.add_conditional_edges(
#         "router",
#         decide_next_node,
#         {
#             "add_operation": "add_node",
#             "subtraction_operation": "subtract_node"
#         }
#     )

# graph6.add_edge("add_node", END)
# graph6.add_edge("subtract_node", END)
# app= graph6.compile()
# intial_state=agentstate6(
#     operation="add",
#     number1= 10,
#     number2= 20,
# )
# result=app.invoke(intial_state)
# print(result)


#excerise conditional graph

class agentstate7(TypedDict):
    number1: int
    number2: int
    operation: str
    finalnumber: int
    number3: int
    number4: int
    finalnumber2: int
    operation2: str

def add_node(state: agentstate7) -> agentstate7:
    """ this is the add node1 """
    return{
        "finalnumber": state["number1"] + state["number2"]
    }
def subtract_node(state: agentstate7) -> agentstate7:
    """ this is the subtract node1 """
    return{
        "finalnumber": state["number1"] - state["number2"]
    }
def decide_next_node(state: agentstate7) -> agentstate7:
    """ this is the decide next node1 """
    if state["operation"] == "add":
        return "add_operation"
    elif state["operation"] == "subtract":
        return "subtraction_operation"

state7=StateGraph(agentstate7)
state7.add_node("add_node", add_node)
state7.add_node("subtract_node", subtract_node)
state7.add_node("router", lambda state:state)
state7.add_edge(START, "router")
state7.add_conditional_edges(
        "router",
        decide_next_node,
        {
            "add_operation": "add_node",
            "subtraction_operation": "subtract_node"
        }
    )
state7.add_edge("add_node", "router2")
state7.add_edge("subtract_node", "router2")
def add_node2(state: agentstate7) -> agentstate7:
    """ this is the add node2 """
    return{
        "finalnumber2": state["number3"] + state["number4"]
    }
def subtract_node2(state: agentstate7) -> agentstate7:
    """ this is the subtract node2 """
    return{
        "finalnumber2": state["number3"] - state["number4"]
    }
def decide_next_node2(state: agentstate7) -> agentstate7:
    """ this is the decide next node2 """
    if state["operation2"] == "add":
        return "add_operation2"
    elif state["operation2"] == "subtract":
        return "subtraction_operation2"

state7.add_node("add_node2", add_node2)
state7.add_node("subtract_node2", subtract_node2)
state7.add_node("router2", lambda state:state)
state7.add_conditional_edges(
        "router2",
        decide_next_node2,
        {
            "add_operation2": "add_node2",
            "subtraction_operation2": "subtract_node2"
        }
    )
state7.add_edge("add_node2", END)
state7.add_edge("subtract_node2", END)
app7=state7.compile()
result7=app7.invoke({"number1": 10, "number2": 20, "number3": 30, "number4": 40, "operation": "add", "operation2": "add"})
print(result7)
    




    
    

