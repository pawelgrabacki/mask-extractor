"""Script"""

import os
import time
from PIL import Image


# Extracts the alpha channel from PNG files and saves it as a separate mask image.


def create_mask():
    """Creates mask"""
    found = False
    for f in os.listdir("."):
        if f.lower().endswith(".png"):
            found = True
            img = Image.open(f).convert("RGBA")
            alpha = img.getchannel("A")
            fn, _ = os.path.splitext(f)
            alpha.save(f"masks/{fn}_mask.png")
            print(f"{f} is done")

    if not found:
        print("No PNG files found.")


# Create 'masks' directory if it doesn't exist
os.makedirs("masks", exist_ok=True)

create_mask()
print("Done!")
time.sleep(4)
