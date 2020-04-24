from tkinter import *

class Application:
    def __init__(self, master=None):
        self.table = Frame(master)
        self.table.pack()
        size = 15
        # pixelVirtual = PhotoImage(width=1, height=1)
        # self.title = Label(self.table, text="Jogo da velha", font=("robot", "20"))
        # self.title.pack()

        self.button00 = Button(self.table, text="00", width=size*2, height=size)
        self.button00.grid(row=0, column=0)
        self.button00.bind("<Button-1>", self.selected)
        self.button01 = Button(self.table, text="01", width=size*2, height=size)
        self.button01.grid(row=0, column=1)
        self.button01.bind("<Button-1>", self.selected)
        self.button02 = Button(self.table, text="02", width=size*2, height=size)
        self.button02.grid(row=0, column=2)
        self.button02.bind("<Button-1>", self.selected)

        self.button10 = Button(self.table, text="10", width=size*2, height=size)
        self.button10.grid(row=1, column=0)
        self.button10.bind("<Button-1>", self.selected)
        self.button11 = Button(self.table, text="11", width=size*2, height=size)
        self.button11.grid(row=1, column=1)
        self.button11.bind("<Button-1>", self.selected)
        self.button12 = Button(self.table, text="12", width=size*2, height=size)
        self.button12.grid(row=1, column=2)
        self.button12.bind("<Button-1>", self.selected)

        self.button20 = Button(self.table, text="20", width=size*2, height=size)
        self.button20.grid(row=2, column=0)
        self.button20.bind("<Button-1>", self.selected)
        self.button21 = Button(self.table, text="21", width=size*2, height=size)
        self.button21.grid(row=2, column=1)
        self.button21.bind("<Button-1>", self.selected)
        self.button22 = Button(self.table, text="22", width=size*2, height=size)
        self.button22.grid(row=2, column=2)
        self.button22.bind("<Button-1>", self.selected)
        
    def selected(self, event):
        if event.widget['bg'] == "green":
            event.widget['bg'] = "gray"
        else:
            event.widget['bg'] = "green"

        # self.button00.pack()
        # self.button01.pack()
        # self.button02.pack()

root = Tk()
# root.geometry("200x200")
Application(root)
root.mainloop()