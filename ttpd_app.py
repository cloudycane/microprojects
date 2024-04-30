import pyautogui
from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.config(background="lightgrey")
root.geometry("800x800")
root.resizable(False, False)
root.title("The Tortured Poets Department")

img = ImageTk.PhotoImage(Image.open("ttpd.png"))
panel = Label(root, image= img)
panel.pack(side= "bottom", fill="both")
panel.config(background="lightgrey")

# TITLE

title = Label(root, text="The Tortured Poets Department", font=("Courier", 20, "bold"))
title.pack(side="top", fill="both")
title.config(background="lightgrey", foreground="darkgrey")

# ENTRIES

name_title = Label(root, text="Name: ", font=("Courier", 15, "normal"))
name_title.pack(side="top")

name_entry_frame = Frame(root, padx=20, pady=20)
name_entry_frame.pack(side="top")
name_entry = Entry(name_entry_frame)
name_entry.pack(side="top")
name_entry_frame.config(background="lightgrey")

position_title = Label(root, text="Position", font=("Courier", 15, "normal"))
position_title.pack(side="top")
position_entry_frame = Frame(root, padx=20, pady=20)
position_entry_frame.pack(side="top")
position_entry = Entry(position_entry_frame)
position_entry.pack(side="top")
position_entry_frame.config(background="lightgrey")

# Message entry

message_entry_frame = Frame(root, padx=100, pady=20)
message_entry_frame.pack(side="top", fill="both")

message_entry = Text(message_entry_frame, height=400, width=400)
message_entry.pack(side="top", fill="both")
message_entry.config(font=("Courier", 35, "italic"))

# Button

def on_key_press(event):
    key_pressed = event.keysym

    if key_pressed == "Shift_R":
        screenshot = pyautogui.screenshot()
        screenshot.save('screenshot.png')

root.bind("<Key>", on_key_press)
root.mainloop()

