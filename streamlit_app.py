from os import path
import streamlit as st
from PIL import Image

st.markdown("<h1 style='text-align: center; color: white;'>WORDLE</h1>", unsafe_allow_html=True)

download = Image.open('Capture2.PNG')

download1 = Image.open('Capture1.PNG')

download2 = Image.open('Capture.PNG')

#st.title("WORDLE")

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#path = "C:\\Users\\sandi\\OneDrive\\Desktop\\wordle\\.streamlit\\style.css"

st.image(download, caption=None, width=450, use_column_width=450, clamp=False, channels="RGB", output_format="auto")

st.caption('In above graph, you will see the maximum frequencies of the letter in 5 letter words.',unsafe_allow_html = False)

st.image(download1, caption=None, width=450, use_column_width=450, clamp=False, channels="RGB", output_format="auto")

st.caption('In above wordcloud, you will see the maximum frequencies of 5 letter words entered by the user.',unsafe_allow_html = False)

st.image(download2, caption=None, width=450, use_column_width=450, clamp=False, channels="RGB", output_format="auto")

st.caption('In above graph, you will see the average round of solving the 5 letter words. Here, -1 means that the user is unable to solve the wordle in six round.',unsafe_allow_html = False)

st.caption('For Wordle 354, my guess was trait. 🟩🟩🟩🟩🟩 !!!!!!')

st.caption("For getting today's Wordle as well as for getting new Wordle for next or other days you have to run Wordle 1 by 6 Jupyter Notebook.")