from openai import OpenAI
from decouple import config
import streamlit as st

# 建立OpenAI物件
api_key = config('OPENAI_API_KEY')
client = OpenAI(api_key=api_key)

# 列出模型列表
models = client.models.list()

# 取得模型的 id
model_list=[m.id for m in models.data]

# 排序 id
model_list.sort()

# 顯示模型 id
st.title("List models")
st.write(model_list)
