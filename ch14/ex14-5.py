from openai import OpenAI
from decouple import config
import streamlit as st

# 建立OpenAI物件
api_key = config('OPENAI_API_KEY')
client = OpenAI(api_key=api_key)

# Chat模型
model_name="gpt-4.1"

# 取得messages的串流回應訊息
def gpt_response(messages):
    stream = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role":m["role"], "content":m["content"]} for m in messages
        ],
        stream=True
    )   
    return stream

# 初始化messages串列
if "messages" not in st.session_state:
    st.session_state.messages=[]

# 顯示messages串列內容
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 判斷是否有使用者輸入訊息
if prompt:= st.chat_input("輸入問題"):
	# 將輸入訊息加入messages串列
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

	# 顯示user輸入的訊息
    with st.chat_message("user"):
        st.markdown(prompt)

	# 顯示Chat回應的串流訊息
    with st.chat_message("assistant"):
		# 取得串流回應訊息
        stream = gpt_response(st.session_state.messages)

		# 顯示串流回應訊息
        resp=st.write_stream(stream)

		# 顯示結果加入messages串列中
        st.session_state.messages.append({"role":"assistant", "content":resp})
