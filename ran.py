import tkinter as tk
from tkinter import messagebox
import requests


















'''
response = requests.get("https://sugoku.herokuapp.com/board?difficulty=easy")
print("requests:", response)
grid = response.json()['board']
print("grid:", grid)
grid_original = [[grid[x][y] for y in range(len(grid[0]))] for x in range(len(grid))]
print("Grid orginal:", grid_original)


import tkinter as tk
from tkinter import messagebox
#check to see if the number repeats 
def check(x,y, number):
    ctr = 0
    for i in range(9):
        if number == board[x][i] or number == board[i][y] :
            ctr += 1
    if ctr == 0:
        board[x][y] = number
        print(board)
    else:
        tk.messagebox.showerror("ERROR", "This number cannot be added here")
            

board = [[1,6,9],[4,0,9],[4,0,8]]
x,y = 1,1
number = 6
check(x,y,number)
'''

        
        