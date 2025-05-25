from openai import OpenAI
from decouple import config
import streamlit as st
import json

# 建立OpenAI物件
api_key = config('OPENAI_API_KEY')
client = OpenAI(api_key=api_key)

# Chat模型
model_name="gpt-4.1"

# 設定json檔案
file_name = "hist_data.json"

# 清除json檔案
def reset_hist():
    open(file_name, "w")    

# 取得對話歷史記錄
def get_hist():
    hist = []
	# 加入聊天角色的設定
    hist.append({"role": "developer", "content": "你會說中文, 是聰明的助理"})

    try:
		# 開啟json檔案，將檔案內容加入hist串列
        with open(file_name) as f:
            data = json.load(f)             
            for item in data:
                hist.append(item)
    except Exception as e:
        pass

    return hist

# 儲存對話記錄
def save_hist(user_msg, reply_msg):
	# 取出對話歷史記錄，忽略聊天角色的設定
    hist = get_hist()[1:]

	# 將新的問題及回應加入hist串列
    hist.append({"role": "user", "content": user_msg})
    hist.append({"role": "assistant", "content": reply_msg})

	# 將hist串列儲存至json檔案
    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(hist, f)

# 取得問題的串列回應訊息
def gpt_response(messages):
    stream = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role":m["role"], "content":m["content"]} for m in messages
        ],
        stream=True
    )   
    return stream

# 加入【新對話】按鈕
if st.sidebar.button("新對話"):
    reset_hist()

# 取得對話歷史，存入messages串列
messages = get_hist()
for message in messages:
	# 顯示對話角色及內容
   	with st.chat_message(message["role"]):
   		st.markdown(message["content"])

# 判斷是否使用者有輸入問題
if prompt:= st.chat_input("輸入問題"): 
	# 將輸入問題加入messages串列
    messages.append({
        "role": "user",
        "content": prompt
    })

	# 顯示使用者問題
    with st.chat_message("user"):
        st.markdown(prompt)

	# 顯示assistant回應訊息
    with st.chat_message("assistant"):
		# 取得串流回應訊息
        stream = gpt_response(messages)

		# 顯示串流回應訊息
        resp=st.write_stream(stream)

		# 將回應訊息加入messages串列        
        messages.append({"role":"assistant", "content":resp})

    # 將問題及回應存入json檔案
    save_hist(prompt, resp)
