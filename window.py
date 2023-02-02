import tkinter as tk

root = tk.Tk()
root.title("cool window by nik")
root.geometry("200x200")

label = tk.Label(root, text="Hello, users!")
label.pack()

root.mainloop()
