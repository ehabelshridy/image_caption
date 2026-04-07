import gradio as gr
import numpy as np
from PIL import Image
from transformers import AutoProcessor, AutoModelForImageTextToText

# 1. Load the pre-trained BLIP model and its corresponding processor from Hugging Face
# The processor handles image resizing and text encoding/decoding
processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = AutoModelForImageTextToText.from_pretrained("Salesforce/blip-image-captioning-base")

def caption_image(input_image):
    """
    This function takes an image, processes it through the BLIP model,
    and returns a generated text description (caption).
    """
    if input_image is None:
        return ""

    # 2. Convert input to PIL Image if it's a numpy array
    if isinstance(input_image, np.ndarray):
        image = Image.fromarray(input_image)
    else:
        image = input_image
    
    # 3. Pre-process the image into a format the model understands (PyTorch tensors)
    inputs = processor(image, return_tensors="pt")
    
    # 4. Use the model to generate the token IDs for the caption
    out = model.generate(**inputs)
    
    # 5. Decode the generated tokens back into a human-readable string
    caption = processor.decode(out[0], skip_special_tokens=True)
    
    return caption

# 6. Define the Gradio Web Interface
# We explicitly define the input as gr.Image() to ensure compatibility
iface = gr.Interface(
    fn=caption_image,
    inputs=gr.Image(label="Upload your image"), # Updated input component
    outputs=gr.Textbox(label="Image Description"), # Updated output component
    title="Image Captioning with BLIP",
    description="This app uses AI to describe the content of any image you upload."
)

# 7. Launch the local web server
iface.launch(server_name="0.0.0.0", server_port=7860)
