from doctest import master
import imghdr
from webbrowser import get
import requests
from bs4 import BeautifulSoup
from tkinter import Label
from tkinter import Tk
from PIL import ImageTk, Image
import pyttsx3



master = Tk()
master.title("Text to Speech")
master.config(bg="black")

img = Image.open("C:/Users/User/Desktop/Text to Speech/OIP.jpg")
img = img.resize((150, 150))
img = ImageTk.PhotoImage(img)

locationLabel = Label(master, font=("Calibri bold", 20), bg="black")
locationLabel.grid(row=0, sticky="N", padx=100)

Label(master, image=img, bg="white").grid(row=1, sticky="E")





engine = pyttsx3.init()

for voice in engine.getProperty("voices"):
    print(voice)

voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

def Speak(Audio):
    engine.say(Audio)
    engine.runAndWait()

text = input("Enter your text...:")

Speak(text)

master.mainloop()




