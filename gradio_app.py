import gradio as gr
from PIL import Image
import numpy as np
import torch
print("Gradio app started")

model = torch.load('license-plate.pt', map_location=torch.device('cpu'))
model.eval()

def predict_license_plate(image):
    
    # Make prediction
    prediction = model.predict(image_array)

    return str(prediction[0])

interface = gr.Interface(
    fn=predict_license_plate,
    inputs=gr.Image(type='pil',label="Upload Vehicle Image"),
    outputs=gr.Textbox(label="Predicted License Plate"),
    title="License Plate Recognition")

if __name__ == "__main__":
    interface.launch()