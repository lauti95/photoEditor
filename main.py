from PIL import Image, ImageEnhance, ImageFilter
import os

# Create output directory
path = r'C:\Users\lauta\OneDrive\Imágenes'  # insert your own path in between the apostrophes
pathOut = r'C:\Users\lauta\OneDrive\Imágenes\editedImgs'    #insert path leaving \editedImgs at the end
if not os.path.exists(pathOut):
    os.makedirs(pathOut)

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