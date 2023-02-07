## https://towardsdatascience.com/read-text-from-image-with-one-line-of-python-code-c22ede074cac

#%%

## USING OPENCV AND PYTESSERACT
import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

img = cv2.imread('images/read-text-from-image1.png')
text = pytesseract.image_to_string(img)
print(text)

print('-------------------------')

img = cv2.imread('images/read-text-from-image2.png')
text = pytesseract.image_to_string(img)
print(text)

# %%
