#!/usr/bin/python3

import sys
import urllib.request
import json
import tkinter as tk
from tkinter import messagebox

application = tk.Tk()
application.title("ISS Location Now")
application.grid_columnconfigure(0)
application.grid_rowconfigure(0)

latitude = tk.DoubleVar()
longitude = tk.DoubleVar()
time = tk.IntVar()
message = tk.StringVar()

def quit():
    sys.exit(0)

def run():
    try:
        url = "http://api.open-notify.org/iss-now.json"
        data = json.loads(urllib.request.urlopen(url).read().decode())
        latitude.set(data["iss_position"]["latitude"])
        longitude.set(data["iss_position"]["longitude"])
        time.set(data["timestamp"])
        message.set(data["message"])
    except Exception as e:
        messagebox.showerror("Error", e)
        return
    return

label = tk.Label(application, text="Latitude").grid(
    row=0, column=0, padx=5, pady=5)

text = tk.Entry(application, textvariable=latitude).grid(
    row=0, column=1, padx=5, pady=5)

label = tk.Label(application, text="Longitude", ).grid(
    row=1, column=0, padx=5, pady=5)

text = tk.Entry(application, textvariable=longitude).grid(
    row=1, column=1, padx=5, pady=5)
    
label = tk.Label(application, text="Time").grid(
    row=2, column=0, padx=5, pady=5)

text = tk.Entry(application, textvariable=time).grid(
    row=2, column=1, padx=5, pady=5)

label = tk.Label(application, text="Message").grid(
    row=3, column=0, padx=5, pady=5)

text = tk.Entry(application, textvariable=message).grid(
    row=3, column=1, padx=5, pady=5)

button = tk.Button(application, text="Run",  command=run).grid(
    row=4, column=0, padx=5, pady=5, sticky="w")

button = tk.Button(application, text="Quit", command=quit).grid(
    row=4, column=1, padx=5, pady=5, sticky="e")

application.mainloop()

