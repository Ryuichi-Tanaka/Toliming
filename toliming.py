import streamlit as st
from PIL import Image
import os

st.write('## 画像トリミングアプリ')
uploaded_files=st.file_uploader("ファイルアップロード", type=('jpg','png'),accept_multiple_files=True)
try:
    if st.checkbox('画像表示'):
        for uploaded_file in uploaded_files:
            image=Image.open(uploaded_file)
            st.image(image,caption = 'アップロード画像',use_column_width = True)
        
except:
    st.error('画像が選択されていません')

resize_value = st.sidebar.slider("リサイズするサイズを選択してください (px)", 100, 1000, 670)

i = 0
if st.button('トリミング開始'):
    for uploaded_file in uploaded_files:

        image=Image.open(uploaded_file)
        resized_image = image.resize((resize_value, resize_value))
        st.success("選択された画像のリサイズ処理が完了しました。")
        st.image(resized_image, caption='リサイズされた画像', use_column_width=True)
        cropped_image = resized_image.crop(resized_image.getbbox())
        filename = f"{i}uploaded_file.jpg"
        i+=1
        filepath = os.path.join(os.environ['USERPROFILE'],filename)
        cropped_image.save(filepath)