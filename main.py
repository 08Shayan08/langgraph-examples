from typing import TypedDict
from langgraph.graph import StateGraph
import math
#graph 1
class agentstate(TypedDict):
    name: str


def greeting_node(state: agentstate) -> agentstate:
    return {
        "name": "Hello, how are you?" + state["name"]
    }


graph=StateGraph(agentstate)

graph.add_node("greeting", greeting_node)

graph.set_entry_point("greeting")
graph.set_finish_point("greeting")
app=graph.compile()
result=app.invoke({"name": "John"})
print(result["name"])

#graph 2
class agentstate2(TypedDict):
    name: str
    result: int 
    values: list[int]

def add_node(state: agentstate2) -> agentstate2:
    return{
        "result": f"hey {state['name']}, your result is {sum(state['values'])}"
    }

graph2=StateGraph(agentstate2)
graph2.add_node("add", add_node)
graph2.set_entry_point("add")

graph2.set_finish_point("add")
app2=graph2.compile()

result2=app2.invoke({"name": "John", "values": [1, 2, 3, 4, 5]})

print(result2["result"])

#graph 3
class agentstate3(TypedDict):
    name: str
    result: int
    values: list[int]
    operation: str

def add_node(state: agentstate3) -> agentstate3:
    if state["operation"] == "+":
        return{
            "result":f"hey {state['name']}, your result is {sum(state['values'])}"
        }
    elif state["operation"] == "*":
        return{
            "result": f"hey {state['name']}, your result is {math.prod(state['values'])}"
        }

graph3=StateGraph(agentstate3)
graph3.add_node("add", add_node)
graph3.set_entry_point("add")
graph3.set_finish_point("add")
app3=graph3.compile()

result3=app3.invoke({"name": "John", "values": [1, 2, 3, 4, 5], "operation": "*"})
print(result3["result"])