import invertedindex as qt
from tkinter import *
import tkinter.messagebox

class BButtons:
    def __init__(self, master):
        frame = Frame(master)
        frame.grid()
        
        self.label = Label(frame, text="SEARCH ENGINE", font=("Arial Bold", 20), bg='blue', fg='red')
        self.label.pack()

        self.searchname = StringVar()
        self.entry = Entry(frame, textvariable=self.searchname, width=25, bg='lightblue')
        self.entry.pack()
        
        self.printButton = Button(frame, text="SEARCH", command=lambda:qt.search_word(self.searchname.get()))
        self.printButton.pack()
        
        
        self.quitButton = Button(frame, text="QUIT", command=lambda:desAndquit(self, frame))
        self.quitButton.pack()
        
        def desAndquit(self, frame):
            frame.destroy()
            window.destroy()
        

window = Tk()
window.title("IR PROJECT")
b = BButtons(window)
window.mainloop()
