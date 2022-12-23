import pygame
import requests
import tkinter as tk
from tkinter import messagebox


WIDTH = 550
background_colour = (251,247,245)
original_grid_element_colour = (52,31,150)
buffer = 5

response = requests.get("https://sugoku.herokuapp.com/board?difficulty=medium")
grid = response.json()['board']
grid_original = [[grid[x][y] for y in range(len(grid[0]))] for x in range(len(grid))]

def insert(win, position):
    i,j = position[1], position[0]
    # i-row, j-column
    myfont = pygame.font.SysFont('Comic Sans MS', 35)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if(grid_original[i-1][j-1] != 0): #tries to edit original file
                    return
                if(event.key == 48): #checking with 0
                    grid[i-1][j-1] = event.key - 48
                    pygame.draw.rect(win, background_colour, (position[0]*50 + buffer, position[1]*50+ buffer, 50 -2*buffer, 50 - 2*buffer))
                    pygame.display.update()
                    return
                if(0 < event.key - 48 <10): #we are checking for valid input
                    pygame.draw.rect(win, background_colour, (position[0]*50 + buffer, position[1]*50+ buffer,50 -2*buffer, 50 -2*buffer))
                    #checks
                    ctr1 = 0
                    ctr2 = 0
                    number = event.key - 48
                    for k in range(9): #check for repetition row and column
                        if number == grid[i-1][k] or number == grid[k][j-1] :
                            ctr1 += 1
                            break
                    
                    #check for repetition box
                    row = i-1
                    column = j-1
                    l1 = [0,1,2]
                    l2 = [3,4,5]
                    l3 = [6,7,8]
                    if row in l1 and column in l1: #box 1,1
                        for a in range(3):
                            for b in range(3):
                                if grid[a][b] == number:
                                    ctr2 += 1
                                    break
                    if row in l1 and column in l2:
                        for a in range(3):
                            for b in range(3,6):
                                if grid[a][b] == number:
                                    ctr2 += 1
                                    break
                    if row in l1 and column in l3:
                        for a in range(3):
                            for b in range(6,9):
                                if grid[a][b] == number:
                                    ctr2 += 1
                                    break
                    if row in l2 and column in l1:
                        for a in range(3,6):
                            for b in range(3):
                                if grid[a][b] == number:
                                    ctr2 += 1
                                    break
                    if row in l2 and column in l2:
                        for a in range(3,6):
                            for b in range(3,6):
                                if grid[a][b] == number:
                                    ctr2 += 1
                                    break
                    if row in l2 and column in l3:
                        for a in range(3,6):
                            for b in range(6,9):
                                if grid[a][b] == number:
                                    ctr2 += 1
                                    break
                    if row in l3 and column in l1:
                        for a in range(6,9):
                            for b in range(3):
                                if grid[a][b] == number:
                                    ctr2 += 1
                                    break
                    if row in l3 and column in l2:
                        for a in range(6,9):
                            for b in range(3,6):
                                if grid[a][b] == number:
                                    ctr2 += 1
                                    break
                    if row in l3 and column in l3:
                        for a in range(6,9):
                            for b in range(6,9):
                                if grid[a][b] == number:
                                    ctr2 += 1
                                    break
                    
                    #final checks to print either the number or the error message
                    if ctr1 == 0 and ctr2 == 0:
                        grid[i-1][j-1] = event.key - 48
                        value = myfont.render(str(event.key-48), True, (0,0,0))
                        win.blit(value, (position[0]*50 +15, position[1]*50))
                        pygame.display.update()
                    else:
                        tk.messagebox.showerror("ERROR", "This number cannot be added here")
                        pygame.draw.rect(win, background_colour, (position[0]*50 + buffer, position[1]*50+ buffer,50 -2*buffer, 50 -2*buffer))
                        pygame.display.update()
                return
            return
                    

def main():
      pygame.init()
      win = pygame.display.set_mode((WIDTH,WIDTH))
      pygame.display.set_caption("Sudoku")
      win.fill(background_colour)
      myfont = pygame.font.SysFont('Comic Sans MS',35)
      
      for i in range(0,10):
          if(i%3 == 0):
              pygame.draw.line(win, (0,0,0), (50+50*i,50), (50+50*i,500), 4)
              pygame.draw.line(win, (0,0,0), (50,50+50*i), (500,50+50*i), 4)
              
          pygame.draw.line(win, (0,0,0), (50+50*i,50), (50+50*i,500), 2)
          pygame.draw.line(win, (0,0,0), (50,50+50*i), (500,50+50*i), 2)
      pygame.display.update()

      for i in range(0, len(grid[0])):
          for j in range(0, len(grid[0])):
              if(0<grid[i][j]<10):
                  value = myfont.render(str(grid[i][j]),True, original_grid_element_colour)
                  win.blit(value, ((j+1)*50+15, (i+1)*50))
      pygame.display.update()
      
      while True:
          for event in pygame.event.get():
              if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                  pos = pygame.mouse.get_pos()
                  insert(win, (pos[0]//50, pos[1]//50))
              if event.type == pygame.QUIT:
                   pygame.quit()
                   return
               
main()

