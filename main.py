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
timer = None # this is the actual clock value -- need to alter it with window.after(); needs to be global so it can be changed outside of count_down() function

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    #reset check marks, clock, stop timer, change title back
    #stop the timer
    window.after_cancel(timer) #cancel the timer, stops counting down
    canvas.itemconfig(timer_text, text="00:00") # need canvas.itemconfig to edit any item on canvas
    title.config(text='Timer')
    check_marks.config(text = '')
    global reps # call the global variable before editing it again
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps +=1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 ==0:
        count_down(long_break_sec)
        title.config(text= "Break", fg= RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        title.config(text="Work", fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}" #dynamic text --> change data type

    canvas.itemconfig(timer_text,text = f"{count_min}:{count_sec}") # to change something in a canvas ojbect, need to specify the canvas with .itemconfig and item you want to change
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)  # after method ---> takes amount of time to wait (ms), calls a function, passing any arguments you specify
    else:
        start_timer() #restart timer and go to next session
        checks = ''
        work_sessions = math.floor(reps/2) # round down the number of reps to get the total number of completed work/short break sessions that have been done (after
        for _ in range(work_sessions):
            checks += '✔'
            check_marks.config(text = checks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg = YELLOW)

title = Label(text= "Timer",bg = YELLOW, fg= GREEN, font=(FONT_NAME, 40, 'bold'))
title.grid(column=1, row =0)

# canvas w/ tomato and timer
canvas = Canvas(width = 210 , height = 230, bg= YELLOW, highlightthickness=0) #higlight removes the boarder around canvas
tomato = PhotoImage(file = 'tomato.png')
canvas.create_image(100, 118, image= tomato) #provide x,y coords; image needs to be of PhotoImage class
timer_text = canvas.create_text(100, 135, text = "00:00", fill = "white", font=(FONT_NAME, 30, 'bold'))
canvas.grid(column = 1, row = 1)



start = Button(text = 'Start', highlightthickness=0, command=start_timer)
start.grid(column = 0, row = 2)

reset = Button(text = 'Reset', highlightthickness=0, command= reset_timer)
reset.grid(column = 2, row = 2)

check_marks = Label(fg = GREEN, bg=YELLOW, font=(FONT_NAME, 14))
check_marks.grid(column= 1, row =3)

window.mainloop()
