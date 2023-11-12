import time
import tkinter as tk

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    pass


# ---------------------------- TIMER MECHANISM ------------------------------- #



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(minutes: int):
    seconds = minutes * 60


    current_time = time.time()
    complete_time = current_time + seconds

    for _ in range(seconds):
        current_time = time.time()

        diff = complete_time - current_time
        d_minutes = diff / 60
        d_seconds = diff % 60

        print(f"{d_minutes}:{d_seconds}")
        time.sleep(1)

        as


display_clock = ""
# ---------------------------- UI SETUP ------------------------------- #

# Goal is to create a "pomodoro" like time management app.

window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(103, 130, text=display_clock, fill="white", font=(FONT_NAME, 35, "bold"))
canvas.pack()

start_button = tk.Button(text="Start", command=lambda: countdown(25))
reset_button = tk.Button(text="Reset")

start_button.pack()
reset_button.pack()


window.mainloop()