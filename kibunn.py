# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 17:13:30 2021

@author: shin
"""

import streamlit as st

from PIL import Image
st.title('最高の快楽を提案します♪')
option = st.selectbox('貴方の今の気分は何でしょうか？',
                      ('-','眠い～','お腹が空いた～','お酒を飲みたい！','動画を見たい！'))
if option == ('眠い～'):
    st.write('布団を温かくして寝ましょう♪')
    img = Image.open('sleep_top_man.png')
    st.image(img,caption='',use_column_width=True)
    option=st.radio('貴方のお役に立てたでしょうか？',('-',' はい',' いいえ',))
if option==(' はい'):
    st.write('貴方のお役に立てて光栄です♪')
if option==(' いいえ'):
     st.write('貴方のお役に立てられず不甲斐ないです(´･ω･｀)')
if option==('お腹が空いた～'):
    option = st.selectbox('この中で何が食べたいですか？',('-','ラーメン','寿司','焼肉'))
if option ==('ラーメン'):
    option = st.selectbox('ラーメンの味は何味がよろしいでしょうか？',('-','味噌','塩','醤油','黒胡椒味噌'))
if option ==('味噌'):
    st.write('味噌ラーメンが食べたい貴方には魂心家の味噌味がお勧めです！')
    img = Image.open('miso.jpg')
    st.image(img,caption='',use_column_width=True)
    option=st.radio('貴方のお役に立てたでしょうか？',('-','  はい','  いいえ',))
if option==('  はい'):
    st.write('貴方のお役に立てて光栄です♪')
if option==('  いいえ'):
     st.write('貴方のお役に立てられず不甲斐ないです(´･ω･｀)')
if option ==('塩'):
    st.write('塩ラーメンが食べたい貴方には魂心家の塩味がお勧めです！')
    img = Image.open('sio.jpg')
    st.image(img,caption='',use_column_width=True)
    option=st.radio('貴方のお役に立てたでしょうか？',('-','   はい','   いいえ',))
if option==('   はい'):
    st.write('貴方のお役に立てて光栄です♪')
if option==('   いいえ'):
     st.write('貴方のお役に立てられず不甲斐ないです(´･ω･｀)')
if option ==('醤油'):
    st.write('醤油ラーメンが食べたい貴方には魂心家の醤油味がお勧めです！')
    img = Image.open('syouyu.jpg')
    st.image(img,caption='',use_column_width=True)
    option=st.radio('貴方のお役に立てたでしょうか？',('-','    はい','    いいえ',))
if option==('    はい'):
    st.write('貴方のお役に立てて光栄です♪')
if option==('    いいえ'):
     st.write('貴方のお役に立てられず不甲斐ないです(´･ω･｀)')
if option ==('黒胡椒味噌'):
    st.write('黒胡椒味噌ラーメンが食べたい貴方には魂心家の黒胡椒味噌味がお勧めです！')
    img = Image.open('kurokosyoumiso.jpg')
    st.image(img,caption='',use_column_width=True)
    option=st.radio('貴方のお役に立てたでしょうか？',('-','     はい','     いいえ',))
if option==('     はい'):
    st.write('貴方のお役に立てて光栄です♪')
if option==('     いいえ'):
     st.write('貴方のお役に立てられず不甲斐ないです(´･ω･｀)')
if option==('寿司'):
    st.write('きときと寿司はいかがでしょうか？おいしいお寿司が頂けます♪')
    img = Image.open('susi.jpg')
    st.image(img,caption='',use_column_width=True)
    option=st.radio('貴方のお役に立てたでしょうか？',('-','       はい','       いいえ',))
if option==('       はい'):
    st.write('貴方のお役に立てて光栄です♪')
if option==('      いいえ'):
     st.write('貴方のお役に立てられず不甲斐ないです(´･ω･｀)')
if option==('焼肉'):
    option = st.selectbox('リーズナブルな焼肉がよろしいでしょうか？それとも高級焼肉がよろしいでしょうか？',('-','リーズナブル','高級'))
if option ==('リーズナブル'):
    st.write('熟成焼肉　いちばんはいかがでしょうか？')
    img = Image.open('itibann.jpg')
    st.image(img,caption='',use_column_width=True)
    option=st.radio('貴方のお役に立てたでしょうか？',('-','       はい','       いいえ',))
if option==('       はい'):
    st.write('貴方のお役に立てて光栄です♪')
if option==('       いいえ'):
     st.write('貴方のお役に立てられず不甲斐ないです(´･ω･｀)')
if option ==('高級'):
    st.write('信州焼肉　悠雅亭はいかがでしょうか？')
    img = Image.open('yuu.jpg')
    st.image(img,caption='',use_column_width=True)
    option=st.radio('貴方のお役に立てたでしょうか？',('-','        はい','        いいえ',))
if option==('        はい'):
    st.write('貴方のお役に立てて光栄です♪')
if option==('        いいえ'):
     st.write('貴方のお役に立てられず不甲斐ないです(´･ω･｀)')
if option ==('お酒を飲みたい！'):
    option = st.selectbox('がっつりお酒を飲みたいですか？それともお洒落な所でお酒を嗜みたいですか？',('-','がっつり飲む！','お洒落な所で'))
if option ==('がっつり飲む！'):
    st.write('ゴールデン酒場の飲み放題はいかがでしょうか？男性は1580円、女性は1180円で2時間飲み放題が可能です♪')
    img = Image.open('go-den.jpg')
    st.image(img,caption='',use_column_width=True)
    option=st.radio('貴方のお役に立てたでしょうか？',('-','         はい','         いいえ',))
if option==('         はい'):
    st.write('貴方のお役に立てて光栄です♪')
if option==('         いいえ'):
     st.write('貴方のお役に立てられず不甲斐ないです(´･ω･｀)')
if option ==('お洒落な所で'):
    st.write('Di PUNTO（ディプント）はいかがでしょうか？窓から見える夜景が綺麗ですよ♪')
    img = Image.open('delipunnto.jpg')
    st.image(img,caption='',use_column_width=True)
    option=st.radio('貴方のお役に立てたでしょうか？',('-','          はい','          いいえ',))
if option==('          はい'):
    st.write('貴方のお役に立てて光栄です♪')
if option==('          いいえ'):
     st.write('貴方のお役に立てられず不甲斐ないです(´･ω･｀)')
if option==('動画を見たい！'):
    option = st.selectbox('どのアプリケーションで動画を見たいですか？',('-','YouTube','Amazon Prime','TikTok'))
if option==('YouTube'):
    option = st.selectbox('どんな動画を見たいですか？',('-','ゲーム実況','エンタメ',))
if option==('ゲーム実況'):
    st.write('SAWAYAN GAMESはいかがでしょうか？外国人がマリオカートをしている動画で台パンしている姿が面白いですよ♪')
    img = Image.open('sawa.jpg')
    st.image(img,caption='',use_column_width=True)
    option=st.radio('貴方のお役に立てたでしょうか？',('-','            はい','             いいえ',))
if option==('            はい'):
    st.write('貴方のお役に立てて光栄です♪')
if option==('            いいえ'):
     st.write('貴方のお役に立てられず不甲斐ないです(´･ω･｀)')
if option==('エンタメ'):
    st.write('東海オンエアはいかがでしょうか？登録者数600万人声の大人気Youtuberです。寝たら速帰宅の旅が面白いですよ♪')
    img = Image.open('onnea.jpg')
    st.image(img,caption='',use_column_width=True)
    option=st.radio('貴方のお役に立てたでしょうか？',('-','             はい','             いいえ',))
if option==('             はい'):
    st.write('貴方のお役に立てて光栄です♪')
if option==('             いいえ'):
     st.write('貴方のお役に立てられず不甲斐ないです(´･ω･｀)')
if option==('Amazon Prime'):
    option = st.selectbox('どんな動画を見たいですか？',('-','冒険','エンタメ',))
if option==('冒険'):
    st.write('ワンピースはいかがでしょうか？ルフィーが海賊王になる物語です♪')
    img = Image.open('wannpi.jpg')
    st.image(img,caption='',use_column_width=True)
    option=st.radio('貴方のお役に立てたでしょうか？',('-','              はい','               いいえ',))
if option==('              はい'):
    st.write('貴方のお役に立てて光栄です♪')
if option==('              いいえ'):
     st.write('貴方のお役に立てられず不甲斐ないです(´･ω･｀)')
if option==('エンタメ'):
    st.write('ODDTAXIはいかがでしょうか？クスッと笑えてしまいます♪')
    img = Image.open('taxi.jpeg')
    st.image(img,caption='',use_column_width=True)
    option=st.radio('貴方のお役に立てたでしょうか？',('-','               はい','               いいえ',))
if option==('               はい'):
    st.write('貴方のお役に立てて光栄です♪')
if option==('               いいえ'):
     st.write('貴方のお役に立てられず不甲斐ないです(´･ω･｀)')
if option==('TikTok'):
    st.write('TikTokは色々な動画が短い時間で見ることができるから自分でお気に入りの動画を探して見ましょう♪')
    img = Image.open('tiktok.png')
    st.image(img,caption='',use_column_width=True)
    option=st.radio('貴方のお役に立てたでしょうか？',('-','はい','いいえ',))
if option==('はい'):
    st.write('貴方のお役に立てて光栄です♪')
if option==('いいえ'):
     st.write('貴方のお役に立てられず不甲斐ないです(´･ω･｀)')



















