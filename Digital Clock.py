from tkinter import Tk
from tkinter import Label
import time


def update_clock():
    current_time = time.strftime("%I:%M:%S %p")  # %I for 12 hours format
    clock.configure(text=current_time)
    clock.after(1000, update_clock)


window = Tk()
window.title("Digital Clock")
window.geometry("650x200")
window.config(bg="#232b2b")

clock = Label(window, font=("Orbitron", 60), bg="#232b2b", fg="#f5f7f7",)
clock.pack(fill="both", expand=1)
clock.place(x=325, y=100, anchor="center")

update_clock()
window.mainloop()
