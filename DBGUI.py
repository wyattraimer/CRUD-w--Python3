import tkinter as tk

def add_clicked():
    global outputArea
    global txtId
    outputArea.delete(1.0, tk.END)
    outputArea.insert(tk.END, "Button was Clicked\n" + txtId.get(1.0,tk.END))

def delete_clicked():
    global outputArea
    global txtId
    outputArea.delete(1.0, tk.END)
    outputArea.insert(tk.END, "Button was Clicked\n" + txtId.get(1.0,tk.END))

def update_clicked():
    global selected
    global outputArea
    # deletes top text?
    outputArea.delete(1.0, tk.END)
    # puts specific text at bottom of text area
    outputArea.insert(tk.END, "Data would be here\n" + selected.get())

def saveChange_clicked():
    global outputArea
    global txtId
    outputArea.delete(1.0, tk.END)
    outputArea.insert(tk.END, "Button was Clicked\n" + txtId.get(1.0,tk.END))

root = tk.Tk()
root.title("Location Data Tool")
root.geometry("600x300")
root.grid_columnconfigure(0, weight=1, uniform="col")
root.grid_columnconfigure(1, weight=1, uniform="col")
root.grid_columnconfigure(2, weight=1, uniform="col")
root.grid_columnconfigure(3, weight=1, uniform="col")

addButton = tk.Button(root, text="Add", command=add_clicked)
deleteButton = tk.Button(root, text="Delete", command=delete_clicked)
updateButton = tk.Button(root, text="Update", command=update_clicked)
saveButton = tk.Button(root, text="Save Changes", command=saveChange_clicked)
outputArea = tk.Text(root, height=10, width=40)

addButton.grid(row=5,column=0)
updateButton.grid(row=5,column=1)
deleteButton.grid(row=5,column=2)
saveButton.grid(row=5,column=3)
outputArea.grid(row=0,column=0,columnspan=2,rowspan=5,sticky="ew")

root.mainloop()