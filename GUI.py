import tkinter as tk

def button_clicked():
    # print("Button was clicked!")
    outputArea.insert(tk.END, "Button was Clicked ")

def showLocations():
    # print("Data would be here")
    outputArea.insert(tk.END, "Data would be here ")

root = tk.Tk()
root.title("Button Example")
root.geometry("400x300")

button = tk.Button(root, text="Click Me!", command=button_clicked)
showButton = tk.Button(root, text="Show Locations", command=showLocations)
outputArea = tk.Text(root, height=10, width=40)


button.pack(pady=2)
showButton.pack(pady=2)
outputArea.pack(pady=2)

root.mainloop()