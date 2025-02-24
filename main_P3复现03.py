import streamlit as st
from langchain.memory import ConversationBufferMemory
from utils_P3复现02 import get_chat_response

st.title("Cary的聊天机器人")
with st.sidebar:
    api_key = st.text_input("请输入您的API密钥:",type="password")
    st.markdown("[阿里云密钥获取地址](https://bailian.console.aliyun.com/?apiKey=1#/api-key)")

if "memory" not in st.session_state:
    st.session_state["memory"]=ConversationBufferMemory(return_messages=True)
    st.session_state["messages"]=[{"role":"ai","content":"您好！我是您的AI聊天助手，请问有什么可以帮您？"}]

for message in st.session_state["messages"]:
    st.chat_message(message["role"]).write(message["content"])

prompt = st.chat_input()
if prompt:
    if not api_key:
        st.info("请输入您的API密钥")
        st.stop()
    st.session_state["messages"].append({"role":"human","content":prompt})
    st.chat_message("human").write(prompt)

    with st.spinner("AI正在思考，请稍候..."):
        response = get_chat_response(prompt,st.session_state["memory"], api_key)
    msg = {"role":"ai","content": response}
    st.session_state["messages"].append(msg)
    st.chat_message("ai").write(response)