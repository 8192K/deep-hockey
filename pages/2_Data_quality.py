import streamlit as st

st.markdown("<h2 style='text-align: center; color: white; font-size: 40pt;'>DEL2 broadcasts in 1280x720 pixels (720p)</h2>", True)
st.markdown("<h2 style='text-align: center; color: white; font-size: 40pt;'>Broadcast quality can vary much as they are done semi-professionally by the teams themselves", True)


_, c2, _ = st.columns([2, 4, 2])
with c2:
    font_css = """
    <style>
    button[data-baseweb="tab"] > div[data-testid="stMarkdownContainer"] > p {
    font-size: 24px;
    }
    </style>
    """

    st.markdown(font_css, unsafe_allow_html=True)

    good, bad, ind = st.tabs(['Good', 'Bad', 'Indistinguishable'])

    with good:
        st.image('images/good_quality.png', width=800)

    with bad:
        st.image('images/bad_quality.png', width=800)

    with ind:
        st.image('images/pixel_mesh.png', width=600)

st.write("")
st.markdown("<h2 style='text-align: center; color: white; font-size: 40pt;'>Challenge: Gather enough input from various arenas with all kinds of jersey colors and broadcast qualities", True)