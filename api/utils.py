import numpy as np
from sklearn.cluster import KMeans
from PIL import Image
import os

def extract_colors(image_path, num_colors=5):
    image = Image.open(image_path).resize((150, 150))
    pixels = np.array(image).reshape(-1, 3)

    kmeans = KMeans(n_clusters=num_colors)
    kmeans.fit(pixels)
    return kmeans.cluster_centers_.astype(int)

def save_palette_as_image(colors, output_path):
    palette = np.zeros((100, 100 * len(colors), 3), dtype=np.uint8)
    for i, color in enumerate(colors):
        palette[:, i*100:(i+1)*100, :] = color
    Image.fromarray(palette).save(output_path)
