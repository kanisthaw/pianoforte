from Tkinter import *

bgcolor = "#6C7A89"

root = Tk()
root.config(bg=bgcolor)
root.title("Pianoforte")
root.geometry("800x500")


#FUNTION FOR CHANGING IMAGE _ MAJOR
def printphoto_C():
    img = PhotoImage(file="C.gif")
    mlabel.config(image=img)
    mlabel.image = img


def printphoto_Db():
    img = PhotoImage(file="Db.gif")
    mlabel.config(image=img)
    mlabel.image = img

def printphoto_D():
    img = PhotoImage(file="D.gif")
    mlabel.config(image=img)
    mlabel.image = img

def printphoto_Eb():
    img = PhotoImage(file="Eb.gif")
    mlabel.config(image=img)
    mlabel.image = img


def printphoto_E():
    img = PhotoImage(file="E.gif")
    mlabel.config(image=img)
    mlabel.image = img

def printphoto_F():
    img = PhotoImage(file="F.gif")
    mlabel.config(image=img)
    mlabel.image = img

def printphoto_FL():
    img = PhotoImage(file="FL.gif")
    mlabel.config(image=img)
    mlabel.image = img

def printphoto_Gb():
    img = PhotoImage(file="Gb.gif")
    mlabel.config(image=img)
    mlabel.image = img

def printphoto_G():
    img = PhotoImage(file="G.gif")
    mlabel.config(image=img)
    mlabel.image = img

def printphoto_Ab():
    img = PhotoImage(file="Ab.gif")
    mlabel.config(image=img)
    mlabel.image = img

def printphoto_A():
    img = PhotoImage(file="A.gif")
    mlabel.config(image=img)
    mlabel.image = img

def printphoto_Bb():
    img = PhotoImage(file="Bb.gif")
    mlabel.config(image=img)
    mlabel.image = img

def printphoto_B():
    img = PhotoImage(file="B.gif")
    mlabel.config(image=img)
    mlabel.image = img

#FUNTION FOR CHANGING IMAGE _ MINOR

def printphoto_Cm():
    img = PhotoImage(file="Cm.gif")
    mlabel.config(image=img)
    mlabel.image = img
def printphoto_CLm():
    img = PhotoImage(file="CLm.gif")
    mlabel.config(image=img)
    mlabel.image = img
def printphoto_Dm():
    img = PhotoImage(file="Dm.gif")
    mlabel.config(image=img)
    mlabel.image = img
def printphoto_Ebm():
    img = PhotoImage(file="Ebm.gif")
    mlabel.config(image=img)
    mlabel.image = img
def printphoto_DLm():
    img = PhotoImage(file="DLm.gif")
    mlabel.config(image=img)
    mlabel.image = img
def printphoto_Em():
    img = PhotoImage(file="Em.gif")
    mlabel.config(image=img)
    mlabel.image = img
def printphoto_Fm():
    img = PhotoImage(file="Fm.gif")
    mlabel.config(image=img)
    mlabel.image = img
def printphoto_FLm():
    img = PhotoImage(file="FLm.gif")
    mlabel.config(image=img)
    mlabel.image = img
def printphoto_Gm():
    img = PhotoImage(file="Gm.gif")
    mlabel.config(image=img)
    mlabel.image = img
def printphoto_GLm():
    img = PhotoImage(file="GLm.gif")
    mlabel.config(image=img)
    mlabel.image = img
def printphoto_Am():
    img = PhotoImage(file="Am.gif")
    mlabel.config(image=img)
    mlabel.image = img
def printphoto_Bbm():
    img = PhotoImage(file="Bbm.gif")
    mlabel.config(image=img)
    mlabel.image = img
def printphoto_Bm():
    img = PhotoImage(file="Bm.gif")
    mlabel.config(image=img)
    mlabel.image = img
    
#START_IMAGE    
img = PhotoImage(file="C.gif")
mlabel = Label( root, image=img)
mlabel.pack()
#FRAME01
frame = Frame(root, bg=bgcolor)
frame.pack(fill=X, pady=10)
#MAJORCHORDNAME
var = StringVar()
label = Label( frame, textvariable=var, bg=bgcolor)
var.set(" Major Chords")
label.pack(side=LEFT)
#MAJORCHORD
cord_c = Button(frame, text="C", fg="red", command = printphoto_C)
cord_c.pack(side=LEFT, ipadx=4)

cord_Db = Button(frame, text="Db", fg="red", command = printphoto_Db)
cord_Db.pack(side=LEFT, ipadx=4)

cord_D = Button(frame, text="D", fg="red", command = printphoto_D)
cord_D.pack(side=LEFT, ipadx=4)

cord_Eb = Button(frame, text="Eb", fg="red", command = printphoto_Eb)
cord_Eb.pack(side=LEFT, ipadx=4)

cord_E = Button(frame, text="E", fg="red", command = printphoto_E)
cord_E.pack(side=LEFT, ipadx=4)

cord_F = Button(frame, text="F", fg="red", command = printphoto_F)
cord_F.pack(side=LEFT, ipadx=4)

cord_FL = Button(frame, text="F#", fg="red", command = printphoto_FL)
cord_FL.pack(side=LEFT, ipadx=4)

cord_Gb = Button(frame, text="Gb", fg="red", command = printphoto_Gb)
cord_Gb.pack(side=LEFT, ipadx=4)

cord_G = Button(frame, text="G", fg="red", command = printphoto_G)
cord_G.pack(side=LEFT, ipadx=4)

cord_Ab = Button(frame, text="Ab", fg="red", command = printphoto_Ab)
cord_Ab.pack(side=LEFT, ipadx=4)

cord_A = Button(frame, text="A", fg="red", command = printphoto_A)
cord_A.pack(side=LEFT, ipadx=4)

cord_Bb = Button(frame, text="Bb", fg="red", command = printphoto_Bb)
cord_Bb.pack(side=LEFT, ipadx=4)

cord_B = Button(frame, text="B", fg="red", command = printphoto_B)
cord_B.pack(side=LEFT, ipadx=4)


#FRAME02
frame = Frame(root, bg=bgcolor)
frame.pack(fill=X)
#MAJORCHORDNAME
var = StringVar()
label = Label( frame, textvariable=var, bg=bgcolor)
var.set("Minor Chords")
label.pack(side=LEFT, ipadx=4)
#MAJORCHORD
cord_Cm = Button(frame, text="Cm", fg="blue", command = printphoto_Cm)
cord_Cm.pack(side=LEFT, ipadx=4)

cord_CLm = Button(frame, text="C#m", fg="blue", command = printphoto_CLm)
cord_CLm.pack(side=LEFT, ipadx=4)

cord_Dm = Button(frame, text="Dm", fg="blue", command = printphoto_Dm)
cord_Dm.pack(side=LEFT, ipadx=4)

cord_Ebm = Button(frame, text="Ebm", fg="blue", command = printphoto_Ebm)
cord_Ebm.pack(side=LEFT, ipadx=4)

cord_DLm = Button(frame, text="D#m", fg="blue", command = printphoto_DLm)
cord_DLm.pack(side=LEFT, ipadx=4)

cord_Em = Button(frame, text="Em", fg="blue", command = printphoto_Em)
cord_Em.pack(side=LEFT, ipadx=4)

cord_Fm = Button(frame, text="Fm", fg="blue", command = printphoto_Fm)
cord_Fm.pack(side=LEFT, ipadx=4)

cord_FLm = Button(frame, text="F#m", fg="blue", command = printphoto_FLm)
cord_FLm.pack(side=LEFT, ipadx=4)

cord_Gm = Button(frame, text="Gm", fg="blue", command = printphoto_Gm)
cord_Gm.pack(side=LEFT, ipadx=4)

cord_GLm = Button(frame, text="G#m", fg="blue", command = printphoto_GLm)
cord_GLm.pack(side=LEFT, ipadx=4)

cord_Am = Button(frame, text="Am", fg="blue", command = printphoto_Am)
cord_Am.pack(side=LEFT, ipadx=4)

cord_Bbm = Button(frame, text="Bbm", fg="blue", command = printphoto_Bbm)
cord_Bbm.pack(side=LEFT, ipadx=4)

cord_Bm = Button(frame, text="Bm", fg="blue", command = printphoto_Bm)
cord_Bm.pack(side=LEFT, ipadx=4)

#FRAME03
frame = Frame(root, bg=bgcolor)
frame.pack(fill=X)
#MAJORCHORDNAME
var = StringVar()
label = Label( frame, textvariable=var, bg=bgcolor)
var.set("Dominant 7th Chords")
label.pack(side=LEFT, ipadx=4)
#MAJORCHORD
cord_Cm = Button(frame, text="C7", fg="blue", command = printphoto_Cm)
cord_Cm.pack(side=LEFT, ipadx=4)

cord_CLm = Button(frame, text="Db7", fg="blue", command = printphoto_CLm)
cord_CLm.pack(side=LEFT, ipadx=4)

cord_Dm = Button(frame, text="D7", fg="blue", command = printphoto_Dm)
cord_Dm.pack(side=LEFT, ipadx=4)

cord_Ebm = Button(frame, text="Eb7", fg="blue", command = printphoto_Ebm)
cord_Ebm.pack(side=LEFT, ipadx=4)

cord_DLm = Button(frame, text="E7", fg="blue", command = printphoto_DLm)
cord_DLm.pack(side=LEFT, ipadx=4)

cord_Em = Button(frame, text="F7", fg="blue", command = printphoto_Em)
cord_Em.pack(side=LEFT, ipadx=4)

cord_Fm = Button(frame, text="F#7", fg="blue", command = printphoto_Fm)
cord_Fm.pack(side=LEFT, ipadx=4)

cord_FLm = Button(frame, text="G7", fg="blue", command = printphoto_FLm)
cord_FLm.pack(side=LEFT, ipadx=4)

cord_Gm = Button(frame, text="Ab7", fg="blue", command = printphoto_Gm)
cord_Gm.pack(side=LEFT, ipadx=4)

cord_GLm = Button(frame, text="A7", fg="blue", command = printphoto_GLm)
cord_GLm.pack(side=LEFT, ipadx=4)

cord_Am = Button(frame, text="Bd7", fg="blue", command = printphoto_Am)
cord_Am.pack(side=LEFT, ipadx=4)

cord_Bbm = Button(frame, text="B7", fg="blue", command = printphoto_Bbm)
cord_Bbm.pack(side=LEFT, ipadx=4)

root.mainloop()
