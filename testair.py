from Tkinter import *

master = Tk()

def callback():
    print "Picture Chord C"
c = Button(master, text="C", command=callback)
c.pack()

def callback():
    print "Picture Chord D"
    
d = Button(master, text="D", command=callback)
d.pack()

def callback():
    print "Picture Chord E"
    
e = Button(master, text="E", command=callback)
e.pack()

def callback():
    print "Picture Chord F"
    
f = Button(master, text="F", command=callback)
f.pack()


def callback():
    print "Picture Chord G"
    
g = Button(master, text="G", command=callback)
g.pack()

def callback():
    print "Picture Chord A"
    
a = Button(master, text="A", command=callback)
a.pack()

def callback():
    print "Picture Chord B"
    
b = Button(master, text="B", command=callback)
b.pack()
mainloop()
