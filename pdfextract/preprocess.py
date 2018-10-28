import pytesseract
from PIL import Image
import cv2
import os

def preprocess(filename):
  img = cv2.imread(filename, 0)
  blur = cv2.GaussianBlur(img, (3,3), 0)
  ret, threshold = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
  cv2.imshow('temp', threshold)

  filename = os.path.basename(filename)
  outputFilename = '../temp/img/'+'.'.join(filename.split('.')[:-1])+'.png'

  cv2.imwrite(outputFilename, threshold)
  return outputFilename

def ocr(filename):
  img = Image.open(filename)
  return pytesseract.image_to_string(img)

def read(filenames):
 for filename in filenames:
   inputImage = preprocess(filename)
   outputText = ocr(inputImage)
   filename = os.path.basename(filename)
   outputFilename = '.'.join(filename.split('.')[:-1])+'.txt'
   f = open('../temp/txt/'+outputFilename, 'w')
   f.write(outputText)
   f.close()

if __name__ == '__main__':
  filenames = os.listdir('../images')
  filenames = ['../images/'+filename for filename in filenames]
  read(filenames)
