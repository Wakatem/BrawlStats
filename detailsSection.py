#imports
import tkinter as tk
from matplotlib.pyplot import fill
import requests as req
from tkinter import ttk
from ctypes import windll
from PIL import Image, ImageTk
from io import BytesIO

"""================================="""


class DetailsSection:

    brawlhallaLegends ={
        "ada" : "https://static.wikia.nocookie.net/brawlhalla_gamepedia/images/f/f9/Ada.png/revision/latest/scale-to-width-down/1000?cb=20210315001847",
        "artemis" : "https://static.wikia.nocookie.net/brawlhalla_gamepedia/images/d/d2/Artemis.png/revision/latest/scale-to-width-down/1000?cb=20210315011328",
        "asuri" : "https://static.wikia.nocookie.net/brawlhalla_gamepedia/images/e/e5/Asuri.png/revision/latest/scale-to-width-down/1000?cb=20210315011122",
        "azoth" : "https://static.wikia.nocookie.net/brawlhalla_gamepedia/images/c/c7/Azoth.png/revision/latest/scale-to-width-down/1000?cb=20210315011432",
        "barraza" : "https://static.wikia.nocookie.net/brawlhalla_gamepedia/images/6/6f/Barraza.png/revision/latest/scale-to-width-down/1000?cb=20210315012052",
        "bodvar" : "https://static.wikia.nocookie.net/brawlhalla_gamepedia/images/e/e2/Bodvar.png/revision/latest/scale-to-width-down/983?cb=20210315004132",
        "brynn" : "https://static.wikia.nocookie.net/brawlhalla_gamepedia/images/3/35/Brynn.png/revision/latest/scale-to-width-down/495?cb=20210315012141",
        "caspian" : "https://static.wikia.nocookie.net/brawlhalla_gamepedia/images/3/34/Caspian.png/revision/latest/scale-to-width-down/847?cb=20210315012337",
        "cassidy" : "https://static.wikia.nocookie.net/brawlhalla_gamepedia/images/a/a2/Cassidy.png/revision/latest/scale-to-width-down/1000?cb=20210315012750",
        "cross" : "https://static.wikia.nocookie.net/brawlhalla_gamepedia/images/4/4e/Cross.png/revision/latest/scale-to-width-down/982?cb=20210315012858",
        "diana" : "https://static.wikia.nocookie.net/brawlhalla_gamepedia/images/5/5f/Diana.png/revision/latest/scale-to-width-down/925?cb=20210315013123",
        "dusk" : "https://static.wikia.nocookie.net/brawlhalla_gamepedia/images/5/5d/Dusk.png/revision/latest/scale-to-width-down/1000?cb=20210315013217",
        "ember" : "https://static.wikia.nocookie.net/brawlhalla_gamepedia/images/3/38/Ember.png/revision/latest/scale-to-width-down/1000?cb=20210315013318",
        "fait" : "https://static.wikia.nocookie.net/brawlhalla_gamepedia/images/6/67/Fait.png/revision/latest/scale-to-width-down/870?cb=20210315013440",
        "gnash" : "https://static.wikia.nocookie.net/brawlhalla_gamepedia/images/7/7f/Gnash.png/revision/latest/scale-to-width-down/866?cb=20200718215657",
        "hattori" : "https://static.wikia.nocookie.net/brawlhalla_gamepedia/images/3/34/Hattori.png/revision/latest/scale-to-width-down/518?cb=20160805042438",
        "isaiah" : "https://static.wikia.nocookie.net/brawlhalla_gamepedia/images/e/ed/Isaiah.png/revision/latest/scale-to-width-down/801?cb=20210315014305",
        "jaeyun" : "https://static.wikia.nocookie.net/brawlhalla_gamepedia/images/2/25/Jaeyun.png/revision/latest/scale-to-width-down/1000?cb=20200708151716",
        "jhala" : "https://static.wikia.nocookie.net/brawlhalla_gamepedia/images/9/9a/Jhala.png/revision/latest/scale-to-width-down/914?cb=20210315014544",
        "jiro" : "https://static.wikia.nocookie.net/brawlhalla_gamepedia/images/5/5a/Jiro.png/revision/latest/scale-to-width-down/708?cb=20210315014715",
        "kaya" : "https://static.wikia.nocookie.net/brawlhalla_gamepedia/images/9/97/Kaya.png/revision/latest/scale-to-width-down/1000?cb=20210315014806",
        "koji" : "https://static.wikia.nocookie.net/brawlhalla_gamepedia/images/f/f2/Koji.png/revision/latest/scale-to-width-down/1000?cb=20210315014849",
        "kor" : "https://static.wikia.nocookie.net/brawlhalla_gamepedia/images/9/96/Kor.png/revision/latest/scale-to-width-down/960?cb=20210315015002",
        "lin fei" : "https://static.wikia.nocookie.net/brawlhalla_gamepedia/images/8/81/Lin_Fei.png/revision/latest/scale-to-width-down/796?cb=20210315015026",
        "lord vraxx" : "https://static.wikia.nocookie.net/brawlhalla_gamepedia/images/6/66/Lord_Vraxx.png/revision/latest/scale-to-width-down/836?cb=20210315020553",
        "lucien" : "https://static.wikia.nocookie.net/brawlhalla_gamepedia/images/1/1e/Lucien.png/revision/latest/scale-to-width-down/710?cb=20200718215734",
        "magyar" : "https://static.wikia.nocookie.net/brawlhalla_gamepedia/images/2/2e/Magyar.png/revision/latest/scale-to-width-down/1000?cb=20210114234550",
        "mako" : "https://static.wikia.nocookie.net/brawlhalla_gamepedia/images/a/a6/Mako.png/revision/latest/scale-to-width-down/1000?cb=20201001180242",
        "mirage" : "https://static.wikia.nocookie.net/brawlhalla_gamepedia/images/f/fb/Mirage.png/revision/latest/scale-to-width-down/1000?cb=20210315015153",
        "mordex" : "https://static.wikia.nocookie.net/brawlhalla_gamepedia/images/2/2d/Mordex.png/revision/latest/scale-to-width-down/941?cb=20180620204144",
        "nix" : "https://static.wikia.nocookie.net/brawlhalla_gamepedia/images/0/0f/Nix.png/revision/latest/scale-to-width-down/806?cb=20210315015436",
        "onyx" : "https://static.wikia.nocookie.net/brawlhalla_gamepedia/images/f/fb/Onyx.png/revision/latest/scale-to-width-down/1000?cb=20200317013921",
        "orion" : "https://static.wikia.nocookie.net/brawlhalla_gamepedia/images/0/0e/Orion.png/revision/latest/scale-to-width-down/463?cb=20200718215604",
        "petra" : "https://static.wikia.nocookie.net/brawlhalla_gamepedia/images/9/93/Petra.png/revision/latest/scale-to-width-down/868?cb=20210315015619",
        "queen nai" : "https://static.wikia.nocookie.net/brawlhalla_gamepedia/images/e/ea/Queen_Nai.png/revision/latest/scale-to-width-down/1000?cb=20210315015342",
        "ragnir" : "https://static.wikia.nocookie.net/brawlhalla_gamepedia/images/1/18/Ragnir.png/revision/latest/scale-to-width-down/985?cb=20210315015702",
        "rayman" : "https://static.wikia.nocookie.net/brawlhalla_gamepedia/images/c/c1/Rayman.png/revision/latest/scale-to-width-down/1000?cb=20210315015753",
        "reno" : "https://static.wikia.nocookie.net/brawlhalla_gamepedia/images/5/54/Reno.png/revision/latest/scale-to-width-down/998?cb=20210415015218",
        "scarlet" : "https://static.wikia.nocookie.net/brawlhalla_gamepedia/images/7/7a/Scarlet.png/revision/latest/scale-to-width-down/815?cb=20210315020007",
        "sentinel" : "https://static.wikia.nocookie.net/brawlhalla_gamepedia/images/9/91/Sentinel.png/revision/latest/scale-to-width-down/522?cb=20201113022225",
        "sidra" : "https://static.wikia.nocookie.net/brawlhalla_gamepedia/images/e/e6/Sidra.png/revision/latest/scale-to-width-down/1000?cb=20210315020107",
        "sir roland" : "https://static.wikia.nocookie.net/brawlhalla_gamepedia/images/6/6f/Sir_Roland.png/revision/latest/scale-to-width-down/1000?cb=20210315015836",
        "teros" : "https://static.wikia.nocookie.net/brawlhalla_gamepedia/images/f/ff/Teros.png/revision/latest/scale-to-width-down/1000?cb=20210315020212",
        "thatch" : "https://static.wikia.nocookie.net/brawlhalla_gamepedia/images/5/51/Thatch.png/revision/latest/scale-to-width-down/672?cb=20201113021805", 
        "thor" : "https://static.wikia.nocookie.net/brawlhalla_gamepedia/images/0/0b/Thor.png/revision/latest/scale-to-width-down/1000?cb=20210315020302",
        "ulgrim" : "https://static.wikia.nocookie.net/brawlhalla_gamepedia/images/3/33/Ulgrim.png/revision/latest/scale-to-width-down/1000?cb=20210315020349",
        "val" : "https://static.wikia.nocookie.net/brawlhalla_gamepedia/images/f/fc/Val.png/revision/latest/scale-to-width-down/862?cb=20210315020432",
        "vector" : "https://static.wikia.nocookie.net/brawlhalla_gamepedia/images/2/27/Vector.png/revision/latest/scale-to-width-down/1000?cb=20190929210243",
        "volkov" : "https://static.wikia.nocookie.net/brawlhalla_gamepedia/images/2/25/Volkov.png/revision/latest/scale-to-width-down/1000?cb=20191219192202",
        "wu shang" : "https://static.wikia.nocookie.net/brawlhalla_gamepedia/images/5/5e/Wu_Shang.png/revision/latest/scale-to-width-down/1000?cb=20210315020641",
        "xull" : "https://static.wikia.nocookie.net/brawlhalla_gamepedia/images/6/6c/Xull.png/revision/latest/scale-to-width-down/1000?cb=20200610141103",
        "yumiko" : "https://static.wikia.nocookie.net/brawlhalla_gamepedia/images/1/1e/Yumiko.png/revision/latest/scale-to-width-down/1000?cb=20210315020732",
        "zariel" : "https://static.wikia.nocookie.net/brawlhalla_gamepedia/images/f/f4/Zariel.png/revision/latest/scale-to-width-down/413?cb=20180731213139",
        "unknown" : "https://media.istockphoto.com/vectors/question-mark-icon-flat-vector-illustration-design-vector-id1162198273?k=20&m=1162198273&s=612x612&w=0&h=s_5DDSXgMDkGq0sVqYpgD2AL1CuB9oK5UtmvMq6XBo8="
    }

    def __init__(self, rootWindow):
        self.legendImage = None
        self.mainFrame = ttk.Frame(rootWindow)
        self.mainFrame.pack(side='top', fill='x')

        self.leftFrame = ttk.Frame(self.mainFrame)
        self.leftFrame.pack(side='left')

        self.rightFrame = ttk.Frame(self.mainFrame)
        self.rightFrame.pack(side='right', fill='y')
        self.rightFrame.config(padding=(0,70, 130, 0))



        #left side widgets
        self.label1 = ttk.Label(self.leftFrame, text="Player's top character:")
        self.label1.pack(padx=(0, 150), pady=(70, 0))
        self.canvas = tk.Canvas(self.leftFrame)
        self.canvas.pack()

        legendName = ttk.Label(self.leftFrame, text="Ada", font='Helvetica 15 bold')
        legendName.pack(padx=(0, 175), pady=(15, 20))

        self.legendDetails = {"Wins" : 0, "Level" : 0, "KOs" : 0}
        self.label2 = ttk.Label(self.leftFrame, text="Wins: {Wins}   |   Level: {Level}   |   KOs: {KOs}".format(**self.legendDetails))
        self.label2.pack(padx=(0, 175))


    
        #right side widgets
        self.playerDetails = {"Name" : "?", "ID" : 0, "Level" : 0}
        self.label3 = ttk.Label(self.rightFrame, text="Name: {Name}   |   ID: {ID}   |   Level: {Level}".format(**self.playerDetails))
        self.label3.pack()

        self.label4 = ttk.Label(self.rightFrame)
        self.label4.pack(padx=(0, 15))
        self.playerRecord = {"Games Played" : 0, "Games Won" : 0, "Games Lost" : 0}
        detailsSTR = "\n\n\n\n\n"
        for entry in self.playerRecord:
            detailsSTR += entry+": "+str(self.playerRecord.get(entry))
            detailsSTR += "\n\n\n\n"
        
        self.label4.config(text=detailsSTR)
        
    def displayLegend(self, topLegend):
        
        #retrieve pic url from given key
        try:
            url = DetailsSection.brawlhallaLegends[topLegend]
        except KeyError:
            url = DetailsSection.brawlhallaLegends["unknown"]
        
        response = req.get(url)
        legend = Image.open(BytesIO(response.content))
        newsize = (int(legend.width/2.2), int(legend.height/2.2))
    
        self.legendImage = ImageTk.PhotoImage(legend.resize(newsize))
        self.canvas.create_image(300, 300, image=self.legendImage)


