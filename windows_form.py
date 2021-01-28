import tkinter as tk
from tkinter import ttk
win=tk.Tk()
win.title('WinForm')

#create labels
# my_label = tk.Label(win, text="Hello", font=("Arial Bold", 70))
name_label=tk.Label(win, text='Enter your name : ', font=("Arial Bold", 25))
name_label.grid(row=0,column=0, sticky=tk.W)

age_label=ttk.Label(win, text='Enter your age : ', font=("Arial Bold", 25))
age_label.grid(row=1,column=0, sticky=tk.W)

school_label=ttk.Label(win, text='Enter your school : ', font=("Arial Bold", 25))
school_label.grid(row=2,column=0, sticky=tk.W)

#create empty box
name_box=ttk.Entry(win, width=16 ,font=('Arial Bold', 25))
name_box.grid(row=0,column=1)

age_box=ttk.Entry(win, width=16, font=("Arial Bold", 25))
age_box.grid(row=1,column=1)

school_box=ttk.Entry(win, width=16, font=("Arial Bold", 25))
school_box.grid(row=2,column=1)

button_save=ttk.Button(win)

win.mainloop()


# import tkinter as tk
# parent = tk.Tk()
# parent.title("-Welcome to Python tkinter Basic exercises-")
# my_label = tk.Label(parent, text="Hello", font=("Arial Bold", 70))
# my_label.grid(column=0, row=0)
# parent.mainloop()