import io #The io module provides Python’s main facilities for dealing with various types of IO.
import json #JSON (JavaScript Object Notation) is a lightweight data-interchange format
import cv2 # cv2.imread(), cv2.imshow() , cv2.imwrite()
import numpy as np #create a NumPy array, use broadcasting, access values, manipulate arrays, and much more
import requests #Make a request to a web page, and print the response text
import matplotlib.pyplot as plt  #Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python.
img = cv2.imread(ImagesCNI.jpg)

height, width, _ = img.shape
height
width,height
url_api = httpsapi.ocr.spaceparseimage
_, compressedimage = cv2.imencode(.jpg, img, [1, 90])
file_bytes = io.BytesIO(compressedimage)
result = requests.post(url_api,
              files = {screenshot.jpg file_bytes},
              data = {apikey K85968086288957,
                      language fre})
result = result.content.decode()
result = json.loads(result)
parsed_results = result.get(ParsedResults)[0]
text_detected = parsed_results.get(ParsedText)
text_detected