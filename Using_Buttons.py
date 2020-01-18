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
        #setting up the variable c for the container
        self.c=container
        #making a dictionary for the frames
        #we will set the keys as the frames and value as the frame object
        self.frames={}
        #for loop is present to initialize all the frame at the begining of the algotithm start
        for F in (frame1, frame2, frame3):
            frame=F(container, self)
            self.frames[F]=frame
            frame.grid(row=0, column=0, sticky='nsew')
        self.show_frame(frame1)
        #Adding titles for the tkitner frames
        tk.Tk.wm_title(self, 'Demo of Frames Using Buttons')
    #show_frame is used to raise the frame from the windows
    def show_frame(self, cont):
        #cont is the container name of which the frame is called (i.e. frame1 or frame2)
        frame=self.frames[cont]
        frame.tkraise()

#class for the frames, this is the first frame1
class frame1(tk.Frame):
    #initializing the first class of the frame
    def __init__(self, parent, controller):
        #calling the frames
        tk.Frame.__init__(self, parent)
        #setting a label to be displayed and buttons on the frame
        lbl2=tk.Label(self, text='This is the first frame in the window')
        lbl2.pack()
        #setting the buttons to slide from the frame1 and frame 3
        btn1=tk.Button(self, text='Frame-2', command=lambda : controller.show_frame(frame2))
        btn1.pack()
        btn2=tk.Button(self, text='Frame-3', command=lambda : controller.show_frame(frame3))
        btn2.pack()

#class for the second frame
class frame2(tk.Frame):
    #initializing the second class
    def __init__(self, parent, controller):
        #calling the frames
        tk.Frame.__init__(self, parent)
        #setting a label to be displayed and buttons on the frame
        lbl2=tk.Label(self, text='This is the second frame in the window')
        lbl2.pack()
        #setting the buttons to slide from the frame1 and frame 3
        btn1=tk.Button(self, text='Frame-1', command=lambda : controller.show_frame(frame1))
        btn1.pack()
        btn2=tk.Button(self, text='Frame-3', command=lambda : controller.show_frame(frame3))
        btn2.pack()
class frame3(tk.Frame):
    #initializing the third class
    def __init__(self, parent, controller):
        #calling the frames
        tk.Frame.__init__(self, parent)
        #setting a label to be displayed and buttons on the frame
        lbl2=tk.Label(self, text='This is the third frame in the window')
        lbl2.pack()
        #setting the buttons to slide from the frame1 and frame 2
        btn1=tk.Button(self, text='Frame-1', command=lambda : controller.show_frame(frame1))
        btn1.pack()
        btn2=tk.Button(self, text='Frame-2', command=lambda : controller.show_frame(frame2))
        btn2.pack()
        
#creating an object for the class
app=main_window()
#cloosing the main loop
app.mainloop()
