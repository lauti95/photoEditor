# Script for editing all images from local Images folder to new 'editedImgs' folder

from PIL import Image, ImageEnhance, ImageFilter
import os

# Create output directory (insert your own path in between apostrophes)
path = r'C:\Users\lauta\OneDrive\Imágenes'
pathOut = r'C:\Users\lauta\OneDrive\Imágenes\editedImgs'
if not os.path.exists(pathOut):
    os.makedirs(pathOut)

# Script
for filename in os.listdir(path):

    if filename.endswith('.jpg') or filename.endswith('.png'):
        img = Image.open(f'{path}\{filename}')

        # Filters
        edit = img.filter(ImageFilter.SHARPEN)

        # Contrast (modify factor to desired values)
        factor = 1.5
        enhancer = ImageEnhance.Contrast(edit)
        edit = enhancer.enhance(factor)

        # Output
        clean_name = os.path.splitext(filename)[0]
        edit.save(f'{pathOut}\{clean_name}_edited.jpg')