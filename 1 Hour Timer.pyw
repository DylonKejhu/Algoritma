import tkinter as tk

root = tk.Tk()
root.title("Timer")
root.geometry("200x70")
root.resizable(False, False)
time_label = tk.Label(root, font=("Helvetica", 24))
time_label.pack(pady=20)

def count(s):
    if s >= 0:
        mins, secs = divmod(s, 60)
        time_label.config(text=f"{mins:02}:{secs:02}")
        root.after(1000, count, s - 1)
    else:
        time_label.config(text="Time's up!")
        
count(8888)

root.mainloop()