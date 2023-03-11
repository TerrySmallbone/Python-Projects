from tkinter import *
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
checks = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global reps
    global checks
    canvas.itemconfig(timer_text, text="00:00")
    window.after_cancel(timer)
    label_title.config(text="Timer")
    reps = 0
    checks = 0
    label_check_marks.config(text="✔" * checks)


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    global checks
    reps += 1

    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps == 8:
        countdown(long_break)
        label_title.config(text= "Break")
        reps == 0
        checks = 0
        label_check_marks.config(text="✔" * checks)
    elif reps % 2 == 0:
        label_title.config(text="Break")
        checks += 1
        label_check_marks.config(text= "✔" * checks)
        countdown(short_break)
    else:
        label_title.config(text="Work")
        countdown(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def countdown(count):
    global reps

    count_minutes = math.floor(count / 60)
    count_seconds = count % 60
    if (count_seconds) < 10:
        count_seconds = f"0{count_seconds}"

    canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx= 100, pady= 50, bg= GREEN)

canvas = Canvas(window, width=200, height=224, bg= GREEN, highlightthickness= 0)
canvas.grid(column= 1, row= 1)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image= tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white",)

label_title = Label(text= "Timer", font=(FONT_NAME, 40, "bold"), fg= RED, bg= GREEN)
label_title.grid(column= 1, row= 0)

label_check_marks = Label(font=(FONT_NAME, 10, "bold"), fg= RED, bg= GREEN)
label_check_marks.grid(column= 1, row= 3)

button_start = Button(text="Start", font=(FONT_NAME, 10), bg= GREEN, command= start_timer)
button_start.grid(column= 0, row= 2)

button_reset = Button(text="Reset", font=(FONT_NAME, 10), bg= GREEN, command=reset_timer)
button_reset.grid(column= 2, row= 2)




window.mainloop()