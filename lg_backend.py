from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph,END,START
from typing import TypedDict,Annotated
from langgraph.checkpoint.memory import InMemorySaver
from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages
from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
llm=ChatOpenAI(model="gpt-4o-mini",api_key=api_key)

class chatState(TypedDict):
    messages:Annotated[list[BaseMessage],add_messages]
def chat_node(state:chatState):
    msg=state['messages']
    res=llm.invoke(msg)
    return {'messages':res}
check_p=InMemorySaver()
graph=StateGraph(chatState)
graph.add_node('chat_node',chat_node)
graph.add_edge(START,'chat_node')
graph.add_edge('chat_node',END)
chat_bot=graph.compile(checkpointer=check_p)