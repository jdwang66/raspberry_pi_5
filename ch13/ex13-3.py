import streamlit as st
from PIL import Image

st.title("Media Gallery")

# 加入影像檔案上傳
upload_image = st.file_uploader("Upload an image", type=["png","jpg","jpeg"])
if upload_image is not None:
    img = Image.open(upload_image)
    # 變更影像大小
    img = img.resize((320, 210))    
    st.image(img, caption="Uploaded image")

# 加入視訊檔案上傳
upload_video = st.file_uploader("Upload a video file", type=["mp4"])
if upload_video is not None:    
    st.video(upload_video)

# 加入音訊檔案上傳
upload_audio = st.file_uploader("Upload a audio file", type=["mp3", "wav"])
if upload_audio is not None:   
    st.audio(upload_audio)
