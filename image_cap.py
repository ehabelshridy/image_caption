import gradio as gr
import numpy as np
from PIL import Image
from transformers import AutoProcessor, BlipForConditionalGeneration

# 1. حمّل الـ Processor والـ Model الجاهزين
processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# 2. دالة بتعمل Caption للصورة
def caption_image(input_image: np.ndarray):
    # حوّل الصورة من numpy → PIL Image وحطها RGB
    raw_image = Image.fromarray(input_image).convert("RGB")

    # حضّر الـ inputs للصورة
    inputs = processor(images=raw_image, return_tensors="pt")

    # اعمل Generate للتوكنز
    output = model.generate(**inputs, max_length=50)

    # فك التوكنز للنص
    caption = processor.decode(output[0], skip_special_tokens=True)

    return caption

# 3. واجهة Gradio
iface = gr.Interface(
    fn=caption_image,
    inputs=gr.Image(type="numpy"),
    outputs="text",
    title="🖼️ Image Captioning",
    description="ارفع صورة وخلي النموذج يوصفلك محتواها باستخدام BLIP."
)

# 4. شغّل التطبيق
if __name__ == "__main__":
    iface.launch()
