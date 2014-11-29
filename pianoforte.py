from Tkinter import *

bgcolor = "#FFFFFF"
root = Tk()
root.config(bg=bgcolor)
root.title("Pianoforte")
root.geometry("800x500")
root.iconbitmap('icons.ico')

#IMAGE CHANGING
#FUNTION1 FOR CHANGING IMAGE _ MAJOR
def printphoto_C():
    img = PhotoImage(file="C.gif")
    mlabel.config(image=img)
    mlabel.image = img
    text = "C MAJOR"
    labeltext.config(text=text)
def printphoto_Db():
    img = PhotoImage(file="Db.gif")
    mlabel.config(image=img)
    mlabel.image = img
    text = "Db MAJOR"
    labeltext.config(text=text)
def printphoto_D():
    img = PhotoImage(file="D.gif")
    mlabel.config(image=img)
    mlabel.image = img
    text = "D MAJOR"
    labeltext.config(text=text)
def printphoto_Eb():
    img = PhotoImage(file="Eb.gif")
    mlabel.config(image=img)
    mlabel.image = img
    text = "Eb MAJOR"
    labeltext.config(text=text)
def printphoto_E():
    img = PhotoImage(file="E.gif")
    mlabel.config(image=img)
    mlabel.image = img
    text = "E MAJOR"
    labeltext.config(text=text)
def printphoto_F():
    img = PhotoImage(file="F.gif")
    mlabel.config(image=img)
    mlabel.image = img
    text = "F MAJOR"
    labeltext.config(text=text)
def printphoto_FL():
    img = PhotoImage(file="FL.gif")
    mlabel.config(image=img)
    mlabel.image = img
    text = "F# MAJOR"
    labeltext.config(text=text)
def printphoto_Gb():
    img = PhotoImage(file="Gb.gif")
    mlabel.config(image=img)
    mlabel.image = img
    text = "Gb MAJOR"
    labeltext.config(text=text)
def printphoto_G():
    img = PhotoImage(file="G.gif")
    mlabel.config(image=img)
    mlabel.image = img
    text = "G MAJOR"
    labeltext.config(text=text)
def printphoto_Ab():
    img = PhotoImage(file="Ab.gif")
    mlabel.config(image=img)
    mlabel.image = img
    text = "Ab MAJOR"
    labeltext.config(text=text)
def printphoto_A():
    img = PhotoImage(file="A.gif")
    mlabel.config(image=img)
    mlabel.image = img
    text = "A MAJOR"
    labeltext.config(text=text)
def printphoto_Bb():
    img = PhotoImage(file="Bb.gif")
    mlabel.config(image=img)
    mlabel.image = img
    text = "Bb MAJOR"
    labeltext.config(text=text)
def printphoto_B():
    img = PhotoImage(file="B.gif")
    mlabel.config(image=img)
    mlabel.image = img
    text = "B MAJOR"
    labeltext.config(text=text)

#FUNTION2 FOR CHANGING IMAGE _ MINOR

def printphoto_Cm():
    img = PhotoImage(file="Cm.gif")
    mlabel.config(image=img)
    mlabel.image = img
    text = "Cm MINOR"
    labeltext.config(text=text)
def printphoto_CLm():
    img = PhotoImage(file="CLm.gif")
    mlabel.config(image=img)
    mlabel.image = img
    text = "C#m MINOR"
    labeltext.config(text=text)
def printphoto_Dm():
    img = PhotoImage(file="Dm.gif")
    mlabel.config(image=img)
    mlabel.image = img
    text = "Dm MINOR"
    labeltext.config(text=text)
def printphoto_Ebm():
    img = PhotoImage(file="Ebm.gif")
    mlabel.config(image=img)
    mlabel.image = img
    text = "Ebm MINOR"
    labeltext.config(text=text)
def printphoto_DLm():
    img = PhotoImage(file="DLm.gif")
    mlabel.config(image=img)
    mlabel.image = img
    text = "D#m MINOR"
    labeltext.config(text=text)
def printphoto_Em():
    img = PhotoImage(file="Em.gif")
    mlabel.config(image=img)
    mlabel.image = img
    text = "Em MINOR"
    labeltext.config(text=text)
def printphoto_Fm():
    img = PhotoImage(file="Fm.gif")
    mlabel.config(image=img)
    mlabel.image = img
    text = "Fm MINOR"
    labeltext.config(text=text)
def printphoto_FLm():
    img = PhotoImage(file="FLm.gif")
    mlabel.config(image=img)
    mlabel.image = img
    text = "F#m MINOR"
    labeltext.config(text=text)
def printphoto_Gm():
    img = PhotoImage(file="Gm.gif")
    mlabel.config(image=img)
    mlabel.image = img
    text = "Gm MINOR"
    labeltext.config(text=text)
def printphoto_GLm():
    img = PhotoImage(file="GLm.gif")
    mlabel.config(image=img)
    mlabel.image = img
    text = "G#m MINOR"
    labeltext.config(text=text)
def printphoto_Am():
    img = PhotoImage(file="Am.gif")
    mlabel.config(image=img)
    mlabel.image = img
    text = "AM MINOR"
    labeltext.config(text=text)
def printphoto_Bbm():
    img = PhotoImage(file="Bbm.gif")
    mlabel.config(image=img)
    mlabel.image = img
    text = "Bbm MINOR"
    labeltext.config(text=text)
def printphoto_Bm():
    img = PhotoImage(file="Bm.gif")
    mlabel.config(image=img)
    mlabel.image = img
    text = "Bm MINOR"
    labeltext.config(text=text)

#FUNTION3 FOR CHANGING IMAGE _ Dominant_7th

def printphoto_C7():
    img = PhotoImage(file="C7.gif")
    mlabel.config(image=img)
    mlabel.image = img
    text = "C7 Dominant 7th"
    labeltext.config(text=text)
def printphoto_Cb7():
    img = PhotoImage(file="Cb7.gif")
    mlabel.config(image=img)
    mlabel.image = img
    text = "Cb7 Dominant 7th"
    labeltext.config(text=text)
def printphoto_Db7():
    img = PhotoImage(file="Db7.gif")
    mlabel.config(image=img)
    mlabel.image = img
    text = "Db7 Dominant 7th"
    labeltext.config(text=text)
def printphoto_D7():
    img = PhotoImage(file="D7.gif")
    mlabel.config(image=img)
    mlabel.image = img
    text = "D7 Dominant 7th"
    labeltext.config(text=text)
def printphoto_Eb7():
    img = PhotoImage(file="Eb7.gif")
    mlabel.config(image=img)
    mlabel.image = img
    text = "Eb7 Dominant 7th"
    labeltext.config(text=text)
def printphoto_E7():
    img = PhotoImage(file="E7.gif")
    mlabel.config(image=img)
    mlabel.image = img
    text = "E7 Dominant 7th"
    labeltext.config(text=text)
def printphoto_F7():
    img = PhotoImage(file="F7.gif")
    mlabel.config(image=img)
    mlabel.image = img
    text = "F7 Dominant 7th"
    labeltext.config(text=text)
def printphoto_G7():
    img = PhotoImage(file="G7.gif")
    mlabel.config(image=img)
    mlabel.image = img
    text = "G7 Dominant 7th"
    labeltext.config(text=text)
def printphoto_FL7():
    img = PhotoImage(file="FL7.gif")
    mlabel.config(image=img)
    mlabel.image = img
    text = "F#7 Dominant 7th"
    labeltext.config(text=text)
def printphoto_Ab7():
    img = PhotoImage(file="Ab7.gif")
    mlabel.config(image=img)
    mlabel.image = img
    text = "Ab7 Dominant 7th"
    labeltext.config(text=text)
def printphoto_A7():
    img = PhotoImage(file="A7.gif")
    mlabel.config(image=img)
    mlabel.image = img
    text = "A7 Dominant 7th"
    labeltext.config(text=text)
def printphoto_Bb7():
    img = PhotoImage(file="Bb7.gif")
    mlabel.config(image=img)
    mlabel.image = img
    text = "Bb7 Dominant 7th"
    labeltext.config(text=text)
def printphoto_B7():
    img = PhotoImage(file="B7.gif")
    mlabel.config(image=img)
    mlabel.image = img
    text = "B7 Dominant 7th"
    labeltext.config(text=text)

#FUNTION4 FOR CHANGING IMAGE _  Major_7th_Chords

def printphoto_Cmaj7():
    img = PhotoImage(file="Cmaj7.gif")
    mlabel.config(image=img)
    mlabel.image = img
    text = "Cmaj7 Major 7th Chords"
    labeltext.config(text=text)
def printphoto_Dbmaj7():
    img = PhotoImage(file="Dbmaj7.gif")
    mlabel.config(image=img)
    mlabel.image = img
    text = "Dbmaj7 Major 7th Chords"
    labeltext.config(text=text)
def printphoto_Dmaj7():
    img = PhotoImage(file="Dmaj7.gif")
    mlabel.config(image=img)
    mlabel.image = img
    text = " Major 7th Chords"
    labeltext.config(text=text)
def printphoto_Ebmaj7():
    img = PhotoImage(file="Ebmaj7.gif")
    mlabel.config(image=img)
    mlabel.image = img
    text = "Ebmaj7 Major 7th Chords"
    labeltext.config(text=text)
def printphoto_Emaj7():
    img = PhotoImage(file="Emaj7.gif")
    mlabel.config(image=img)
    mlabel.image = img
    text = "Emaj7 Major 7th Chords"
    labeltext.config(text=text)
def printphoto_Fmaj7():
    img = PhotoImage(file="Fmaj7.gif")
    mlabel.config(image=img)
    mlabel.image = img
    text = "Fmaj7 Major 7th Chords"
    labeltext.config(text=text)
def printphoto_FLmaj7():
    img = PhotoImage(file="FLmaj7.gif")
    mlabel.config(image=img)
    mlabel.image = img
    text = "F#maj7 Major 7th Chords"
    labeltext.config(text=text)
def printphoto_Gmaj7():
    img = PhotoImage(file="Gmaj7.gif")
    mlabel.config(image=img)
    mlabel.image = img
    text = "Gmaj7 Major 7th Chords"
    labeltext.config(text=text)
def printphoto_Abmaj7():
    img = PhotoImage(file="Abmaj7.gif")
    mlabel.config(image=img)
    mlabel.image = img
    text = "Abmaj7 Major 7th Chords"
    labeltext.config(text=text)
def printphoto_Amaj7():
    img = PhotoImage(file="Amaj7.gif")
    mlabel.config(image=img)
    mlabel.image = img
    text = "Amaj7 Major 7th Chords"
    labeltext.config(text=text)
def printphoto_Bbmaj7():
    img = PhotoImage(file="Bbmaj7.gif")
    mlabel.config(image=img)
    mlabel.image = img
    text = "Bbmaj7 Major 7th Chords"
    labeltext.config(text=text)
def printphoto_Bmaj7():
    img = PhotoImage(file="Bmaj7.gif")
    mlabel.config(image=img)
    mlabel.image = img
    text = "Bmaj7 Major 7th Chords"
    labeltext.config(text=text)
    
#START_IMAGE
labeltext = Label(root, text="PIANO CHORDS", bg=bgcolor)
labeltext.pack(pady=10)
img = PhotoImage(file="piano.gif")
mlabel = Label( root, image=img)
mlabel.pack()



#BUTTON
#FRAME01
frame = Frame(root, bg=bgcolor)
frame.pack(fill=X, pady=10)
#MAJORCHORDNAME
var = StringVar()
label = Label( frame, textvariable=var, bg=bgcolor)
var.set(" Major Chords")
label.pack(side=LEFT)
#MAJORCHORD
chord_c = Button(frame, text="C", fg="Firebrick1", command = printphoto_C)
chord_c.pack(side=LEFT, ipadx=4)

chord_Db = Button(frame, text="Db", fg="Firebrick1", command = printphoto_Db)
chord_Db.pack(side=LEFT, ipadx=4)

chord_D = Button(frame, text="D", fg="Firebrick1", command = printphoto_D)
chord_D.pack(side=LEFT, ipadx=4)

chord_Eb = Button(frame, text="Eb", fg="Firebrick1", command = printphoto_Eb)
chord_Eb.pack(side=LEFT, ipadx=4)

chord_E = Button(frame, text="E", fg="Firebrick1", command = printphoto_E)
chord_E.pack(side=LEFT, ipadx=4)

chord_F = Button(frame, text="F", fg="Firebrick1", command = printphoto_F)
chord_F.pack(side=LEFT, ipadx=4)

chord_FL = Button(frame, text="F#", fg="Firebrick1", command = printphoto_FL)
chord_FL.pack(side=LEFT, ipadx=4)

chord_Gb = Button(frame, text="Gb", fg="Firebrick1", command = printphoto_Gb)
chord_Gb.pack(side=LEFT, ipadx=4)

chord_G = Button(frame, text="G", fg="Firebrick1", command = printphoto_G)
chord_G.pack(side=LEFT, ipadx=4)

chord_Ab = Button(frame, text="Ab", fg="Firebrick1", command = printphoto_Ab)
chord_Ab.pack(side=LEFT, ipadx=4)

chord_A = Button(frame, text="A", fg="Firebrick1", command = printphoto_A)
chord_A.pack(side=LEFT, ipadx=4)

chord_Bb = Button(frame, text="Bb", fg="Firebrick1", command = printphoto_Bb)
chord_Bb.pack(side=LEFT, ipadx=4)


chord_B = Button(frame, text="B", fg="Firebrick1", command = printphoto_B)
chord_B.pack(side=LEFT, ipadx=4)


#FRAME02
frame = Frame(root, bg=bgcolor)
frame.pack(fill=X, pady=10)
#MAJORCHORDNAME
var = StringVar()
label = Label( frame, textvariable=var, bg=bgcolor)
var.set("Minor Chords")
label.pack(side=LEFT, ipadx=4)
#MAJORCHORD
chord_Cm = Button(frame, text="Cm", fg="SeaGreen", command = printphoto_Cm)
chord_Cm.pack(side=LEFT, ipadx=4)

chord_CLm = Button(frame, text="C#m", fg="SeaGreen", command = printphoto_CLm)
chord_CLm.pack(side=LEFT, ipadx=4)

chord_Dm = Button(frame, text="Dm", fg="SeaGreen", command = printphoto_Dm)
chord_Dm.pack(side=LEFT, ipadx=4)

chord_Ebm = Button(frame, text="Ebm", fg="SeaGreen", command = printphoto_Ebm)
chord_Ebm.pack(side=LEFT, ipadx=4)

chord_DLm = Button(frame, text="D#m", fg="SeaGreen", command = printphoto_DLm)
chord_DLm.pack(side=LEFT, ipadx=4)

chord_Em = Button(frame, text="Em", fg="SeaGreen", command = printphoto_Em)
chord_Em.pack(side=LEFT, ipadx=4)

chord_Fm = Button(frame, text="Fm", fg="SeaGreen", command = printphoto_Fm)
chord_Fm.pack(side=LEFT, ipadx=4)

chord_FLm = Button(frame, text="F#m", fg="SeaGreen", command = printphoto_FLm)
chord_FLm.pack(side=LEFT, ipadx=4)

chord_Gm = Button(frame, text="Gm", fg="SeaGreen", command = printphoto_Gm)
chord_Gm.pack(side=LEFT, ipadx=4)

chord_GLm = Button(frame, text="G#m", fg="SeaGreen", command = printphoto_GLm)
chord_GLm.pack(side=LEFT, ipadx=4)

chord_Am = Button(frame, text="Am", fg="SeaGreen", command = printphoto_Am)
chord_Am.pack(side=LEFT, ipadx=4)

chord_Bbm = Button(frame, text="Bbm", fg="SeaGreen", command = printphoto_Bbm)
chord_Bbm.pack(side=LEFT, ipadx=4)

chord_Bm = Button(frame, text="Bm", fg="SeaGreen", command = printphoto_Bm)
chord_Bm.pack(side=LEFT, ipadx=4)

#FRAME03
frame = Frame(root, bg=bgcolor)
frame.pack(fill=X, pady=10)
#MAJORCHORDNAME
var = StringVar()
label = Label( frame, textvariable=var, bg=bgcolor)
var.set("Dominant 7th Chords")
label.pack(side=LEFT, ipadx=4)
#Dominant_7th_Chords
chord_C7 = Button(frame, text="C7", fg="Blue", command = printphoto_C7)
chord_C7.pack(side=LEFT, ipadx=4)

chord_Db7 = Button(frame, text="Db7", fg="Blue", command = printphoto_Db7)
chord_Db7.pack(side=LEFT, ipadx=4)

chord_D7 = Button(frame, text="D7", fg="Blue", command = printphoto_D7)
chord_D7.pack(side=LEFT, ipadx=4)

chord_Eb7 = Button(frame, text="Eb7", fg="Blue", command = printphoto_Eb7)
chord_Eb7.pack(side=LEFT, ipadx=4)

chord_E7 = Button(frame, text="E7", fg="Blue", command = printphoto_E7)
chord_E7.pack(side=LEFT, ipadx=4)

chord_F7 = Button(frame, text="F7", fg="Blue", command = printphoto_F7)
chord_F7.pack(side=LEFT, ipadx=4)

chord_FL7 = Button(frame, text="F#7", fg="Blue", command = printphoto_FL7)
chord_FL7.pack(side=LEFT, ipadx=4)

chord_G7 = Button(frame, text="G7", fg="Blue", command = printphoto_G7)
chord_G7.pack(side=LEFT, ipadx=4)

chord_Ab7 = Button(frame, text="Ab7", fg="Blue", command = printphoto_Ab7)
chord_Ab7.pack(side=LEFT, ipadx=4)

chord_A7 = Button(frame, text="A7", fg="Blue", command = printphoto_A7)
chord_A7.pack(side=LEFT, ipadx=4)

chord_Bb7 = Button(frame, text="Bb7", fg="Blue", command = printphoto_Bb7)
chord_Bb7.pack(side=LEFT, ipadx=4)

chord_B7 = Button(frame, text="B7", fg="Blue", command = printphoto_B7)
chord_B7.pack(side=LEFT, ipadx=4)

#FRAME04
frame = Frame(root, bg=bgcolor)
frame.pack(fill=X, pady=10)
#MAJOR7CHORDNAME
var = StringVar()
label = Label( frame, textvariable=var, bg=bgcolor)
var.set("Major 7th Chords")
label.pack(side=LEFT, ipadx=4)
#Major_7th_Chords
chord_Cmaj7 = Button(frame, text="Cmaj7", fg="SteelBlue4", command = printphoto_Cmaj7)
chord_Cmaj7.pack(side=LEFT, ipadx=4)

chord_Dbmaj7 = Button(frame, text="Dbmaj7", fg="SteelBlue4", command = printphoto_Dbmaj7)
chord_Dbmaj7.pack(side=LEFT, ipadx=4)

chord_Dmaj7 = Button(frame, text="Dmaj7", fg="SteelBlue4", command = printphoto_Dmaj7)
chord_Dmaj7.pack(side=LEFT, ipadx=4)

chord_Ebmaj7 = Button(frame, text="Ebmaj7", fg="SteelBlue4", command = printphoto_Ebmaj7)
chord_Ebmaj7.pack(side=LEFT, ipadx=4)

chord_Emaj7 = Button(frame, text="Emaj7", fg="SteelBlue4", command = printphoto_Emaj7)
chord_Emaj7.pack(side=LEFT, ipadx=4)

chord_Fmaj7 = Button(frame, text="Fmaj7", fg="SteelBlue4", command = printphoto_Fmaj7)
chord_Fmaj7.pack(side=LEFT, ipadx=4)

chord_FLmaj7 = Button(frame, text="F#maj7", fg="SteelBlue4", command = printphoto_FLmaj7)
chord_FLmaj7.pack(side=LEFT, ipadx=4)

chord_Gmaj7 = Button(frame, text="Gmaj7", fg="SteelBlue4", command = printphoto_Gmaj7)
chord_Gmaj7.pack(side=LEFT, ipadx=4)

chord_Abmaj7 = Button(frame, text="Abmaj7", fg="SteelBlue4", command = printphoto_Abmaj7)
chord_Abmaj7.pack(side=LEFT, ipadx=4)

chord_Amaj7 = Button(frame, text="Amaj7", fg="SteelBlue4", command = printphoto_Amaj7)
chord_Amaj7.pack(side=LEFT, ipadx=4)

chord_Bbmaj7 = Button(frame, text="Bbmaj7", fg="SteelBlue4", command = printphoto_Bbmaj7)
chord_Bbmaj7.pack(side=LEFT, ipadx=4)


chord_Bmaj7 = Button(frame, text="Bmaj7", fg="SteelBlue4", command = printphoto_Bmaj7)
chord_Bmaj7.pack(side=LEFT, ipadx=4)


root.mainloop()
