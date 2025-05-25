from openai import OpenAI
from decouple import config
import streamlit as st

# 建立OpenAI物件
api_key = config('OPENAI_API_KEY')
client = OpenAI(api_key=api_key)

# chat模型
model_name="gpt-4.1"

# 加入單行文字輸入框
message=st.text_input("輸入問題","台北那裡最好玩?請給200字說明")

# 取得message訊息的回應
def gpt_response(message):
    completion = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "developer", "content": "你會說中文, 是聰明的助理"},
            {"role": "user", "content": message}
        ]
    )
    response = completion.choices[0].message.content
    return response

if st.button("確定"):
    if message:
		# 取得message訊息的回應
        resp = gpt_response(message)
		
		# 顯示回應
        st.write(resp)
