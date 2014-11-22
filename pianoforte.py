from Tkinter import *

class Application(Frame):
    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit

        self.QUIT.pack({"side": "left"})
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
myapp = Application(master=root)
myapp.master.title("Pianoforte")
myapp.master.maxsize(1000, 400)
myapp.mainloop()
root.destroy()
