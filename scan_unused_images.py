import glob
import os

# Configuration
PROJECT_DIR = '../thesis/'        # Root folder with .tex files
IMAGE_FOLDER = f'{PROJECT_DIR}/images' # Root image folder (may have subfolders)
IMAGE_EXTENSIONS = ('png', 'jpg', 'jpeg', 'pdf', 'eps')

image_files = []
for ext in IMAGE_EXTENSIONS:
    pattern = os.path.join(IMAGE_FOLDER, '**', f'*.{ext}')
    image_files.extend(glob.glob(pattern, recursive=True))

tex_files = []
for root, _, files in os.walk(PROJECT_DIR):
    for file in files:
        if file.endswith('.tex'):
            tex_files.append(os.path.join(root, file))


all_tex_content = ""
for tex_file in tex_files:
    with open(tex_file, 'r', encoding='utf-8') as f:
        all_tex_content += f.read()

unused_images = []
for img in image_files:
    img_name = os.path.splitext(img)[0]  # strip extension
    if img_name not in all_tex_content:
        unused_images.append(img)

if unused_images:
    for img in unused_images:
        print(f" - {img}")
else:
    print("All images are used in the .tex files!")
