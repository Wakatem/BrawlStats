#imports
import tkinter as tk
import requests as req
import json
import detailsSection as ds
from matplotlib.pyplot import fill
from tkinter import ttk
from ctypes import windll

"""==========================================="""


def getInput(textbox):
    return textbox.get()



def parseResponse(response):
    parsedDetails = json.loads(response.content)

    playerName = parsedDetails["name"]
    playerID = parsedDetails["brawlhalla_id"]
    playerLevel = parsedDetails["level"]
    playedGames = parsedDetails["games"]
    gamesWon = parsedDetails["wins"]
    gamesLost = int(playedGames) - int (gamesWon)

    toplegend = parsedDetails["legends"][0]
    legendName = toplegend["legend_name_key"]
    legendWins = toplegend["wins"]
    legendLevel = toplegend["level"]
    legendKOs = toplegend["kos"]

    list = [playerName, playerID, playerLevel, playedGames, gamesWon, gamesLost, legendName, legendWins, legendLevel, legendKOs]
    
    #send parsed data to details section
    detailsSection.updateDetails(list)


def searchPlayer(textbox):
    playerID = getInput(textbox)
    getRequest = "http://brawlhallastats.herokuapp.com/api/submit-form3-by-id?player=" + playerID
    response = req.get(getRequest)
    
    #clear textbox
    textbox.delete(0, 8)
    parseResponse(response)
    



def setupInputSection(rootWindow):
    inputFrame = ttk.Frame(rootWindow)
    inputFrame.pack()

    message = ttk.Label(inputFrame, text="Enter Brawlhalla ID:")
    message.pack()

    textbox = ttk.Entry(inputFrame)
    textbox.focus()
    textbox.pack(pady=(10, 25))

    button = ttk.Button(inputFrame, text="Search")
    button.bind('<Button>', lambda event: searchPlayer(textbox))
    button.pack()


"""==========================================="""



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

setupInputSection(root)


root.mainloop()