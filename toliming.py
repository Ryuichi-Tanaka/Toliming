import streamlit as st
from PIL import Image
import os

st.write('## 画像トリミングアプリ')
uploaded_file=st.file_uploader("ファイルアップロード", type='jpg')
try:
    if st.checkbox('画像表示'):
        image=Image.open(uploaded_file)
        st.image(image,caption = 'アップロード画像',use_column_width = True)
        
except:
    st.error('画像が選択されていません')

resize_value = st.sidebar.slider("リサイズするサイズを選択してください (px)", 100, 1000, 670)

if st.button('トリミング開始'):
    image=Image.open(uploaded_file)
    resized_image = image.resize((resize_value, resize_value))
    st.success("選択された画像のリサイズ処理が完了しました。")
    st.image(resized_image, caption='リサイズされた画像', use_column_width=True)
    cropped_image = resized_image.crop(resized_image.getbbox())
    filename = "uploaded_file.jpg"
    filepath = os.path.join(os.environ['USERPROFILE'],filename)
    cropped_image.save(filepath)