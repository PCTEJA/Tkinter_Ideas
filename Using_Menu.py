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
        tk.Tk.wm_title(self, 'Demo of Frames')
    #show_frame is used to raise the frame from the windows
    def show_frame(self, cont):
        #cont is the container name of which the frame is called (i.e. frame1 or frame2)
        frame=self.frames[cont]
        frame.tkraise()

#class for the frames, this is the first frame1
class frame1(tk.Frame):
    def __init__(self, parent, controller):
        #importing the partial module from functiontools
        from functools import partial
        tk.Frame.__init__(self, parent)
        # Create a Tkinter variable
        tkvar = StringVar(self)
        Label(self, text='              Opening the frame-2 or frame-3 using months', font=('arial bold', 20)).grid(row=0, column=0, columnspan=2)
        Label(self, text='IF month selected is between One - Seven: Frame-2 Diaplayes', fg='red').grid(row=1, column=0)
        Label(self, text='IF month selected is between Eight - Ten: Frame-3 Diaplayes', fg='blue').grid(row=2, column=0)
        
        # List with options of months
        choices = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        popupMenu = OptionMenu(self, tkvar, *choices)
        Label(self, text="Choose Number", font=("Arial Bold", 20), fg='Red').grid(row = 3, column = 0)
        popupMenu.grid(row = 4, column =0)
        tkvar.set('1') # set the default option
        
        #calling a new window based on the month and the weather type!!
        def type(tkvar):
            global m
            m=tkvar.get()
            choices = ['1', '2', '3', '4', '5', '6', '7']
            choices1=[ '8', '9', '10']
            for month in choices:
                if(m==month):
                    print(m)
                    controller.show_frame(frame2)
                    
                    break
                elif(m==choices1[0]):
                    print(m)
                    controller.show_frame(frame3)
                    
                    break
                elif(m==choices1[1]):
                    print(m)
                    controller.show_frame(frame3)
                    
                    break
                elif(m==choices1[2]):
                    print(m)
                    controller.show_frame(frame3)
                    
                    break
        #giving two parameters
        type=partial(type, tkvar)
        #closing the main loop
        
        def closewin():
            self.destroy()
            #controller.quit_frame(startpage)
            controller.quit_frame(pageone)
            controller.quit_frame(pagetwo)
            
        Button(self, text='QUIT', command=closewin, font=('Arial BOld', 15)).grid(row=5, column=1)

        #Button for the window.
        Button(self, text="Open Frame", command=type, font=("Arial Bold", 20), fg='black', bg="white" ).grid(row=4, column=1)
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
