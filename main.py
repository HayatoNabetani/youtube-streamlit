import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title("streamlit入門")

st.write("DataFrame")

# プログレスバー
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.1)


# 2カラムレイアウト
left_column, right_column= st.columns(2)
button = left_column.button('右から無に文字を表示')

if button:
    right_column.text('test!')

# トグルバー
expander = st.expander('問い合わせ')
expander.write('おと岩瀬を描く')

# セレクトボックス
option = st.selectbox(
    'あなたの好きな数字を教えて',
    list(range(1,11))
)

f'あなたの好きな数字は{option}です。'

# テキストボックス
text = st.text_input(
    'あなたの趣味を教えて'
)
f'あなたの好きな趣味は{text}です。'

# スライダー
condition = st.slider(
    'あなたの今の調子は？', 
    0,100,50
)

f'あなたの調子は{condition}です。'