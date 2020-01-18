import tkinter as tk
from tkinter import *
from matplotlib import style
import matplotlib
matplotlib.use('TkAgg')
style.use('ggplot')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
#creating a tkinter window
class main_window(tk.Tk):
    #initializing the class with arguments and keyword arguments
    def __init__(self, *args, **kwargs):
        #initializing the Tk
        tk.Tk.__init__(self, *args, **kwargs)
        #creating a Frame using variable container
        container = tk.Frame(self)
        #packing the frame inside the window (i.e. main_window)
        container.pack(side="top", fill="both", expand=True)
        #setting up the grid for the frames
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        #setting up the variable c for the container
        self.c=container
        frame=frame1(container, self)
        self.frames={}
        self.frames[frame1]=frame
        frame.grid(row=0, column=0, sticky='nsew')
        #Adding titles for the tkitner frames
        tk.Tk.wm_title(self, 'Demo of Graph')
        #frame is raised at the initialization of the main_window
        frame.tkraise()

#class for the frames, this is the first frame1
class frame1(tk.Frame):
    #initializing the first class of the frame
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        #setting up label for the graph
        Label(self, text="Displaying the Graph", font=('Arial Bold', 20)).pack()
        f=Figure(figsize=(5, 5), dpi=100)
        a=f.add_subplot(111)
        #plotting the x_values in the graph
        x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        #Plotting the lines of the graph
        t0, =a.plot(x, [2, 3, 5, 2, 1, 9, 4, 2, 1, 3], color="red", marker="o", linestyle="-")
        t1, =a.plot(x, [5, 5, 3, 2, 8, 1, 9, 3, 2, 1], color="blue", marker="x", linestyle="-")
       #setting up labels for the graph
        a.set_ylabel('y_scattered')
        a.set_xlabel('x_scattered')
        a.grid()
        #creating the legends for the graph
        f.legend((t0, t1), ('line-1', 'line-2'), 'upper right')
        #creating the canvas for the graph
        canvas=FigureCanvasTkAgg(f, self)
        #drawing the canvas
        canvas.draw()
        canvas.get_tk_widget().pack()
        #creating the navigation tool bar for the graph using matplotlib
        toolbar=NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        #packing the whole canvas with navigation tool bar and the graph diagram
        canvas._tkcanvas.pack()
app=main_window()
app.mainloop()
