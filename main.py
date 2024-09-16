import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
from typing import *
from PIL import *  # Import PIL for image resizing
from googletrans import Translator,LANGUAGES

def change(text="type",src="English",dest="Hindi"):
    text1=text
    src1=src
    dest1=dest
    trans= Translator()
    trans1 = trans.translate(text,src1,dest1)
    return trans1.text

def data():
    s = combobox_destination.get()
    d = combobox_source.get()
    masg = source_txt.get(1.0,END)
    textget = change(text=masg,src=s,dest=d)
    destination_txt.delete(1.0,END)
    destination_txt.insert(END,textget)

# Create the main window
root = tk.Tk()
root.title("CodeAlpha_Language_Translator_Tool")

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set the geometry of the window to the screen size
root.geometry(f"{screen_width}x{screen_height}")

# Create and place the "Translator" label in the center horizontally
translator_label = tk.Label(root, text="Translator", font=("Times New Roman", 40, "bold"),bg='#ffffe6')
translator_label.place(relx=0.5, rely=0.1, anchor='n')

# Set the background color of the window
root.config(bg='#ffffe6')
# Create a frame at the bottom of the window
frame = Frame(root, bg='#ffffe6',height=600)
frame.pack(side=BOTTOM, fill='x')

enter_text_label = tk.Label(root, text="Enter Text:", font=("Times New Roman", 20, "bold"),bg='#ffffe6')
enter_text_label .place(x=200, y=100,width=300, height=150)

# Create the Text widget and place it 20 pixels below the label
source_txt = tk.Text(root, font=("Times New Roman", 20, "bold"), wrap=WORD)
source_txt.place(x=screen_width // 2 - 500, y=screen_height // 4 + 10, height=160, width=1080)

# Define the list of values for the Combobox
list_text = list(LANGUAGES.values())

# Calculate the y-coordinate for the Combobox (7 pixels below the Text widget)
combobox_y = 140 + 20 + 7  # y-coordinate of Text widget + height + 7 pixels

# Create and place the Combobox widget
combobox_source = ttk.Combobox(frame, values=list_text)  # Use ttk.Combobox
combobox_source.place(x=490, y=combobox_y, height=40, width=150)  # Place it 7 pixels below the Text widget
combobox_source.set("Choose Language")
        
 
button_change = Button(frame,text="Translate",relief=RAISED,command=data)  
button_change.place(x=720, y=combobox_y, height=40, width=150)           

combobox_destination = ttk.Combobox(frame, values=list_text)  # Use ttk.Combobox
combobox_destination.place(x=950, y=combobox_y, height=40, width=150)  # Place it 7 pixels below the Text widget
combobox_destination.set("Choose Language")

translation_label = tk.Label(root, text="Translation:", font=("Times New Roman", 20, "bold"),bg='#ffffe6')
translation_label .place(x=200, y=screen_height// 4+240,width=300, height=150)

destination_txt = tk.Text(root, font=("Times New Roman", 20, "bold"), wrap=WORD)
destination_txt.place(x=screen_width // 2 - 500, y=screen_height // 4 + 350, height=160, width=1080)

root.mainloop()
