
from PIL import Image

lemur = Image.open("lemur.png")
flag = Image.open("flag.png")

pixels_lemur = lemur.load() # create the pixel map
pixels_flag = flag.load()
print(pixels_flag)