from tkinter import *
import math
import winsound
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECKMARK = "❎"
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    what_we_do.config(text="Timer", fg=GREEN)
    check_mark.config(text="")
    reps = 0

def finshed_cycle():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    what_we_do.config(text="Nice Work", fg=GREEN)
    check_mark.config(text="")
    reps = 0
    for x in range(1, 4):
        winsound.Beep(2000, 1000)
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    if reps == 9:
        finshed_cycle()
    elif reps % 2 == 0 and reps < 8:
        what_we_do.config(text="Break", fg=RED)
        short_break_seconds = SHORT_BREAK_MIN * 60
        count_down(short_break_seconds)
        for x in range(1, 4):
            winsound.Beep(1000, 1000)
    elif reps == 8:
        what_we_do.config(text="Break", fg=PINK)
        long_break_seconds = LONG_BREAK_MIN * 60
        count_down(long_break_seconds)
        for x in range(1, 4):
            winsound.Beep(1000, 1000)
        # reset_timer()
    else:
        what_we_do.config(text="Work", fg=GREEN)
        work_seconds = WORK_MIN * 60
        count_down(work_seconds)
        for x in range(1, 4):
            winsound.Beep(1000, 1000)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(seconds):
    minutes = int(seconds / 60)
    display_seconds = seconds % 60
    if display_seconds < 10:
        canvas.itemconfig(timer_text, text=f"{minutes}:0{display_seconds}")
    else:
        canvas.itemconfig(timer_text, text=f"{minutes}:{display_seconds}")
    if seconds > 0:
        global timer
        timer = window.after(1000, count_down, seconds - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "❎"
        check_mark.config(text=marks)




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Work Smart")
window.config(padx=100, pady=50, background=YELLOW)



what_we_do = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 45, "bold"))
what_we_do.grid(column=1, row=0)


canvas = Canvas(width=200, height=224, background=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)



button1 = Button(text="Start", command=start_timer)
button1.grid(column=0, row=2)

button2 = Button(text="Reset", command=reset_timer)
button2.grid(column=3, row=2)

check_mark = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
check_mark.place(x=60, y=300)





window.mainloop()