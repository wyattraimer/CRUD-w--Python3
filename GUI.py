import tkinter as tk

def button_clicked():
    global outputArea
    global txtId
    outputArea.delete(1.0, tk.END)
    outputArea.insert(tk.END, "Button was Clicked\n" + txtId.get(1.0,tk.END))

def showLocations():
    global selected
    global outputArea
    # deletes top text?
    outputArea.delete(1.0, tk.END)
    # puts specific text at bottom of text area
    outputArea.insert(tk.END, "Data would be here\n" + selected.get())

root = tk.Tk()
root.title("Button Example")
root.geometry("400x600")

button = tk.Button(root, text="Click Me!", command=button_clicked)
showButton = tk.Button(root, text="Show Locations", command=showLocations)
outputArea = tk.Text(root, height=10, width=40)
labelId = tk.Label(root, text="Input Id")
txtId = tk.Text(root, height=1)

items = ["--Select--", "Wyatt", "was", "here"]
label2Id = tk.Label(root, text="Drop Down Demo")
selected=tk.StringVar(value="--Select--")
lb=tk.OptionMenu(root, selected, *items)


# button.pack(pady=2)
# showButton.pack(pady=2)
# outputArea.pack(pady=2)
# labelId.pack(pady=2)
# txtId.pack(pady=2)
# label2Id.pack(pady=2)
# lb.pack(pady=2)

button.grid(row=0,column=0)
showButton.grid(row=0,column=1)
outputArea.grid(row=1,column=0,columnspan=2,sticky="ew")
labelId.grid(row=2,column=0)
txtId.grid(row=2,column=1)
label2Id.grid(row=3,column=0)
lb.grid(row=3,column=1)

root.mainloop()