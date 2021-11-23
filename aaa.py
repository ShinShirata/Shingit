# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 16:07:13 2021

@author: shin
"""

import streamlit as st
from PIL import Image
st.title('初めてのstreamlit')
st.write('私の名前はShinです。')
text = st.text_input('貴方の名前を教えてください。')
'貴方の名前は,', text, 'です。'
condition=st.slider('貴方の今の調子は？',0,100,80)
'コンディション:',condition
option=st.selectbox(
    '好きな数字を教えてください。',
    list(['1番','2番','3番','4番','5番'])
    )
'貴方が選択したのは,',option,'です。'

left_column,right_column=st.columns(2)
button=left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムです')
    
img = Image.open('sample.bmp')
st.image(img,caption='肉',use_column_width=True)

st.title('作品')
import streamlit as st


def main():
    selected_item = st.radio('どっちが好き?',
                             ['イヌ', 'ネコ'])
    if selected_item == 'イヌ':
        st.write('ワンワン！')
    else:
        st.write('ニャーニャー～')
        

        
        
if __name__ == '__main__':
    main()        

button_state = st.button('Say hello')
if button_state:
    st.write('バイバーイ')
else:
    st.write('押してみて！')
