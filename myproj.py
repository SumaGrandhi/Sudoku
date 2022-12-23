#tkinter window 
import tkinter as tk
from tkinter import messagebox
#import requests

def window():
    global root
    root = tk.Tk()
    root.title("WELCOME")
    l = tk.Label(root, text = "SUDUKO PUZZLE", height = 4, width=31, bg = "black", fg = "green")
    l.pack()
    b1 = tk.Button(root, text = "QUIT",borderwidth=5,height = 3, width=30,bg = "black", fg = "white", command = quit)
    b1.pack()
    b2 = tk.Button(root, text = "PLAY", width=30, height = 3, borderwidth=5,bg = "black", fg = "white", command = play)
    b2.pack()
    root.mainloop()

def levels():
    global r
    r = tk.Tk()
    label = tk.Label(r, text = "DIFFICULTY LEVELS" ,  height = 4, width=31, bg = "black", fg = "green")    
    label.pack()
    b1 = tk.Button(r, text = "EASY"  ,borderwidth=5,height = 3, width=30,bg = "black", fg = "white", command = easy) 
    b1.pack()
    b2 = tk.Button(r, text = "MEDIUM" ,borderwidth=5,height = 3, width=30,bg = "black", fg = "white", command = medium)
    b2.pack()
    b3 = tk.Button(r, text = "HARD" ,borderwidth=5,height = 3, width=30,bg = "black", fg = "white", command = hard)
    b3.pack()
    r.mainloop()

def easy():
    r.destroy()
    import sudokumain

def medium():
    r.destroy()
    import sudokumain2

def hard():
    r.destroy()
    import sudokumain3

def quit():
    if tk.messagebox.askyesno("Verify","Really Quit?"):
        tk.messagebox.showinfo("Quit", "Goodbye")
        exit()
    else:
        tk.messagebox.showinfo("No", "Good Choice")
        root.destroy()
        window()


def play():
    root.destroy()
    levels()

window()