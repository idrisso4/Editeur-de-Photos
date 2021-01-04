# Author: idrisso4
# Main file


# Import Libraries
from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import *
import matplotlib.image as mpimg
import numpy as np
import matplotlib.pyplot as plt


# Import functions from edit_image.py
from edit_image import lecture_img as ima
from edit_image import r90d as deg
from edit_image import negatif as n
from edit_image import green as gr
from edit_image import gray as g


# Define functions
def ini(i):
    global img
    img=ima(i)
    plt.imshow(img)
    plt.show()

def degr(i):
    global img
    img=deg(i)
    plt.imshow(img)
    plt.show()

def neg(i):
    global img
    img=n(i)
    plt.imshow(img)
    plt.show()

def green(i):
    global img
    img=gr(i)
    plt.imshow(img)
    plt.show()

def black(i):
    global img
    img=g(i)
    plt.imshow(img)
    plt.show()

def dossier():
    global path
    path=filedialog.askdirectory()

def saisie():
    global nom
    nom=entre.get()

def fichier():
    global fil
    global img
    if entree.get()=='':
        fil=filedialog.askopenfilename(filetypes = [("Fichiers PNG","*.png")])
        img=ima(fil)
    else:
        fil=entree.get()
        img=ima(fil)

def alertex():
    global ask
    ask=askyesno('Warning','Are you sure to quit?')
    if ask==1:
        return(f.destroy())

def save(i):
    saisie()
    mpimg.imsave('C:/Users/assus/Desktop/'+nom,i)



# Main program
# Create the window
f=Tk()
f.geometry("600x650+250+30")
f.title("photo editor")
f['bg']='turquoise'
a=("Times", "15", "bold")

# Define the Frame File
l=LabelFrame(f,font=a,fg='blue',text="File",padx=20,pady=10,borderwidth=2)
l.config(bg="turquoise")
Label(l,text="Open Image",bg='turquoise',font=a).pack()
# Define Buttons
butimage1=PhotoImage(file='bouton/dossier.png')
bout1=Button(l,command= lambda:fichier())
bout1.config(bg='turquoise',image=butimage1)
entree=Entry(l,width=40,font=("Times", "15"))
bout1.pack()
entree.pack()
l.pack(fill='both',pady=5)


# Define the Frame Rotation
l3=LabelFrame(f,font=a,fg='blue',text="Rotation",padx=20,pady=20,borderwidth=2)
l3.config(bg="turquoise")
# Define Buttons
butimage2=PhotoImage(file='bouton/boy1.png')
bout2=Button(l3,command=lambda:ini(fil))
bout2.config(bg='turquoise',image=butimage2)
bout2.pack(padx=40,pady=10,side=LEFT)
butimage3=PhotoImage(file='bouton/boy2.png')
bout3=Button(l3,command=lambda:degr(deg(deg(img))))
bout3.config(bg='turquoise',image=butimage3)
bout3.pack(padx=40,pady=10,side=LEFT)
butimage4=PhotoImage(file='bouton/boy3.png')
bout4=Button(l3,command=lambda:degr(deg(img)))
bout4.config(bg='turquoise',image=butimage4)
bout4.pack(padx=40,side=RIGHT,pady=10)
butimage5=PhotoImage(file='bouton/boy4.png')
bout5=Button(l3,command=lambda:degr(img))
bout5.config(bg='turquoise',image=butimage5)
bout5.pack(side=RIGHT,padx=40,pady=10)
l3.pack(fill='both',pady=5)


# Define the Frame Colors
l4=LabelFrame(f,font=a,fg='blue',text="Colors",padx=20,pady=20,borderwidth=2)
l4.config(bg="turquoise")
# Define Buttons
butimage11=PhotoImage(file='bouton/boy1.png')
bout11=Button(l4,command=lambda:ini(fil))
bout11.config(bg='turquoise',image=butimage11)
bout11.pack(padx=40,pady=10,side=LEFT)
butimage12=PhotoImage(file='bouton/boy5.png')
bout12=Button(l4,command=lambda:neg(img))
bout12.config(bg='turquoise',image=butimage12)
bout12.pack(padx=40,pady=10,side=LEFT)
butimage13=PhotoImage(file='bouton/boy7.png')
bout13=Button(l4,command=lambda:green(img))
bout13.config(bg='turquoise',image=butimage13)
bout13.pack(padx=40,side=RIGHT,pady=10)
butimage14=PhotoImage(file='bouton/boy6.png')
bout14=Button(l4,command=lambda:black(img))
bout14.config(bg='turquoise',image=butimage14)
bout14.pack(side=RIGHT,padx=40,pady=10)
l4.pack(fill='both',pady=5)


# Define the Frame Saving
l2=LabelFrame(f,font=a,fg='blue',text="Save",padx=20,pady=20,borderwidth=2)
l2.config(bg="turquoise")
l11=Frame(l2)
l11.config(bg="turquoise")
l1=Frame(l11)
l1.config(bg="turquoise")
entre=Entry(l1)
entre.pack(side=LEFT)
# Define Buttons
bout20=Button(l1,text='Choose Directory',bg='green',font=a,command=dossier,padx=5,pady=5)
butimage21=PhotoImage(file='bouton/enregistrer.png')
bout21=Button(l11,command=lambda:save(img))
bout21.config(bg='turquoise',image=butimage21)
bout21.pack(side=BOTTOM)
bout20.pack(side=RIGHT)
l1.pack(padx=10,side=TOP)
l5=Frame(l2,borderwidth=0)
l5.config(bg="turquoise")
bout22=Button(l5,text='Exit',font=a,bg='red',command=alertex,padx=5,pady=5)
bout22.pack()
l5.pack(side=RIGHT)
l11.pack(side=LEFT)
l2.pack(fill='both',expand='yes',pady=5)

f.mainloop()
