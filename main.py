import numpy as np
from pyzbar.pyzbar import decode
import cv2
#Reading QR code
img = cv2.imread("test.png")
code = decode(img)
for barcode in decode(img):
    # print(barcode.data)
    text = barcode.data.decode('utf-8')
    print(text)
    print(barcode.rect)