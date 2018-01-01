import pytesseract
#加载图文库
from PIL import Image

image = Image.open("./timg.jpg")
txt = pytesseract.image_to_string(image)

print(txt)
