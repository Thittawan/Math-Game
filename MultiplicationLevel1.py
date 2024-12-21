import random
import pygame
from tkinter import *

num1 = [1,2,3,4,5,6,7,8,9,]
num2 = [10,11,12,13,14,15,16,17,18,19,20,]

def submt(var1):
    if var1.get() == str(resultPLUS()):
        correct = Label(app, text="Correct!", fg="green", font=("Courier", 16))
        correct.place(relx=0.33, rely=0.2)
    else:
        wrong = Label(app, text="Wrong" + " The answer is " + str(try_again.num1update * try_again.num2update), fg="red", font=("Courier", 10))
        wrong.place(relx=0.15, rely=0.2)
        pygame.mixer.music.load("ES_Buzzer 9 - SFX Producer.mp3")
        pygame.mixer.music.play(loops=0)

def try_again():
    try_again.num1update = random.choice(num2)
    try_again.num2update = random.choice(num1)

    newQ = Label(
        app, text=f"{try_again.num1update}*{try_again.num2update}", font=("Courier", 16)
    )
    newQ.place(relx=0.16, rely=0.14, relwidth=0.7, relheight=0.23)


def resultPLUS():
    try_again
    return try_again.num1update * try_again.num2update



app = Tk()
app.title("Math For Kids")
# canvas = Canvas(app, width=240, height=300)
# canvas.pack()
app.geometry("290x300")
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
submit.place(relx=0.35, rely=0.64, relwidth=0.34, relheight=0.23)
try_again = Button(app, text="Try Again", command=try_again)
try_again.place(relx=0.415, rely=0.9)

pygame.mixer.music.load("Song1.mp3")
pygame.mixer.music.play(-1)

app.mainloop()

