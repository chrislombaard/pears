import os
import PIL

from PIL import Image
from io import BytesIO


def load_image(image):
    """
    Load, resize a portrait or landscape image.
    """
    # Open the uploaded image
    pil_image = Image.open(image)

    # Grab the extension and the file format
    img_format = pil_image.format

    # Resize or modify the image
    portrait_sizes = (320, 568)
    landscape_sizes = (640, 480)
    square_sizes = (600, 600)
    # If Square -> (550, 550)
    width, height = pil_image.size

    if width < height:  # Portrait
        resize_dim = portrait_sizes
    elif height < width:  # Landscape
        resize_dim = landscape_sizes
    else:
        resize_dim = square_sizes

    # Highest quality Image resizing filters as of this version of PIL.
    # https://pillow.readthedocs.io/en/3.0.x/releasenotes/2.7.0.html#antialias-renamed-to-lanczos
    pil_image = pil_image.resize((resize_dim[0], resize_dim[1]), PIL.Image.LANCZOS)

    # After all necessary modifications, save to the database.
    image_file = BytesIO()
    pil_image.save(fp=image_file, format=img_format, quality=100)
    image_file.seek(0)

    file_type = "image/" + img_format.lower()

    return {
        "img": image_file,
        "file_type": file_type,
        "width": resize_dim[0],
        "height": resize_dim[1],
    }
