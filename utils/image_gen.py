import shutil
from gradio_client import Client
import os
from PIL import Image

def image_gen(prompt):
    your_repo_path = "/Users/aditya.narayan/Desktop/form-to-ppt/generated_images"
    os.makedirs(your_repo_path, exist_ok=True)

    client = Client("LLMhacker/Realtime-FLUX-Modified-Flux.Schnell-for-JA.P")
    result = client.predict(
        prompt=prompt,
        seed=42,
        width=1024,
        height=1024,
        api_name="/generate_image"
    )

    image_path, seed_used, latency = result

    if os.path.exists(image_path):
        # Convert and save as JPEG
        with Image.open(image_path) as im:
            jpeg_filename = os.path.splitext(os.path.basename(image_path))[0] + ".jpeg"
            destination = os.path.join(your_repo_path, jpeg_filename)
            im.convert("RGB").save(destination, "JPEG")

        print(f"✅ Image converted and saved as: {destination}")

        os.remove(image_path)
        print(f"🗑️ Temp file deleted: {image_path}")

        print(f"ℹ️  Seed used: {seed_used}")
        print(f"⏱️  Generation latency: {latency}")
    else:
        print("❌ Error: Temp image file does not exist.")