import json
from playsound import playsound
from tkinter import *
import random


BACKGROUND_COLOR = "#B1DDC6"
word_data = {}
#__________________ACCESSING SOUND FILES_________________________#
# Accessing json
with open("is_data.json", 'r') as data_file:
    # Reading old data
    data = json.load(data_file)

# Creating a dictionary to avoid repetition of guess words
dict = {key:value for (key, value) in data.items() if int(key) <= 1000}

def is_sound_play():
    sound = word_data["sound"]
    playsound(sound)

# Word Randomiser
def next_card():
    rd_word_index = random.randint(0, 1001)
    global word_data, flip_timer
    window.after_cancel(flip_timer)

    word_data = dict[str(rd_word_index)]
    is_word = word_data["word"]
    en_word = word_data["trans"]
    sound = word_data["sound"]

    canvas.itemconfig(canvas_bg, image=card_front_img)
    canvas.itemconfig(card_word, text=is_word, fill="black")
    canvas.itemconfig(card_title, text="íslensku", fill="#5A5A5A")

    is_sound_play()
    flip_timer = window.after(10000, func=flip_card)
#___________________FLIP OVER_________________________________#
def flip_card():
    canvas.itemconfig(canvas_bg, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=word_data["trans"], fill="white")


#_________________________UI SETUP__________________________#
window = Tk()
window.title("Flash Cards")
window.config(background=BACKGROUND_COLOR, padx=50, pady=50)
flip_timer = window.after(10000, func=flip_card)

# Adding images
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")
play_img = PhotoImage(file="images/play.png")

# Creating canvas and adding images to canvas
canvas = Canvas(window,background=BACKGROUND_COLOR ,width=800, height=526, highlightthickness=0)

canvas_bg = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="Title",fill="#5A5A5A", font=("American Typewriter", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word",fill="black", font=("American Typewriter", 60, "bold"))
play_button = Button(canvas, bg="white", image=play_img, command=is_sound_play, highlightthickness=0, highlightbackground="white", highlightcolor="white").place(x=690, y=20)
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
right_button = Button(image=right_img, command=next_card, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, highlightcolor=BACKGROUND_COLOR)
right_button.grid(column=0, row=1)

wrong_button = Button(image=wrong_img, command=next_card, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, highlightcolor=BACKGROUND_COLOR)
wrong_button.grid(column=1, row=1)


next_card()

window.mainloop()
