#Importing libraries
import tkinter
import cv2
from tkinter import *
from tkinter import filedialog
import numpy as np
import imutils

#Creating a Window as user interface
window=tkinter.Tk()
window.title("Cartoonizer")
window.geometry("300x300")

def helper():
    #taking image input from user
    file_path = filedialog.askopenfilename()
    img = cv2.imread(file_path)
    img = imutils.resize(img, width=300)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    #applying bilateral filter and then threshold
    color = cv2.bilateralFilter(img, 5, 400, 400)
    ret, image = cv2.threshold(color, 127, 255, cv2.THRESH_TOZERO)
    
    Z = image.reshape((-1,3))
    Z = np.float32(Z)
    
    #Applying k means clustering
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    
    K=8
    ret, label1, center1 = cv2.kmeans(Z, K, None,criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
       
    center1 = np.uint8(center1)
    res1 = center1[label1.flatten()]
    o1 = res1.reshape((img.shape)) 
    
    #o1[np.where((o1 == [0,255,255]).all(axis = 2))] = [255,224,189]
              
    o1 = cv2.cvtColor(o1, cv2.COLOR_RGB2BGR)
    cv2.imshow("cartoon", o1)
    #cv2.imshow("img", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

       
lable=tkinter.Label(window, text="Click on upload to select an image")
B=tkinter.Button(window, text="Upload",command=helper)

B.pack()
lable.pack()
window.mainloop()