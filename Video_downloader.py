import streamlit as st
import streamlit.components.v1 as components
import youtube_dl
import os

st.markdown("<h1 style = 'text-align:center; color:orange;'>Welcome to Our page </h1>", unsafe_allow_html=True)
st.markdown("<h1 style = 'text-align:center; color:white;'>Here you can download Youtube Instagram Facebook Video and Audio </h1>", unsafe_allow_html=True)
page_bg_img = '''
<style>
body {
background-image: url("https://ak.picdn.net/shutterstock/videos/3644240/thumb/1.jpg");
background-size: cover;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)
st.markdown("<h1 style = 'text-align:left; color:green;'>Enter your link here</h1>", unsafe_allow_html=True)
url = st.text_input("")
st.markdown("<h1 style = 'text-align:left; color:orange;'>How would you like to download </h1>", unsafe_allow_html=True)
option = st.selectbox('',('','Video', 'Audio'))
if option == " ":
    st.write("choose Video or Audio")
if option == "Video":
    try:
        os.chdir('Desktop')
        ydl_opts = {'format': 'best',
            'quiet': True,}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        st.markdown("<h1 style = 'text-align:center; color:yellow;'>The video is downloaded </h1>", unsafe_allow_html=True)
    except Exception as e:
        print(e)
if option == "Audio":
    try:
        os.chdir('Desktop')
        ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [
            {'key': 'FFmpegExtractAudio','preferredcodec': 'mp3',
             'preferredquality': '192',
            },
            {'key': 'FFmpegMetadata'},
        ],
    }

        os.chdir('Desktop')
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        st.markdown("<h1 style = 'text-align:center; color:rose;'>The audio is downloaded </h1>", unsafe_allow_html=True)
    except Exception as e:
        print(e)
st.markdown("<a href = 'https://www.youtube.com/'>Visit Youtube </a>", unsafe_allow_html=True)
st.markdown("<a href = 'https://twitter.com/'>Visit Twitter</a>", unsafe_allow_html=True)
st.markdown("<a href = 'https://www.instagram.com/'>Visit Twitter</a>", unsafe_allow_html=True)
st.markdown("<a href = 'https://www.facebook.com/'>Visit Facebook </a>", unsafe_allow_html=True)
from PIL import Image
image = Image.open('a.png')
st.image(image,use_column_width=True)
st.markdown("<h1 style = 'text-align:center; color:violet;style=font-size:300%;style=font-family:verdana;'>These are the supported websites</h1>", unsafe_allow_html=True)


