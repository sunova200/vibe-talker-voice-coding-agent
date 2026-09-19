import os
from typing import Annotated
from typing_extensions import TypedDict
from dotenv import load_dotenv

from langchain.chat_models import init_chat_model
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.tools import tool

from langgraph.graph import StateGraph, START, END, add_messages
from langchain_groq import ChatGroq                    # ✅ Groq instead of Gemini
from langgraph.prebuilt import ToolNode, tools_condition

load_dotenv()

# ✅ Groq — fast, free, no quota issues
# llm = ChatGroq(
#     model="llama-3.1-8b-instant",
#     api_key=os.getenv("GROQ_API_KEY")
# )

class State(TypedDict):
    messages: Annotated[list, add_messages]

@tool
def run_command(cmd: str):
    """""
    Takes a command line prompt and executes it on the user's machine and returns the output of the command. 
    Example: run_command(cmd="ls) where ls is the command to list the files 
    """""
    result = os.system(command=cmd)
    return result

# llm = ChatGroq(
#     model="llama-3.1-8b-instant",
#     api_key=os.getenv("GROQ_API_KEY")
llm = init_chat_model(
        model_provider="groq",
        model="llama-3.1-8b-instant",
    )
llm_with_tools = llm.bind_tools(tools=[run_command])
                        
    
    
    

def chatbot(state: State):
    system_prompt = SystemMessage(content="""
    You are a helpful AI Coding assistant who take an input from and based on tools you choose the correct tool and execute the command.
                                 
    You can even execute commands and help user with the output of the command.
     
         Always make sure to keep your generated codes and files in chat_gpt/ folder
       
                                 """ )
    message = llm_with_tools.invoke([system_prompt] + state["messages"])
    assert len(message.tool_calls) <= 1
    return {"messages": [message]}

tools = [run_command]
tool_node = ToolNode(tools=[run_command])

graph_builder = StateGraph(State)
graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("tools", tool_node)
graph_builder.add_edge(START, "chatbot")
graph_builder.add_conditional_edges("chatbot", tools_condition)
graph_builder.add_edge("tools", "chatbot")
graph_builder.add_edge("chatbot", END)

def create_chat_graph(checkpointer=None):
    return graph_builder.compile(checkpointer=checkpointer)



################################################--------------------------------------------------------#########################

# import os
# from typing import Annotated
# from typing_extensions import TypedDict
# from dotenv import load_dotenv

# from langchain_core.tools import tool                  # ✅ FIX 1: missing import
# from langchain_core.messages import SystemMessage      # ✅ FIX 2: SystemMessage not SytemMessage

# from langgraph.graph import StateGraph, START, END, add_messages  # ✅ FIX 3: correct import
# from langchain_groq import ChatGroq
# from langgraph.prebuilt import ToolNode, tools_condition

# load_dotenv()

# class State(TypedDict):
#     messages: Annotated[list, add_messages]

# @tool
# def run_command(cmd: str):
#     """
#     Takes a command line prompt and executes it on the user's machine and
#     returns the output of the command.
#     Example: run_command(cmd="ls") where ls is the command to list the files.
#     """
#     result = os.popen(cmd).read()                      # ✅ FIX 4: os.popen returns output, os.system doesn't
#     return result

# # ✅ FIX 5: Clean Groq setup — removed commented out mess
# llm = ChatGroq(
#     model="llama-3.1-8b-instant",
#     api_key=os.getenv("GROQ_API_KEY")
# )

# llm_with_tools = llm.bind_tools(tools=[run_command])   # ✅ FIX 6: bind run_command not empty list

# def chatbot(state: State):
#     system_prompt = SystemMessage(content="""
#         You are an AI Coding assistant who takes an input from user and based on available
#         tools you choose the correct tool and execute the commands.

#         You can even execute commands and help user with the output of the command.
#         Always make sure to keep your generated codes and files in vibe_talker/ folder.
#         You can create the folder if it does not already exist.
#     """)
#     message = llm_with_tools.invoke([system_prompt] + state["messages"])
#     # ✅ FIX 7: removed assert — it crashes if AI makes multiple tool calls
#     return {"messages": [message]}

# tool_node = ToolNode(tools=[run_command])              # ✅ FIX 8: removed empty tools = []

# graph_builder = StateGraph(State)
# graph_builder.add_node("chatbot", chatbot)
# graph_builder.add_node("tools", tool_node)
# graph_builder.add_edge(START, "chatbot")
# graph_builder.add_conditional_edges("chatbot", tools_condition)
# graph_builder.add_edge("tools", "chatbot")
# graph_builder.add_edge("chatbot", END)

# def create_chat_graph(checkpointer=None):
#     return graph_builder.compile(checkpointer=checkpointer)