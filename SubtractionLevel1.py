import random
import pygame
from tkinter import *

num1 = [1,2,3,4,5,6,7,8,9,10,11, 12, 13, 14, 15, 16, 17, 18, 19,
20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
40, 41, 42, 43, 44, 45, 46, 47, 48, 49,
50,]
num2 = [50, 51, 52, 53, 54, 55, 56, 57, 58, 59,
60, 61, 62, 63, 64, 65, 66, 67, 68, 69,
70, 71, 72, 73, 74, 75, 76, 77, 78, 79,
80, 81, 82, 83, 84, 85, 86, 87, 88, 89,
90, 91, 92, 93, 94, 95, 96, 97, 98, 99,
100.]

def submt(var1):
    if var1.get() == str(resultPLUS()):
        correct = Label(app, text="Correct!", fg="green", font=("Courier", 16))
        correct.place(relx=0.33, rely=0.2)
    else:
        wrong = Label(app, text="Wrong" + " The answer is " + str(try_again.num1update - try_again.num2update), fg="red", font=("Courier", 11))
        wrong.place(relx=0.15, rely=0.2)
        pygame.mixer.music.load("ES_Buzzer 9 - SFX Producer.mp3")
        pygame.mixer.music.play(loops=0)

def try_again():
    try_again.num1update = random.choice(num2)
    try_again.num2update = random.choice(num1)

    newQ = Label(
        app, text=f"{try_again.num1update}-{try_again.num2update}", font=("Courier", 16)
    )
    newQ.place(relx=0.16, rely=0.14, relwidth=0.7, relheight=0.23)


def resultPLUS():
    try_again
    return try_again.num1update - try_again.num2update



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