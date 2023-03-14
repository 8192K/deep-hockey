import streamlit as st

font_css = """
<style>
button[data-baseweb="tab"] > div[data-testid="stMarkdownContainer"] > p {
  font-size: 24px;
}
</style>
"""

st.markdown(font_css, unsafe_allow_html=True)

orig, anot, slow = st.tabs(['Original', 'Annotated', 'Slow motion'])

orig.video('data/vid/eck_ecn_excerpt_short.mp4')
anot.video('data/vid/eck_ecn_excerpt_short_annotated.mp4')
slow.video('data/vid/eck_ecn_excerpt_short_annotated_slow.mp4')
