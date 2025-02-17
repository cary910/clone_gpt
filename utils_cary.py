import streamlit as st
import os
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain_openai import ChatOpenAI

def get_chat_response(prompt,memory,openai_api_key):
    model = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=openai_api_key)
    chain = ConversationChain(llm=model, memory=memory)

    response = chain.invoke({"input":prompt})
    return response["response"] #要访问字典的值，可以指定字典名并且把键放在方括内

# memory = ConversationBufferMemory(return_messages=True)
# print(get_chat_response("牛顿提出过哪些指名的定律",memory, os.getenv("OPENAI_API_KEY")))
# print(get_chat_response("我上一个问的问题是什么",memory, os.getenv("OPENAI_API_KEY")))
