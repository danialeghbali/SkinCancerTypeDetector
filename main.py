import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from tkinter import Tk 
from tkinter import messagebox
from tkinter.filedialog import askopenfilename

cancerName=["Basal cell carcinoma (BCC)","Melanoma","Solar Keratoses"]
data=["BCC makes up about two-thirds (66%) of non-melanoma skin cancers.BCC commonly develops on the head, neck and upper body",
"Melanoma is the least common type of skin cancer, (accounting for approximately 1-2% of cases), but it is the most serious",
"Generally hard, red, scaly spots on sun exposed areas of the skin"]

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing

def process(fileName):
    img_rgb = cv.imread(fileName)
    img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
    db=[]
    for i in range(1,3):
       template = cv.imread('database/db'+str(i)+'.jpg',0)
       w, h = template.shape[::-1]
       res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)
       threshold = 0.9
       loc = np.where( res >= threshold)
       num=0
       for pt in zip(*loc[::-1]):
         cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 1)
         num+=1
       db.append(num)
    return db.index(max(db))
    #cv.imwrite('res'+ str(i) +'.png',img_rgb)
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
index=process(filename)
messagebox.showinfo(cancerName[index], data[index])