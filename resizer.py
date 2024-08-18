from PIL import Image

def resize_image(image_path, new_path, width, height):
  image = Image.open(image_path)
  new_image = image.resize((width, height))
  new_image.save(new_path)

