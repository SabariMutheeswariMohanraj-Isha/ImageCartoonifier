import cv2
import os
import numpy as np
import datetime
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from tkmacosx import Button
import matplotlib.pyplot as plt
from tkinter.font import Font

def upload():
    try:
        global filePath
        filePath = filedialog.askopenfilename()
        upload = Image.open(filePath)
        upload = upload.resize((300, 300),Image.ANTIALIAS)
        #print("Uploaded")
        img = ImageTk.PhotoImage(upload)  
        #cv2.imshow(img)
        picture.configure(image=img)
        picture.image=img
        picture.pack(side=TOP,expand=True)
        #plt.imshow(picture)
        
        #label.configure(text="",fg="red",font=('montserrat',20, "bold"))
    
    except:
        pass
    
    
def cartoonify(filePath):
    
    global dtmy,cartoon
    
    x = datetime.datetime.now()
    dtmy = x.strftime("%d-%b-%y")
    
    
    img = Image.open(filePath)
    img = img.resize((600,400))
    img = np.array(img)
    
    label.configure(foreground = "#ad3e72", text = "Cartooned Image",font=('montserrat',20))
    
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)    
    
    gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    gray = cv2.medianBlur(gray,5)
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
    #plt.imshow(edges,cmap= "gray")
    
    ctn = cv2.bilateralFilter(img,9,250,250)
    cartoon = cv2.bitwise_and(ctn,ctn,mask = edges)
    #plt.imshow(cartoon)
    cv2.imshow("Cartoon Art",cartoon)
        
    return cartoon
    
def lineEdge(filePath):
    
    global dtmy,edges
    
    x = datetime.datetime.now()
    dtmy = x.strftime("%d-%b-%y")
    
    
    img = Image.open(filePath)
    img = img.resize((600,400))
    img = np.array(img)
    
    label.configure(foreground = "#ad3e72", text = "Edge Image",font=('montserrat',20))

    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)    
    
    gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    gray = cv2.medianBlur(gray,5)
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
    cv2.imshow("Line Art",edges)
    
    return edges


#filePath = "../Cartoonify/Data/"



def saveCartoon(res):
    global result
    path = '../Cartoonify/CartoonImag/Cartooned/'
    cv2.imwrite(os.path.join(path , 'Cartoonify_'+dtmy+'.jpg'), res)


def saveEdgeLine(edge):
    path = '../Cartoonify/CartoonImag/Edges/'
    cv2.imwrite(os.path.join(path , 'EdgesImage_'+dtmy+'.jpg'),edge)

    


#I = "Image saved at "+ path
#tk.messagebox.showinfo(title=None, message=I)

top=tk.Tk()
top.geometry('1200x800')
top.title('Cartoonify Image')
top.configure(background='white')
label = tk.Label(top, background = "white", font = ("montserrat",15,"bold"))

picture = tk.Label(top)

## hex - #293861

## IMAGE CARTOONIFIER--Image Cartoonifier
heading = Label(top, text="IMAGE CARTOONIFIER",pady=10, font=('montserrat',21,"bold"))
heading.configure(background='white',foreground='#434f70')
heading.pack(side=TOP,pady=20)
#heading.grid(row=10,column=5)

Cartoonify_button = Button(top,text="Cartoonified Image", command = lambda : cartoonify(filePath), borderless=1, padx=15,pady=10)
Cartoonify_button.configure(background="#ffcbc4", foreground="#383838",font=("montserrat",15))
#Cartoonify_button.configure(background="white", foreground="#447f80",font=("montserrat",15),highlightbackground="#447f80",highlightthickness=1)
Cartoonify_button.pack(side=LEFT,padx=10)
#Cartoonify_button.grid(row=3,column=3)

LineEdge_button = Button(top,text="Line Edge Image", command = lambda : lineEdge(filePath), borderless=1, padx=15,pady=10)
LineEdge_button.configure(background="#ffcbc4", foreground="#383838",font=("montserrat",15))
LineEdge_button.pack(side=RIGHT,padx=10)
#LineEdge_button.grid(row=3,column=6)

saveC = Button(top,text="Save Cartoon Image",command=lambda: saveCartoon(cartoon),padx=30,pady=5)
saveC.configure(background="#ffcbc4", foreground="#383838",font=("montserrat",15))
saveC.pack(side=BOTTOM,padx=10,pady=5)
#saveC.grid(row=3,column=9)

saveE = Button(top,text="Save LineEdge Image",command=lambda: saveEdgeLine(edges),padx=30,pady=5)
saveE.configure(background="#ffcbc4", foreground="#383838",font=("montserrat",15))
saveE.pack(side=BOTTOM,padx=10,pady=5)
#saveE.grid(row=3,column=12)

upload = Button(top,text="Upload Image",command=upload,padx=10,pady=5)
upload.configure(background='#434f70', foreground='white',font=('montserrat',20))
upload.pack(side=TOP,pady=30)
#upload.grid(row=3,column=1)


label.pack(side=TOP,expand=True)
#label.grid(row=3,column=3)

top.mainloop()

#cv2.waitKey(0)
#cv2.destroyAllWindows()
