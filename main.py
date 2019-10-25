import tkinter as tk
import requests
from PIL import Image, ImageTk

HEIGHT = 500
WIDTH = 800

def test_function(loc):
    print("Get weather for", loc)

def get_weather(city):
    weather_key = '7e8c333fb2d66541012d69eb1e323358'
    url = 'https://api.openweathermap.org/data/2.5/forecast'
    params = {'APPID': weather_key, 'q' : city, 'units' : 'imperial'}
    response = requests.get(url, params=params)
    print(response.json())

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='c:/Users/nuajd15/Desktop/VS Workspace/Weather GUI/background.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg="#b3cce6", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor="n")

entry = tk.Entry(frame, bg="lightgray")
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get Weather", bg="gray", activebackground="orange", command=lambda: test_function(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg="#b3cce6", bd=5)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor="n")

label = tk.Label(lower_frame, text="label", bg="lightgray")
label.place(relwidth=1, relheight=1)

root.mainloop()