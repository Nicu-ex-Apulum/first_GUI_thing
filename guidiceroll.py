#!/usr/bin/env python3
import tkinter as tk 
from tkinter import *
from random import random, seed
from PIL import Image, ImageTk
import time

rolls=[0,0,0,0,0,0,0,0,0,0]
#rolls the dice and prints the "chart"
def roll():
	i=0
	for roll in rolls:
		rolls[i] = int(random() * 6 + 1)
		i += 1

	coll1.place( relwidth= 0.10, relheight= (rolls[0] / 6), relx= 0, rely= 1 - (rolls[0] / 6))
	coll2.place( relwidth= 0.10, relheight= (rolls[1] / 6), relx= 0.1, rely= 1 - (rolls[1] / 6))
	coll3.place( relwidth= 0.10, relheight= (rolls[2] / 6), relx= 0.2, rely= 1 - (rolls[2] / 6))
	coll4.place( relwidth= 0.10, relheight= (rolls[3] / 6), relx= 0.3, rely= 1 - (rolls[3] / 6))
	coll5.place( relwidth= 0.10, relheight= (rolls[4] / 6), relx= 0.4, rely= 1 - (rolls[4] / 6))
	coll6.place( relwidth= 0.10, relheight= (rolls[5] / 6), relx= 0.5, rely= 1 - (rolls[5] / 6))
	coll7.place( relwidth= 0.10, relheight= (rolls[6] / 6), relx= 0.6, rely= 1 - (rolls[6] / 6))
	coll8.place( relwidth= 0.10, relheight= (rolls[7] / 6), relx= 0.7, rely= 1 - (rolls[7] / 6))
	coll9.place( relwidth= 0.10, relheight= (rolls[8] / 6), relx= 0.8, rely= 1 - (rolls[8] / 6))
	coll10.place( relwidth= 0.10, relheight= (rolls[9] / 6), relx= 0.9, rely= 1 - (rolls[9] / 6))

	#dice change part
	if rolls[9]==1:
		dice_display1.place(width= 100, height= 100)
		dice_display2.place(width= 0, height= 0)
		dice_display3.place(width= 0, height= 0)
		dice_display4.place(width= 0, height= 0)
		dice_display5.place(width= 0, height= 0)
		dice_display6.place(width= 0, height= 0)
	elif rolls[9]==2:
		dice_display1.place(width= 0, height= 0)
		dice_display2.place(width= 100, height= 100)
		dice_display3.place(width= 0, height= 0)
		dice_display4.place(width= 0, height= 0)
		dice_display5.place(width= 0, height= 0)
		dice_display6.place(width= 0, height= 0)	
	elif rolls[9]==3:
		dice_display1.place(width= 0, height= 0)
		dice_display2.place(width= 0, height= 0)
		dice_display3.place(width= 100, height= 100)
		dice_display4.place(width= 0, height= 0)
		dice_display5.place(width= 0, height= 0)
		dice_display6.place(width= 0, height= 0)
	elif rolls[9]==4:
		dice_display1.place(width= 0, height= 0)
		dice_display2.place(width= 0, height= 0)
		dice_display3.place(width= 0, height= 0)
		dice_display4.place(width= 100, height= 100)
		dice_display5.place(width= 0, height= 0)
		dice_display6.place(width= 0, height= 0)	
	elif rolls[9]==5:
		dice_display1.place(width= 0, height= 0)
		dice_display2.place(width= 0, height= 0)
		dice_display3.place(width= 0, height= 0)
		dice_display4.place(width= 0, height= 0)
		dice_display5.place(width= 100, height= 100)
		dice_display6.place(width= 0, height= 0)	
	elif rolls[9]==6:
		dice_display1.place(width= 0, height= 0)
		dice_display2.place(width= 0, height= 0)
		dice_display3.place(width= 0, height= 0)
		dice_display4.place(width= 0, height= 0)
		dice_display5.place(width= 0, height= 0)
		dice_display6.place(width= 100, height= 100)

#clears chart
def reset():
	rolls=[0,0,0,0,0,0,0,0,0,0]
	coll1.place( relwidth= 0.10, relheight= (rolls[0] / 6), relx= 0, rely= 1 - (rolls[0] / 6))
	coll2.place( relwidth= 0.10, relheight= (rolls[1] / 6), relx= 0.1, rely= 1 - (rolls[1] / 6))
	coll3.place( relwidth= 0.10, relheight= (rolls[2] / 6), relx= 0.2, rely= 1 - (rolls[2] / 6))
	coll4.place( relwidth= 0.10, relheight= (rolls[3] / 6), relx= 0.3, rely= 1 - (rolls[3] / 6))
	coll5.place( relwidth= 0.10, relheight= (rolls[4] / 6), relx= 0.4, rely= 1 - (rolls[4] / 6))
	coll6.place( relwidth= 0.10, relheight= (rolls[5] / 6), relx= 0.5, rely= 1 - (rolls[5] / 6))
	coll7.place( relwidth= 0.10, relheight= (rolls[6] / 6), relx= 0.6, rely= 1 - (rolls[6] / 6))
	coll8.place( relwidth= 0.10, relheight= (rolls[7] / 6), relx= 0.7, rely= 1 - (rolls[7] / 6))
	coll9.place( relwidth= 0.10, relheight= (rolls[8] / 6), relx= 0.8, rely= 1 - (rolls[8] / 6))
	coll10.place( relwidth= 0.10, relheight= (rolls[9] / 6), relx= 0.9, rely= 1 - (rolls[9] / 6))
	dice_display1.place(width= 0, height= 0)
	dice_display2.place(width= 0, height= 0)
	dice_display3.place(width= 0, height= 0)
	dice_display4.place(width= 0, height= 0)
	dice_display5.place(width= 0, height= 0)
	dice_display6.place(width= 0, height= 0)

root = tk.Tk()
root.title('Rolly boi')
root.geometry('333x166')
root.resizable(False, False)
root.iconphoto(False, ImageTk.PhotoImage(file= "dice6.png"))

canvas = tk.Canvas(root)
canvas.pack()

main = tk.Frame(root, bg="grey")
main.place(relwidth=1, relheight=1)
#dice part
dice_area = tk.Frame(main)
dice_area.place( relwidth= 0.3, relheight= 0.6, rely= 0.07, relx= 0.08)

image1 = Image.open('dice1.png')
image2 = Image.open('dice2.png')
image3 = Image.open('dice3.png')
image4 = Image.open('dice4.png')
image5 = Image.open('dice5.png')
image6 = Image.open('dice6.png')
dice1 = ImageTk.PhotoImage(image1)
dice2 = ImageTk.PhotoImage(image2)
dice3 = ImageTk.PhotoImage(image3)
dice4 = ImageTk.PhotoImage(image4)
dice5 = ImageTk.PhotoImage(image5)
dice6 = ImageTk.PhotoImage(image6)
dice_display1= tk.Label(dice_area,image=dice1,)
dice_display2= tk.Label(dice_area,image=dice2,)
dice_display3= tk.Label(dice_area,image=dice3,)
dice_display4= tk.Label(dice_area,image=dice4,)
dice_display5= tk.Label(dice_area,image=dice5,)
dice_display6= tk.Label(dice_area,image=dice6,)
#dice_display.place(width= 100, height= 100)


#chart part
chart_area = tk.Canvas(main)
chart_area.place( relwidth= 0.46, relheight= 0.6, rely=0.07, relx= 0.46)

line = chart_area.create_line(0, 15, 154, 15)
line = chart_area.create_line(0, 32, 154, 32)
line = chart_area.create_line(0, 49, 154, 49)
line = chart_area.create_line(0, 65, 154, 65)
line = chart_area.create_line(0, 82, 154, 82)

coll1 = tk.Canvas(chart_area, bg= '#ff0080', highlightcolor='#ffffff')
coll2 = tk.Canvas(chart_area, bg= '#ff66b3', highlightcolor='#ffffff')
coll3 = tk.Canvas(chart_area, bg= '#cc3399', highlightcolor='#ffffff')
coll4 = tk.Canvas(chart_area, bg= '#e699cc', highlightcolor='#ffffff')
coll5 = tk.Canvas(chart_area, bg= '#ff33cc', highlightcolor='#ffffff')
coll6 = tk.Canvas(chart_area, bg= '#ff80df', highlightcolor='#ffffff')
coll7 = tk.Canvas(chart_area, bg= '#ff0066', highlightcolor='#ffffff')
coll8 = tk.Canvas(chart_area, bg= '#ff66a3', highlightcolor='#ffffff')
coll9 = tk.Canvas(chart_area, bg= '#ff1ab3', highlightcolor='#ffffff')
coll10 = tk.Canvas(chart_area, bg= '#ff80d5', highlightcolor='#ffffff')

roll_button = tk.Button(main, text="Roll", command= roll)
roll_button.place( relwidth= 0.2, relheight= 0.1, rely= 0.75, relx= 0.4)

reset_button = tk.Button(main, text="reset", command= reset)
reset_button.place( relwidth= 0.1, relheight= 0.05, rely= 0.9, relx= 0.45)

root.mainloop()