import os
import numpy as np
import pandas as pd
from PIL import Image
from tqdm import tqdm
from transformers import CLIPProcessor, CLIPModel
import torch
import faiss

image_dir = '/kaggle/input/codecum/extracted_data/dataset'
image_files = sorted([f for f in os.listdir(image_dir) if f.endswith('.png')])

model = CLIPModel.from_pretrained('openai/clip-vit-base-patch32')
processor = CLIPProcessor.from_pretrained('openai/clip-vit-base-patch32')

def get_image_embedding(image_path):
    try:
        image = Image.open(image_path)
        inputs = processor(images=image, return_tensors="pt")
        with torch.no_grad():
            outputs = model.get_image_features(**inputs)
        return outputs.numpy().flatten()
    except Exception as e:
        print(f"Error processing {image_path}: {e}")
        return None

embeddings = []
valid_image_files = []

for image_file in tqdm(image_files):
    image_path = os.path.join(image_dir, image_file)
    embedding = get_image_embedding(image_path)
    if embedding is not None:
        embeddings.append(embedding)
        valid_image_files.append(image_file)

embeddings = np.array(embeddings)

index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

_, indices = index.search(embeddings, 7)

results = {}
for i, image_file in enumerate(valid_image_files):
    neighbors = [valid_image_files[idx] for idx in indices[i] if idx != i]
    results[image_file] = ' '.join(neighbors[:6])

df = pd.DataFrame(list(results.items()), columns=['filename', 'ranking'])
df.to_csv('submission.csv', index=False)