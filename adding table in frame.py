import tkinter as tk
from tkinter import *
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
        #Adding titles for the tkitner frames
        tk.Tk.wm_title(self, 'Demo of Graph')
        #setting up the variable c for the container
        self.c=container
        #frames dictionary is used to raise the frames in the window
        self.frames={}
        #the for loop calls and initialises all the classes when tkinter opens
        for F in (frame1, frame2):    
            frame=F(container, self)
            self.frames[F]=frame
            frame.grid(row=0, column=0, sticky='nsew')
    #the show_frame function used to raise the frame.
    def show_frame(self, cont):
        frame=self.frames[cont]
        frame.tkraise()
# this is the first frame
class frame1(tk.Frame):
#Initializing the frame
    def __init__(self, parent, controller):
    #importing pandas for the data frame
        import pandas as pd
        df=pd.DataFrame({'x_values': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'y_values1' : [2, 3, 5, 2, 1, 9, 4, 2, 1, 3], 'y_values2' : [5, 5, 3, 2, 8, 1, 9, 3, 2, 1]}) 
        tk.Frame.__init__(self, parent)
        #importing the pandas table for the table in the tkinter
        from pandastable import Table, TableModel
        f = Frame(self)
        f.grid(row=2, column=0, columnspan=3)
        #table creation for the frame
        self.table = pt = Table(f, dataframe=df,
        showtoolbar=True, showstatusbar=True)
        #showing the table
        pt.show()
        #Button to go to the second frame
        Button(self, text="Go to the second frame", command=lambda:controller.show_frame(frame2)).pack()
#class for the second frame
class frame2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        lbl=Label(self, text='This is the second frame')
        lbl.pack()
        #Button to go to the first frame
        Button(self, text="Go to the table", command=lambda:controller.show_frame(frame1)).pack()
        
app=main_window()
app.mainloop()
