# Flashcard GUI app

import tkinter as tk


window = tk.Tk()
window.title("FlashCards!")
window.config(width=800, height=500)
window.minsize(width=1000, height=500)

# canvas = tk.Canvas(width=)

check_img = tk.PhotoImage(file="./images/right.png")
check_btn = tk.Button(image=check_img, highlightthickness=1)

cross_img = tk. PhotoImage(file="./images/wrong.png")
cross_btn = tk.Button(image=cross_img, highlightthickness=1)


canvas = tk.Canvas(width=600, height=400, highlightthickness=1)
flashcard_front_img = tk.PhotoImage(file="./images/card_front.png")
canvas.create_image(200, 200, image=flashcard_front_img)


canvas.grid(row=0, column=0, columnspan=2)
check_btn.grid(row=1, column=1)
cross_btn.grid(row=1, column=0)





window.mainloop()