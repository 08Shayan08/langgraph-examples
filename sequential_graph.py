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

#excercise 1
class agentstate5(TypedDict):
    name: str
    age: str
    skills: list[str]
    final: str

def first_node(state: agentstate5) -> agentstate5:
    """ this is the first node that will greet the user"""
    return{
        "final": "hi" + state["name"]
    }

def second_node(state: agentstate5) -> agentstate5:
    """ this is the second node that will ask the user for their age"""
    return{
        "final": state["final"] + " your age is " + state["age"]
    }

def third_node(state: agentstate5) -> agentstate5:
    """ this is the third node that will ask the user for their skills"""
    return{
        "final": state["final"] + " your skills are " + ", ".join(state["skills"])
    }

graph5=StateGraph(agentstate5)
graph5.add_node("first", first_node)
graph5.add_node("second", second_node)
graph5.add_node("third", third_node)
graph5.add_edge("first", "second")
graph5.add_edge("second", "third")
graph5.set_entry_point("first")
graph5.set_finish_point("third")
app5=graph5.compile()
result5=app5.invoke({"name": "John", "age": "20", "skills": ["python", "java", "c++"]})
print(result5["final"])
from IPython.display import Image, display
display(Image(app5.get_graph().draw_mermaid_png()))
    