import streamlit as st
import gradio as gr

st.set_page_config(page_title="License Plate Recognition", page_icon="🚗")

st.title("🚘 License Plate Recognition")
st.write("Upload an image of a vehicle to recognize its license plate.")
st.components.v1.iframe("http://127.0.0.1:7860", height=600,scrolling=True)