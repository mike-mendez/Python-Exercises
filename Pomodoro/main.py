import math
import tkinter

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
    title.config(text="Timer")
    canvas.itemconfig(timer_txt, text="00:00")
    checkmark.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    print(reps)
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        title.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        title.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        title.config(text="Work", fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(start_time):
    timer_min = math.floor(start_time / 60)
    if timer_min < 10:
        timer_min = f"0{timer_min}"
    timer_sec = start_time % 60
    if timer_sec < 10:
        timer_sec = f"0{timer_sec}"

    canvas.itemconfig(timer_txt, text=f"{timer_min}:{timer_sec}")
    if start_time > 0:
        global timer
        timer = window.after(1000, count_down, start_time - 1)
    else:
        start_timer()
        marks = ""
        # checkmark["text"] += ""
        work_sessions = math.floor(reps / 2)
        for i in range(work_sessions):
            marks += "✔"
        checkmark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

# WINDOW
window = tkinter.Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

# TITLE
title = tkinter.Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 34, "bold"))
title.grid(column=1, row=0)

# IMAGE AND COUNTER
pomodoro_img = tkinter.PhotoImage(file="tomato.png")
canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=pomodoro_img)
timer_txt = canvas.create_text(104, 134, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(column=1, row=1)

# START
start_btn = tkinter.Button(text="Start", relief="groove", font=(FONT_NAME, 12, "bold"), command=start_timer)
start_btn.grid(column=0, row=2)

# RESET
reset_btn = tkinter.Button(text="Reset", relief="groove", font=(FONT_NAME, 12, "bold"), command=reset_timer)
reset_btn.grid(column=2, row=2)

# CHECKMARKS
checkmark = tkinter.Label(text="", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 12, "bold"))
checkmark.grid(column=1, row=3)

# KEEP AT END OF PROGRAM
window.mainloop()
