from tkinter.ttk import *
from tkinter import *
from PIL import ImageTk, Image
from datetime import datetime
from time import sleep
from pygame import mixer
from threading import Thread

# Colors
bg_color = '#ffffff'
co1 = "#566FC6"  # blue
co2 = "#000000"  # black

# Window
window = Tk()
window.title("")
window.geometry('350x150')
window.configure(bg=bg_color)

# Frame up
frame_line = Frame(window, width=400, height=5, bg=co1)
frame_line.grid(row=0, column=0)

frame_body = Frame(window, width=400, height=290, bg=bg_color)
frame_body.grid(row=1, column=0)

# Configuring frame body
img = Image.open('Alaram clock\icons.png')
img.resize((100, 100))
img = ImageTk.PhotoImage(img)

app_image = Label(frame_body, height=100, image=img, bg=bg_color)
app_image.place(x=10, y=10)

name = Label(frame_body, text="Alarm", height=1, font=('Ivy 18 bold'), bg=bg_color)
name.place(x=125, y=10)

hour = Label(frame_body, text="hour", height=1, font=('Ivy 10 bold'), bg=bg_color, fg=co1)
hour.place(x=127, y=40)

c_hour = Combobox(frame_body, width=2, font=('arial 15'))
c_hour['values'] = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12")
c_hour.current(0)
c_hour.place(x=130, y=58)

min = Label(frame_body, text="Min", height=1, font=('Ivy 10 bold'), bg=bg_color, fg=co1)
min.place(x=177, y=40)
c_min = Combobox(frame_body, width=2, font=('arial 15'))
c_min['values'] = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30",
                   "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60")
c_min.current(0)
c_min.place(x=180, y=58)

sec = Label(frame_body, text="Sec", height=1, font=('Ivy 10 bold'), bg=bg_color, fg=co1)
sec.place(x=227, y=40)
c_sec = Combobox(frame_body, width=2, font=('arial 15'))
c_sec['values'] = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30",
                   "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60")
c_sec.current(0)
c_sec.place(x=230, y=58)

period = Label(frame_body, text="Period", height=1, font=('Ivy 10 bold'), bg=bg_color, fg=co1)
period.place(x=277, y=40)
c_period = Combobox(frame_body, width=3, font=('arial 15'))
c_period['values'] = ("AM", "PM")
c_period.current(0)
c_period.place(x=280, y=58)

def activate_alarm():
    t = Thread(target=alarm)  # Create a new thread to run the alarm function
    t.start()

def deactivate_alarm():
    print("Deactivated alarm")
    mixer.music.stop()  # Stop playing the alarm sound

selected = IntVar()

rad1 = Radiobutton(frame_body, font=('arial 10 bold'), value=1, text="Activate", bg=bg_color, command=activate_alarm, variable=selected)
rad1.place(x=125, y=95)

def sound_alarm():
    mixer.music.load('Alaram clock\Alarm.mp3')  # Load the alarm sound file
    mixer.music.play()  # Play the alarm sound
    selected.set(0)  # Reset the selected variable to 0

    rad2 = Radiobutton(frame_body, font=('arial 10 bold'), value=2, text="Deactivate", bg=bg_color, command=deactivate_alarm, variable=selected)
    rad2.place(x=187, y=95)

def alarm():
    while True:
        control = selected.get()  # Get the value of the selected variable
        print(control)
        alarm_hour = c_hour.get()  # Get the selected hour
        alarm_minute = c_min.get()  # Get the selected minute
        alarm_sec = c_sec.get()  # Get the selected second
        alarm_period = c_period.get()  # Get the selected period (AM/PM)
        alarm_period = str(alarm_period).upper()  # Convert the period to uppercase
        
        now = datetime.now()  # Get the current datetime
        
        hour = now.strftime("%I")  # Get the current hour
        minute = now.strftime("%M")  # Get the current minute
        second = now.strftime("%S")  # Get the current second
        period = now.strftime("%p")  # Get the current period (AM/PM)
        
        if control == 1:
            if alarm_period == period:
                if alarm_hour == hour:
                    if alarm_minute == minute:
                        if alarm_sec == second:
                            print("Time to take a break!")
                            sound_alarm()  # Trigger the alarm sound
        sleep(1)  # Pause for 1 second

mixer.init()  # Initialize the mixer for playing audio
window.mainloop()  # Start the Tkinter event loop
