# Flashcard GUI app
import random
import tkinter as tk
import pandas

BACKGROUND_COLOR = "#B1DDC6"

# Data Ingress

data = pandas.read_csv("./data/french_words.csv")

# Game Setup

word_dict = {word: definition for word, definition in zip(data["French"], data["English"])}
known_words = {}
unknown_words = {key: 1 for key in data["French"]}
current_word = random.choice(list(unknown_words.keys()))


def handle_correct_btn() -> None:
    """
    Called when the "I know this" or "Check" button is pressed:

    - Should remove a word from the set of unknown words.
    - Should add the same word to the list of known words.
    - Should update the view with a new word.
    """
    global current_word, unknown_words, known_words

    if len(unknown_words) == 0:
        # Player has won the game.
        return

    unknown_words.pop(current_word)
    known_words[current_word] = 1

    current_word = random.choice(list(unknown_words.keys()))
    canvas.itemconfig(word_obj_id, text=current_word)


def handle_incorrect_btn() -> None:
    """
    Called when the "I DON'T know this" or "Cross" button is pressed:

    - Should update the view with a new word.
    """
    global current_word
    current_word = random.choice(list(unknown_words.keys()))
    canvas.itemconfig(word_obj_id, text=current_word)


# UI Setup

window = tk.Tk()
window.title("FlashCards!")
window.config(width=700, height=500, background=BACKGROUND_COLOR, padx=50, pady=50)
window.minsize(width=600, height=500)

check_img = tk.PhotoImage(file="./images/right.png")
check_btn = tk.Button(image=check_img, highlightthickness=0, background=BACKGROUND_COLOR, command=handle_correct_btn)

cross_img = tk.PhotoImage(file="./images/wrong.png")
cross_btn = tk.Button(image=cross_img, highlightthickness=0, background=BACKGROUND_COLOR, command=handle_incorrect_btn)

canvas = tk.Canvas(width=800, height=526, highlightthickness=0, background=BACKGROUND_COLOR)

flashcard_front_img = tk.PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 260, image=flashcard_front_img)

canvas.create_text(400, 150, text="Title", font=("Ariel", 48, "italic"))
word_obj_id = canvas.create_text(400, 263, text=current_word, font=("Ariel", 60, "bold"))


canvas.grid(row=0, column=0, columnspan=2)
check_btn.grid(row=1, column=1)
cross_btn.grid(row=1, column=0)



window.mainloop()