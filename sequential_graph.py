from typing import TypedDict
from langgraph.graph import StateGraph

class agentstate4(TypedDict):
    name: str
    age: str
    final: str 

def first_node(state: agentstate4) -> agentstate4:
    """ this is the first node"""
    return{
        "final": "hi " + state["name"]
    }


def second_node(state: agentstate4) -> agentstate4:
    """ this is the second node"""
    return{
        "final": state["final"] + "your age is " + state["age"]
    }

graph4=StateGraph(agentstate4)
graph4.add_node("first", first_node)
graph4.add_node("second", second_node)
graph4.add_edge("first", "second")
graph4.set_entry_point("first")
graph4.set_finish_point("second")
app4=graph4.compile()
result4=app4.invoke({"name": "John", "age": "20"})
print(result4)
