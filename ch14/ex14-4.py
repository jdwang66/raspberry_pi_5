from openai import OpenAI
from decouple import config
import streamlit as st

# 建立OpenAI物件
api_key = config('OPENAI_API_KEY')
client = OpenAI(api_key=api_key)

# Chat模型
model_name="gpt-4.1"

# 加入聊天輸入框
message=st.chat_input("輸入問題")

# 取得message的串流回應
def gpt_response(message):
    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "developer", "content": "你會說中文, 是聰明的助理"},
            {"role": "user", "content": message}
        ],
        stream=True
    )   
    return response

if message:
	# 顯示message訊息
    with st.chat_message("user"):
        st.write(message)
    
    resp = gpt_response(message)

	# 顯示串流回應
    with st.chat_message("assistant"):        
        st.write_stream(resp)
