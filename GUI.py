import tkinter as tk

def button_clicked():
    print("Button was clicked!")

root = tk.Tk()
root.title("Button Example")
root.geometry("300x200")

button = tk.Button(root, text="Click Me!", command=button_clicked)

button.pack(pady=50)

root.mainloop()