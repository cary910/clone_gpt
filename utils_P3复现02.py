from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
import os

def get_chat_response(prompt, memory,api_key):

    model = ChatOpenAI(
        model="qwen-max",
        api_key = api_key,
        base_url = "https://dashscope.aliyuncs.com/compatible-mode/v1"
    )
    chain = ConversationChain(llm=model,memory=memory)
    response = chain.invoke({"input": prompt})
    return response["response"]

