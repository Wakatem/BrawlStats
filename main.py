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

root.mainloop()