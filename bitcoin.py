import tkinter as tk
import requests
from datetime import datetime


def trackBitcoin():
    url = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR"
    response = requests.get(url).json()
    price = response["USD"]
    time = datetime.now().strftime("%H:%M:%S")

    labelPrice.config(text=str(price) + "$")
    labelTime.config(text="Updated at: " + time)

    canvas.after(5000, trackBitcoin)


canvas = tk.Tk()
canvas.geometry("400x500")
canvas.title("Bitcoin Price Tracker")

font1 = ("poppins", 24, "bold")
font2 = ("poppins", 24, "bold")
font3 = ("poppins", 24, "bold")

label = tk.Label(canvas, text="Bitcoin Price", font="font1")
label.pack(pady=20)

labelPrice = tk.Label(canvas, font=font2)
labelPrice.pack(pady=20)

labelTime = tk.Label(canvas, font=font3)
labelTime.pack(pady=20)

trackBitcoin()

canvas.mainloop()
