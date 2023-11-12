import tkinter as tk
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")

    global reps
    reps = 0






# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_secs = math.floor(0.5 * 60)
    short_break_sec = math.floor(0.5 * 60)
    long_break_sec = math.floor(0.5 * 60)

    if reps % 8 == 0:
        title_label.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        title_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        title_label.config(text="Work", fg=GREEN)
        count_down(work_secs)






# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
# This actually was NOT the way to implement
# def countdown(minutes: int):
#     seconds = minutes * 60
#
#
#     current_time = time.time()
#     complete_time = current_time + seconds
#
#     for _ in range(seconds):
#         current_time = time.time()
#
#         diff = complete_time - current_time
#         d_minutes = diff / 60
#         d_seconds = diff % 60
#
#         print(f"{d_minutes}:{d_seconds}")
#         time.sleep(1)
#
#         as
def count_down(seconds: int):
    if seconds >= 0:
        formatted_min = math.floor(seconds / 60)
        formatted_sec = seconds % 60
        if formatted_sec < 10:
            formatted_sec = f"0{formatted_sec}"

        if formatted_min < 10:
            formatted_min = f"0{formatted_min}"

        canvas.itemconfig(timer_text, text=f"{formatted_min}:{formatted_sec}")
        # NOTE: This is the method that we'd get into the looping mechanism for the tkinter window.
        # Read as: after this time in ms call this function with these arguments
        global timer
        timer = window.after(1000, count_down, seconds - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

# Goal is to create a "pomodoro" like time management app.

window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = tk.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.pack()

canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.pack()

start_button = tk.Button(text="Start", command=start_timer)
reset_button = tk.Button(text="Reset", command=reset_timer)

start_button.pack()
reset_button.pack()


window.mainloop()