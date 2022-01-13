#imports
import tkinter as tk
from tkinter import ttk
from ctypes import windll
import requests as req


#fix blurriness on windows
windll.shcore.SetProcessDpiAwareness(1)

#window setup
root = tk.Tk()
root.title("BrawlStats")
root.geometry("1600x900+500+400")

detailsFrame = ttk.Frame(root, height=700)
detailsFrame.pack()

message = ttk.Label(root, text="Enter Brawlhalla ID:")
message.pack()

textbox = ttk.Entry()
textbox.pack(pady=(15, 25))

button = ttk.Button(root, text="Search")
button.pack()

root.mainloop()