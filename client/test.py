#!/usr/bin/env python
#Run as follows: python3 test.py

import tkinter as tk
import sys
import random
import os

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")


        self.L1 = tk.Label(root, text="User Name")
        self.L1.pack( side ="left")
        self.E1 = tk.Entry(bd =5)
        self.E1.pack(side ="right")

	self.b1 = Button(root, text='Show', command=(lambda e=ents: fetch(e)))
	self.b1.pack(side="left", padx=5, pady=5)

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

    def fetch(entries):
        for entry in entries:
          field = entry[0]
          text  = entry[1].get()
          print('%s: "%s"' % (field, text)) 

root = tk.Tk()
ents = makeform(root, fields)
root.title('Supreeth Raspberry Pi Buggy')
app = Application(master=root)

app.mainloop()
