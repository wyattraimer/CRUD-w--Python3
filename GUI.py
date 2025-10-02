import tkinter as tk

def button_clicked():
    print("Button was clicked!")

def showLocations():
    print("Data would be here")

root = tk.Tk()
root.title("Button Example")
root.geometry("300x200")

button = tk.Button(root, text="Click Me!", command=button_clicked)
showButton = tk.Button(root, text="Show Locations", command=showLocations)

button.pack(pady=20)
showButton.pack(pady=20)

root.mainloop()