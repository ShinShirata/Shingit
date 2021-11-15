# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 17:22:46 2021

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

st.latex(r'''
...     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
...     \sum_{k=0}^{n-1} ar^k =
...     a \left(\frac{1-r^{n}}{1-r}\right)
...     ''')

st.success('This is a success message!')

import streamlit as st
import plotly.graph_objects as go
import numpy as np

st.title('Superquadrics')
st.sidebar.subheader('Formulas')
# st.latex(r'\left|\frac{x}{a}\right|^s + \left|\frac{y}{b}\right|^t + \left|\frac{z}{c}\right|^u = 1')
# st.markdown('where $r$, $s$, and $t$ are positive real numbers that determine the main features of the superquadric, and $a$, $b$, and $c$ are scaling parameters.')
st.sidebar.latex(r'\left(\left|\frac{x}{a}\right|^{n_2} + \left|\frac{y}{b}\right|^{n_2}\right)^\frac{n_1}{n_2} + \left|\frac{z}{c}\right|^{n_1} = 1')
st.sidebar.markdown('where $n_1$ and $n_2$ are shape parameters, and $a$, $b$, and $c$ are scaling parameters.')
# st.subheader('Formula python code')
# with st.echo():
import numpy as np
@st.cache
def superquadrics(a,b,c,n1,n2,x,y,z):
    values = np.power(np.power(np.abs(x/a),n2) \
                    + np.power(np.abs(y/b),n2),n1/n2) \
            + np.power(np.abs(z/c),n1)
    return values
X, Y, Z = np.mgrid[-1:1:20j, -1:1:20j, -2:2:40j]
st.sidebar.subheader('Parameters')
a  = 1.
b  = 1.
c  = st.sidebar.slider('c (a=b=1)', .2, 2., 1., .2)
n1 = st.sidebar.slider('n1', 1, 10, 10, 1)
n2 = st.sidebar.slider('n2', 1, 10, 2, 1)
fig = go.Figure(data=go.Isosurface(
    x = X.flatten(),
    y = Y.flatten(),
    z = Z.flatten(),
    value = superquadrics(a,b,c,n1,n2,X,Y,Z).flatten(),
    isomin = .5,
    isomax = 1,
    showscale = False,
))
fig.update_layout(
    scene = dict(
        xaxis_title='',
        yaxis_title='',
        zaxis_title='',
        xaxis = dict(
            showbackground = False,
            showline = False,
            showticklabels = False,
        ),
        yaxis = dict(
            showbackground = False,
            showline = False,
            showticklabels = False,
        ),
        zaxis = dict(
            showbackground = False,
            showline = False,
            showticklabels = False,
        ),
    )
)
st.write(fig)
st.subheader('Code')
st.markdown('* https://github.com/ken2s/superquadrics/blob/main/st_superquadrics.py')
st.subheader('References')
st.markdown('* https://en.wikipedia.org/wiki/Superquadrics')