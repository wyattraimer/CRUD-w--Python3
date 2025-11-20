import tkinter as tk
import sys
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from DBHousing import getCorrData, scatterData, fields

def doPlot(axs,canvas,field1,field2):
    cData=getCorrData(field1,field2)
    scatterData(field1,field2,axs)
    axs.set_xlabel(field1)
    axs.set_ylabel(field2)
    canvas.draw()

def OurClose():
    root.destroy()
    sys.exit()

# Create the main window
root = tk.Tk()

fig, axs = plt.subplots(1,1)

canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.

root.title("DB Housing GUI")
root.geometry("300x600") # Set window size
root.grid_columnconfigure(0, weight=1, uniform='col')
root.grid_columnconfigure(1, weight=1, uniform='col')

label1Id = tk.Label(root,text="Field 1 Choice:")
selected1=tk.StringVar(value="-")
field1=tk.OptionMenu(root,selected1 , *fields)

label2Id = tk.Label(root,text="Field 2 Choice:")
selected2=tk.StringVar(value="-")
field2=tk.OptionMenu(root,selected2 , *fields)

button = tk.Button(root, text="Plot", command=lambda: doPlot( \
    axs, \
    canvas, \
    selected1.get(), \
    selected2.get()))

button.grid(row=0,column=0,columnspan=2,sticky="ew")

label1Id.grid(row=1,column=0)
field1.grid(row=1,column=1,stick="ew")

label2Id.grid(row=2,column=0)
field2.grid(row=2,column=1,stick="ew")

canvas.get_tk_widget().grid(row=3,column=0,columnspan=2)
root.protocol("WM_DELETE_WINDOW", OurClose)
# Start the Tkinter event loop
root.mainloop()
