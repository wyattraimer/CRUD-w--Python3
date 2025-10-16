import tkinter as tk
from DB import *

def actualAddToDB(values,win):
    # need to pass a tuple to putLocation()
    putLocation(values)
    outputLocations()
    win.destroy()

def actualUpdateDB(values, win): # values is a tuple wher 0 is Id, 1 is X, etc.
    d={"id":values[0]}
    if len(values[1])>0:
        d["x"]=values[1]
    if len(values[2])>0:
        d["y"]=values[2]
    putChange(d)
    outputLocations()
    win.destroy()

def add_clicked():
    global root
    addWin=tk.Toplevel(root)
    addWin.geometry("600x300")
    addWin.grid_columnconfigure(0, weight=1, uniform="col")
    addWin.grid_columnconfigure(1, weight=1, uniform="col")
    lblX=tk.Label(addWin,text="X Value")
    txtX=tk.Scale(addWin, from_=0.0, to=100.0, orient=tk.HORIZONTAL)
    lblY=tk.Label(addWin,text="Y Value")
    txtY=tk.Scale(addWin, from_=0.0, to=100.0, orient=tk.HORIZONTAL)
    addButton = tk.Button(addWin, text="Add", command=lambda : actualAddToDB((
        txtX.get(),txtY.get()),addWin)
        )
    cancelButton = tk.Button(addWin, text="Cancel", command=lambda : addWin.destroy())
    lblX.grid(row=0,column=0)
    txtX.grid(row=0,column=1, sticky="ew")
    lblY.grid(row=1,column=0)
    txtY.grid(row=1,column=1, sticky="ew")
    addButton.grid(row=3,column=0)
    cancelButton.grid(row=3,column=1)
    addWin.transient(root)
    addWin.wait_visibility()
    addWin.grab_set()
    addWin.wait_window()

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

def update_clicked():
    global root
    updWin=tk.Toplevel(root)
    updWin.geometry("600x300")
    updWin.grid_columnconfigure(0, weight=1, uniform="col")
    updWin.grid_columnconfigure(1, weight=1, uniform="col")
    lblId=tk.Label(updWin,text="Update Id")
    txtId=tk.Text(updWin, height=1)
    lblX=tk.Label(updWin,text="X Value")
    txtX=tk.Text(updWin, height=1)
    lblY=tk.Label(updWin,text="Y Value")
    txtY=tk.Text(updWin, height=1)
    updButton = tk.Button(updWin, text="Update", command=lambda : actualUpdateDB((txtId.get(1.0,tk.END),txtX.get(1.0,tk.END),txtY.get(1.0,tk.END)),updWin))
    cancelButton = tk.Button(updWin, text="Cancel", command=lambda : updWin.destroy())
    lblId.grid(row=0,column=0)
    txtId.grid(row=0,column=1)
    lblX.grid(row=1,column=0)
    txtX.grid(row=1,column=1)
    lblY.grid(row=2,column=0)
    txtY.grid(row=2,column=1)
    updButton.grid(row=3,column=0)
    cancelButton.grid(row=3,column=1)
    updWin.transient(root)
    updWin.wait_visibility()
    updWin.grab_set()
    updWin.wait_window()

def outputLocations():
    global outputArea
    # goes to db query and gives locations
    locations=getLocations()
    outputArea.delete(1.0, tk.END)
    outputArea.insert(tk.END,"ID\t X\t Y\n")
    for location in locations:
        id=location[0]
        x=location[1]
        y=location[2]
        outputArea.insert(tk.END, f"{id}\t {x}\t {y}\n")

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
saveButton = tk.Button(root, text="Save Changes", command=commitChanges)
outputArea = tk.Text(root, height=10, width=40)

addButton.grid(row=5,column=0)
updateButton.grid(row=5,column=1)
deleteButton.grid(row=5,column=2)
saveButton.grid(row=5,column=3)
outputArea.grid(row=0,column=0,columnspan=2,rowspan=5,sticky="ew")
outputLocations()

root.mainloop()