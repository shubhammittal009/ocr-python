from PIL import Image
import pytesseract

# im = Image.open("images/sample.jpg")
im = Image.open("images/sample2.png")

text = pytesseract.image_to_string(im, lang="eng")

print(text)