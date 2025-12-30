import streamlit as st
from ultralytics import YOLO
from IPython.display import Image

@st.cache_resource
def load_model():
    return YOLO('licese-plate.pt')
model = load_model()

st.set_page_config(page_title="License Plate Recognition", page_icon="🚗")

st.title("🚘 License Plate Recognition")
st.write("Upload an image or video of a vehicle to recognize license plate.")
uploaded = st.file_upload('Choose an image...',type=['jpg','jpeg','png'])

if uploaded is not None:
    if uploaded.type.startswith('image'):
        img = Image.open(uploaded).convet("RGB")
        st.image(img,caption='uploaded image',use_column_width=True)

        pred = model.predict(img)
        pred[0].plot()[ :,:,::-1]