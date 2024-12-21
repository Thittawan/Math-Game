import random
import tkinter
import pygame
import math
from tkinter import *

num2 = [11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]
num1 = [1,2,3,4,5,6,7,8,9,10]
def submt(var1):
    if var1.get() == str(resultPLUS()):
        correct = Label(app, text="Correct!", fg="green", font=("Courier", 16))
        correct.place(relx=0.33, rely=0.3)

    else:
        wrong = Label(app, text="Wrong" + " The answer is " + str(round_half_up(try_again.num1update / try_again.num2update,2)), fg="red", font=("Courier", 10))
        wrong.place(relx=0.15, rely=0.3)
        pygame.mixer.music.load("ES_Buzzer 9 - SFX Producer.mp3")
        pygame.mixer.music.play(loops=0)



def try_again():
    try_again.num1update = random.choice(num2)
    try_again.num2update = random.choice(num1)
    newQ = Label(
        app, text=f"{try_again.num1update}/{try_again.num2update}", font=("Courier", 15))

    newQ.place(relx=0.16, rely=0.14, relwidth=0.7, relheight=0.23)

def round_half_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n*multiplier + 0.5) / multiplier

def resultPLUS():
    try_again
    return (round_half_up(try_again.num1update / try_again.num2update,2))



app = Tk()
app.title("Math For Kids")
# canvas = Canvas(app, width=240, height=300)
# canvas.pack()
app.geometry("290x310")
app.resizable(False, False)

pygame.mixer.init()
def play():
    pygame.mixer.music.load("Song1.mp3")
    pygame.mixer.music.play(loops=0)
Music = Button(app, text="Play Music", command=play)
Music.place(relx=0.40, rely=0.01)

start = Button(app, text="Start", command=try_again)
start.place(relx=0.45, rely=0.2,)

solving = Entry(app)
solving.place(relx=0.35, rely=0.4, relwidth=0.34, relheight=0.23)
submit = Button(app, text="Submit", command=lambda: submt(solving))
submit.place(relx=0.35, rely=0.64, relwidth=0.34, relheight=0.15)
try_again = Button(app, text="Try Again", command=try_again)
try_again.place(relx=0.415, rely=0.8)
title_lable = tkinter.Label(master=app, text='Round the answer to 2 decimal place "0.00"')
title_lable.place(relx=0.11, rely=0.09)

title_lable = tkinter.Label(master=app, text='If the answer have no decimal please put ".0"')
title_lable.place(relx=0.11, rely=0.9)

pygame.mixer.music.load("Song1.mp3")
pygame.mixer.music.play(-1)

app.mainloop()