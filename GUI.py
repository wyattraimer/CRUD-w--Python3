import tkinter as tk

def button_clicked():
    global outputArea
    global txtId
    # print("Button was clicked!")
    outputArea.delete(1.0, tk.END)
    outputArea.insert(tk.END, "Button was Clicked\n" + txtId.get(1.0,tk.END))

def showLocations():
    # print("Data would be here")
    # deletes top text?
    outputArea.delete(1.0, tk.END)
    # puts specific text at bottom of text area
    outputArea.insert(tk.END, "Data would be here\n")

root = tk.Tk()
root.title("Button Example")
root.geometry("400x600")

button = tk.Button(root, text="Click Me!", command=button_clicked)
showButton = tk.Button(root, text="Show Locations", command=showLocations)
outputArea = tk.Text(root, height=10, width=40)
labelId = tk.Label(root, text="Input Id")
txtId = tk.Text(root, height=1)

items = ["Wyatt", "was", "here"]
var = tk.StringVar()
var.set(items)
label2Id = tk.Label(root, text="Drop Down Demo")
lb=tk.Listbox(root, listvariable=var)


button.pack(pady=2)
showButton.pack(pady=2)
outputArea.pack(pady=2)
labelId.pack(pady=2)
txtId.pack(pady=2)
label2Id.pack(pady=2)
lb.pack(pady=2)

root.mainloop()