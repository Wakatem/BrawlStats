#imports
import tkinter as tk
from matplotlib.pyplot import fill
import requests as req
import detailsSection as ds
from turtle import width
from tkinter import ttk
from ctypes import windll
from PIL import Image, ImageTk
from io import BytesIO

"""================================="""


def getInput(textbox):
    return textbox.get()


#simple networking
def searchPlayer(textbox):
    playerID = getInput(textbox)
    getRequest = "http://brawlhallastats.herokuapp.com/api/submit-form3-by-id?player=" + playerID
    response = req.get(getRequest)
    
    #clear textbox
    textbox.delete(0, 8)


"""================================="""



#fix blurriness on windows
windll.shcore.SetProcessDpiAwareness(1)

#window setup
root = tk.Tk()
root.title("BrawlStats")
root.geometry("1600x940+500+400")
root.resizable(width=False, height=False)

#TODO setup details section here
detailsSection = ds.DetailsSection(root)
detailsSection.displayLegend("ada")


centerFrame = ttk.Frame(root)
centerFrame.pack()

message = ttk.Label(centerFrame, text="Enter Brawlhalla ID:")
message.pack()

textbox = ttk.Entry(centerFrame)
textbox.focus()
textbox.pack(pady=(10, 25))

button = ttk.Button(centerFrame, text="Search")
button.bind('<Button>', lambda event: searchPlayer(textbox))
button.pack()


root.mainloop()