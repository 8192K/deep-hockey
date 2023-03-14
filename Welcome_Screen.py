import streamlit as st

st.set_page_config(layout='wide')

st.markdown("<h1 style='text-align: center; color: white; font-size: 50pt;'>Detecting and Tracking Actors<BR> in Ice Hockey Live TV Broadcasts</h1>", True)
st.write("")
st.write("")
st.write("")
st.markdown("<h2 style='text-align: center; color: white; font-size: 35pt;'>by Sebastian Frehmel</h1>", True)
st.write("")
st.write("")
st.write("")
st.write("")

c1, c2, c3 = st.columns([1, 4, 1])

with c1:
    st.write("")
    st.write("")
    st.write("")
    c1.columns([1, 4, 1])[1].image('images/spiced_logo.jpg')

with c2:
    st.markdown("<h1 style='text-align: center; color: white;'>Data Science Bootcamp</h1>", True)
    st.markdown("<h1 style='text-align: center; color: white;margin-top:-35px;'>Spiced Academy, Berlin</h1>", True)
    st.markdown("<h2 style='text-align: center; color: white;'>Gradient Masala<BR>Dec 5th, 2022 - March 15th, 2023</h2>", True)

with c3:
    st.write("")
    st.write("")
    st.write("")
    c3.columns([1, 4, 1])[1].image('images/spiced_logo.jpg')
