import streamlit as st
import pandas as pd

font_css = """
<style>
button[data-baseweb="tab"] > div[data-testid="stMarkdownContainer"] > p {
  font-size: 24px;
}
</style>
"""

st.markdown(font_css, unsafe_allow_html=True)

stats, setup, scores = st.tabs(['Statistics', 'Setup', 'Scores'])

with stats:
    st.markdown("<h2 style='text-align: center; color: white; font-size: 40pt;'>Total of 503 labeled images with around 10 labels each</h2>", True)
    st.write("")
    st.markdown("<h2 style='text-align: center; color: white; font-size: 40pt;'>Split into 60% training, 30% validation and 10% test sets</h2>", True)
    st.write("")
    st.markdown("<h2 style='text-align: center; color: white; font-size: 40pt;'>With augmentations this became 8100 images for training and 800 for validation</h2>", True)
    st.write("")
    st.markdown("<h2 style='text-align: center; color: white; font-size: 40pt;'>Roboflow handles the data flow,  ultralytics the training, detection and later tracking</h2>", True)

with setup:
    st.markdown("<h2 style='text-align: center; color: white; font-size: 40pt;'>Used up Google Colab capacity very quickly, switched to AWS G5 GPU spot instances</h2>", True)
    st.write("")
    st.markdown("<h2 style='text-align: center; color: white; font-size: 40pt;'>16-32 cores and a Nvidia A10 GPU with 24GB of RAM</h2>", True)
    st.write("")
    st.markdown("<h2 style='text-align: center; color: white; font-size: 40pt;'>Training on the large YOLO model took around 12 hours<BR> Training on the smallest YOLO model took only 2 hours</h2>", True)

with scores:
    _, c2, _ = st.columns([1, 4, 1])

    hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """
    
    # Inject CSS with Markdown
    c2.markdown(hide_table_row_index, unsafe_allow_html=True)

    # style
    th_props = [
    ('font-size', '45px'),
    ('text-align', 'center'),
    ('font-weight', 'bold'),
    #('color', '#6d6d6d'),
    #('background-color', '#f7ffff')
    ]
                                
    td_props = [
    ('font-size', '50px')
    ]
                                    
    styles = [
    dict(selector="th", props=th_props),
    dict(selector="td", props=td_props)
    ]

    df = pd.DataFrame(data={'model':['nano', 'medium', 'large'], 'mAP50': ['86.6%', '88.4%', '89.2%'], 'precision': ['92.8%', '92.6%', '91.9%'], 'recall': ['79.6%', '81.4%', '83.3%']})
    df=df.style.set_properties(**{'text-align': 'left'}).set_table_styles(styles)
    c2.table(df)

    st.markdown("<h2 style='text-align: center; color: white; font-size: 40pt;'>Consequence: Using the nano model (6MB vs 250MB) is encouraged since the loss is almost negligable and the small model can be used for live detection as well</h2>", True)