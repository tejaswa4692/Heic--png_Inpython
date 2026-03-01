from PIL import Image
import pillow_heif
import os

#This script is written by epic tejaswas divine intellect for a frined please star this repo im desperate


pillow_heif.register_heif_opener()

folder_name: str = "outputimages"

os.makedirs(folder_name, exist_ok=True)

files = os.listdir(".")

for i in files: 
    nameoffile = i.lower()
    if nameoffile.endswith(".heic"):

        print(nameoffile + " is being converted...")
        
        input_path = nameoffile
        output_path = os.path.join(folder_name, nameoffile.replace(".heic", ".png"))

        image = Image.open(input_path)
        image.save(output_path, "PNG")

        print("Conversion complete.")
