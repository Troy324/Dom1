import tkinter as tk
import random
from tkinter import *
from tkinter import ttk

root = tk.Tk()
root.title("Дом")
root.geometry("400x460")

def toggle_light():
    global light_on
    light_on = not light_on

    if light_on:

        canvas.config(bg="midnightblue")
        canvas.itemconfig(window, fill="yellow")
        button.config(text="Выключить свет")
    else:
        canvas.config(bg="lightblue")
        canvas.itemconfig(window, fill="white")
        button.config(text="Включить свет")


canvas = tk.Canvas(root, width=400, height=400, bg="lightblue")
canvas.pack()

canvas.create_polygon(100, 150, 300, 150, 200, 50, fill="pink", outline="black") #Крыша
canvas.create_rectangle(120, 150, 280, 300, fill="green", outline="black") #Стены
canvas.create_rectangle(180, 180, 220, 220, fill="white") #Окно

light_on = False
button = tk.Button(root, text="Включить свет", command=toggle_light)
button.pack(pady=10)

root.mainloop()