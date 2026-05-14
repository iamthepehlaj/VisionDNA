from PIL import Image

image = Image.open("input.jpg")

print("Image Size:", image.size)
print("Image Mode:", image.mode)