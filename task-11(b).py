import tkinter as tk
from datetime import datetime

def update_time():
    current_time = datetime.now().strftime("%H:%M:%S")
    time_label.config(text=current_time)
    time_label.after(1000, update_time)

root = tk.Tk()
root.title("Digital Clock")

style = "calibri"
size = 40
font_style = (style, size, "bold")

time_label = tk.Label(root, font=font_style, anchor="center", background='purple', foreground='white')
time_label.pack(fill=tk.BOTH, expand=True)

update_time()
root.mainloop()
