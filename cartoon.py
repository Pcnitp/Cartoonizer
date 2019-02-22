#Importing libraries
import tkinter
import cv2
from tkinter import filedialog
import imutils

#Creating a Window as user interface
window=tkinter.Tk()
window.title("Cartoonizer")
window.geometry("300x300")

def helper():
    #taking image input from user
    file_path = filedialog.askopenfilename()
    
    #reading image
    img = cv2.imread(file_path)
    
    #Resizing image 
    img = imutils.resize(img, width=300)
    
    #reducing noise by bilateral Filter
    color = cv2.bilateralFilter(img, 6, 100, 100)
    
    #making it non-realistic by stylizing
    img1=cv2.stylization(color, sigma_s=600, sigma_r=0.4)
    
    #converting into gray scale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #removing noise
    gray = cv2.medianBlur(gray, 5)
    #getting edges
    edges = cv2.adaptiveThreshold(gray, 400, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5, 5)

    #adding edges to stylized image
    cartoon = cv2.bitwise_and(img1, img1, mask=edges)
    
    #Showing images
    #cv2.imshow("original", img)
    #cv2.imshow("color", color)
    #cv2.imshow("edges", edges)
    #cv2.imshow("stylized", img1)
    cv2.imshow("cartoon", cartoon)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
B=tkinter.Button(window, text="Upload",command=helper)

B.pack()
window.mainloop()