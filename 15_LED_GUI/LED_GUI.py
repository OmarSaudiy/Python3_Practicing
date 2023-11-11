#!/usr/bin/python3
import tkinter as tk

# Function to turn the LED on (set red light)
def turn_on_led():
    canvas.itemconfig(led, fill='red')

# Function to turn the LED off (no color)
def turn_off_led():
    canvas.itemconfig(led, fill='')

# Create the main window
window = tk.Tk()
window.title("LED Control")

# Create a canvas for displaying the LED
canvas = tk.Canvas(window, width=100, height=100)
canvas.pack()

# Create the LED (initially off)
led = canvas.create_oval(10, 10, 90, 90, fill='')

# Create buttons to control the LED
on_button = tk.Button(window, text="Turn On", command=turn_on_led)
off_button = tk.Button(window, text="Turn Off", command=turn_off_led)

on_button.pack()
off_button.pack()

window.mainloop()