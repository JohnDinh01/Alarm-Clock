import winsound
import tkinter as tk
from tkinter import ttk
from datetime import datetime as dt

root = tk.Tk()
root.title("Clock")

def time():
    now = dt.now()
    s = now.strftime("%I:%M:%S %p")
    label.config(text=s)
    label.after(1000, time)

sound_list = ["alarm", "old car horn", "old phone", "presto", "radar"]

label = tk.Label(root, font=("Times", 80),background="black", foreground="cyan")
label.pack(anchor='center')
time()

while True:
    string = (" do you want your alarm to ring?: ")
    alarmH = int(input("What hour" + string))
    alarmM = int(input("What minute" + string))
    amPm = str(input("am or pm?: "))
    print(*sound_list, sep ="\n")
    alarm_sound = str(input("Choose a alarm sound: "))
 
    if alarmH in range(1, 13) and alarmM in range(0, 60):
        if amPm == "am" or amPm == "pm":
            if alarm_sound in sound_list:
                break
    else:
        print("Invalid entries, please re-enter your alarm time.")

alarm_ring = "Your alarm will ring at:"

print(alarm_ring, alarmH, alarmM, amPm)
if amPm == "pm" and alarmH != 12:
    alarmH += 12
elif alarmH == 12 and amPm == "am":
    alarmH -= 12

while True:
    if (alarmH == dt.now().hour and alarmM == dt.now().minute):
        winsound.PlaySound(alarm_sound, winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)
        end, snooze_time = str(input("'snooze x' for x minute or 'stop alarm'? ")).split()

        if end == "stop":
            winsound.PlaySound(None, 0)
            exit()

        elif end == "snooze":
            winsound.PlaySound(None, 0)
            alarmM = dt.now().minute + int(snooze_time)
            if alarmM >= 60:
                alarmH += 1
                alarmM -= 60

            if alarmH in range(0, 12):
                amPm = "am"
                if alarmH == 12:
                    print(alarm_ring, alarmH + 12, alarmM, amPm)
                else:
                    print(alarm_ring, alarmH, alarmM, amPm)

            elif alarmH in range(13, 24):
                print(alarm_ring, alarmH - 12, alarmM, amPm)

root.mainloop()
