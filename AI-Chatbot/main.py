from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama
import streamlit as st
import os
from dotenv import load_dotenv
# from langchain_ollama import OllamaLLM

load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

## Prompt Template

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please respond to user queries."),
        ("user","Question:{question}")
    ]
)
## streamlit framework

st.title('LangChain + Ollama Chatbot')
input_text=st.text_input("Ask a question")

# Ollama chat model (local inference)
llm=ChatOllama(model="llama2", temperature=0.7)
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))