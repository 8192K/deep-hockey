import streamlit as st

c1, c2 = st.columns([1.4, 5])
c1.image('images/roboflow.png')
c2.markdown("<h2 style='text-align: center; color: white; font-size: 40pt;margin-top:-16px;'> is a(n almost) free platform that makes it easy to label large amounts of data efficiently</h2>", True)

st.markdown("<h2 style='text-align: center; color: white; font-size: 40pt;'>Roboflow workflow</h2>", True)

font_css = """
<style>
button[data-baseweb="tab"] > div[data-testid="stMarkdownContainer"] > p {
  font-size: 24px;
}
</style>
"""

st.markdown(font_css, unsafe_allow_html=True)

up_img, ass, label, interm, version, train, auto_label, repeat = \
    st.tabs(['Upload images', 'Assignment', 'Labeling', 'Intermediate dataset', 'Version', 'Train locally', 'Automatic labeling', 'Repeat'])

up_img.image('images/roboflow_upload.png', width=1000)

with ass:
    ass1, ass2, ass3, ass4 = st.tabs(['Assign', 'Categories', 'Unannotated', 'Annotated'])

    ass1.image('images/roboflow_assign.png', width=1000)
    ass2.image('images/roboflow_assign_blocks.png', width=1000)
    ass3.image('images/roboflow_assign_block_view.png', width=1000)
    ass4.image('images/roboflow_assign_block_view_ready.png', width=1000)

with label:
    lab1, lab2, lab3 = st.tabs(['Use COCO', 'Manual labeling', 'Layers'])

    lab1.image('images/roboflow_label_coco.png', width=1000)
    lab2.image('images/roboflow_label_self.png', width=1000)
    lab3.image('images/roboflow_label_layers.png', width=1000)

interm.image('images/roboflow_dataset.png', width=1000)

with version:
    ver1, ver2, ver3 = st.tabs(['Preprocessing', 'Augmentations', 'Overview'])

    ver1.image('images/roboflow_version_preprocess.png', width=1000)
    ver2.image('images/roboflow_version_augmentations.png', width=1000)
    ver3.image('images/roboflow_version_overview.png', width=1000)

with train:
    st.image('images/roboflow_yolo_notebook.png', width=1000)
    st.header("Run YOLO training in notebook on a GPU system. Then upload to Roboflow again.")

with auto_label:
    al1, al2, al3 = st.tabs(['Select new model', 'Select classes', 'Result'])

    al1.image('images/roboflow_autolabel_select1.png', width=1000)
    al2.image('images/roboflow_autolabel_select2.png', width=1000)
    al3.image('images/roboflow_autolabel_result.png', width=850)
    al3.header('Only refine automatic bounding boxes.')

with repeat:
    st.markdown("<h2 style='text-align: center; color: white; font-size: 40pt;'>Repeat until dataset is large enough and model is good enough</h2>", True)
    st.write("")
    st.markdown("<h2 style='text-align: center; color: white; font-size: 40pt;'>Labelling process took more than a week...!</h2>", True)