import tkinter as tk
import tkinter.ttk as ttk
import subprocess
import os,sys
import tkinter.filedialog
from tkinter import filedialog
from tkinter import messagebox
from tkinter import *
import sympy
import re

root = tk.Tk()
root.title("calclate")
root.geometry("300x450")

def click00():
    entry.delete(0,tk.END)
    entry.insert(END,"0")

def click01():
    entry.insert(END, "1")

def click02():
    entry.insert(END, "2")

def click03():
    entry.insert(END, "3")

def click04():
    entry.insert(END, "4")

def click05():
    entry.insert(END, "5")

def click06():
    entry.insert(END, "6")

def click07():
    entry.insert(END, "7")

def click08():
    entry.insert(END, "8")

def click09():
    entry.insert(END, "9")

def get_entry_and_plus():
    global num
    number = entry.get()
    entry.delete(0,tk.END)
    entry.insert(END, "+")
    num = int(number)
    return num

def get_entry_and_minus():
    number = entry.get()
    entry.delete(0,tk.END)
    entry.insert(END, "-")

def get_entry_and_multi():
    number = entry.get()
    entry.delete(0,tk.END)
    entry.insert(END, "x")

def get_entry_and_div():
    number = entry.get()
    entry.delete(0,tk.END)
    entry.insert(END, "÷")

def delete_and_output():
    s = entry.get()
    t = int(s.lstrip('+'))
    entry.delete(0,tk.END)
    plus = num + t
    entry.insert(END, plus)

def delete():
    entry.delete(0,tk.END)

frame1 = ttk.Frame(root)
frame1.grid(column=0, row=4, sticky=tk.NSEW, padx=5, pady=10)

frame2 = ttk.Frame(root)
frame2.grid(column=0, row=3, sticky=tk.NSEW, padx=5, pady=10)

frame3 = ttk.Frame(root)
frame3.grid(column=0, row=2, sticky=tk.NSEW, padx=5, pady=10)

frame4 =ttk.Frame(root)
frame4.grid(column=0, row=1, sticky=tk.NSEW, padx=5, pady=10)

frame5 =ttk.Frame(root)
frame5.grid(column=0, row=5, sticky=tk.NSEW, padx=5, pady=10)

frame6 =ttk.Frame(root)
frame6.grid(column=0, row=6, sticky=tk.NSEW, padx=5, pady=10)

frame7 = ttk.Frame(root)
frame7.grid(column=0, row=7, sticky=tk.NSEW, padx=5, pady=10)

button01 = ttk.Button(frame1, text="1", command=click01)
button01.grid(column=0,row=0)
button02 = ttk.Button(frame1, text="2", command=click02)
button02.grid(column=1,row=0)
button03 = ttk.Button(frame1, text="3", command=click03)
button03.grid(column=2,row=0)
button04 = ttk.Button(frame2, text="4", command=click04)
button04.grid(column=0,row=0)
button05 = ttk.Button(frame2, text="5", command=click05)
button05.grid(column=1,row=0)
button06 =ttk.Button(frame2, text="6", command=click06)
button06.grid(column=2,row=0)
button07 =ttk.Button(frame3, text="7", command=click07)
button07.grid(column=0,row=0)
button08 = ttk.Button(frame3, text="8", command=click08)
button08.grid(column=1,row=0)
button09 = ttk.Button(frame3, text="9", command=click09)
button09.grid(column=2, row=0)
button00 = ttk.Button(frame5, text="0", command=click00)
button00.grid(column=0, row=0)
buttonplus = ttk.Button(frame5, text="+", command=get_entry_and_plus)
buttonplus.grid(column=1, row=0)
buttonminus = ttk.Button(frame5, text="-", command=get_entry_and_minus)
buttonminus.grid(column=2, row=0)
buttonmulti = ttk.Button(frame6, text='x', command=get_entry_and_multi)
buttonmulti.grid(column=0,row=0)
buttondiv = ttk.Button(frame6, text='÷',command=get_entry_and_div)
buttondiv.grid(column=1, row=0)
buttonequal = ttk.Button(frame6, text='=', command=delete_and_output)
buttonequal.grid(column=2, row=0)
buttondelete = ttk.Button(frame7, text ='delete', command=delete)
buttondelete.grid(column=0, row=0)

entry = ttk.Entry(frame4)
entry.grid(column=0, row=0)





root.mainloop()
