import tkinter as tk

def button_clicked():
    # print("Button was clicked!")
    outputArea.delete(1.0, tk.END)
    outputArea.insert(tk.END, "Button was Clicked\n")

def showLocations():
    # print("Data would be here")
    # deletes top text?
    outputArea.delete(1.0, tk.END)
    # puts specific text at bottom of text area
    outputArea.insert(tk.END, "Data would be here\n")

root = tk.Tk()
root.title("Button Example")
root.geometry("400x300")

button = tk.Button(root, text="Click Me!", command=button_clicked)
showButton = tk.Button(root, text="Show Locations", command=showLocations)
outputArea = tk.Text(root, height=10, width=40)
labelId = tk.Label(root, text="Input Id")
txtId = tk.Text(root)


button.pack(pady=2)
showButton.pack(pady=2)
outputArea.pack(pady=2)
labelId.pack(pady=2)
txtId.pack(pady=2)

root.mainloop()