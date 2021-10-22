#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 15:35:47 2021

@author: jiechi
"""

import tkinter
import tkinter.font as font
import numpy as np 


#generate sudoku game
main = tkinter.Tk()
main.title('sudoku game')
main.geometry('2500x2000')
btn_fonts = font.Font(family='Helvetica', size=30, weight='bold')
entry_fonts = font.Font(family='Helvetica', size=20, weight='bold')


entries = []

bg_i = 0
color_i = 0
entry_colors = ['azure', 'palegreen', 'thistle', 'lavender', 'mistyrose', 'lightcyan', 'peachpuff', 'cornflowerblue','whitesmoke']

for a in range(0, 1800, 200):
    for b in range(0, 1800, 200):
        if bg_i == 0:
            color = entry_colors[color_i]
        elif bg_i % 27 == 0:
            color_i += 1
            color = entry_colors[color_i]
        elif bg_i % 9 == 0:
            color_i -= 2
            color = entry_colors[color_i]
        elif bg_i % 3 == 0:
            color_i += 1
            color = entry_colors[color_i]
        else:
            color = entry_colors[color_i]         
        temp = tkinter.Entry(main,font = entry_fonts,justify="center",bg=color)
        temp.place(x=b, y=a, width=200, height=200)
        entries.append(temp)
        bg_i += 1
        
def get_entries():
    
    values = []
    for entry in entries:
        values.append (entry.get() or -1)
    return np.array(values).astype(np.int).reshape(9,9)

def find_empty_cell(values, i=0, j=0):
    
    for x in range(i,9):
        for y in range(j,9):
            # print(values)
            # print(values[x][y])
            if values[x][y] < 0:
                return (x,y)
    return (10,10)
def check_cell_valid(values, i, j, num):
    #check row
    if all([num != values[i][k] for k in range(9)]):
        if all([num != values[k][j] for k in range(9)]):
            for x in range(i//3*3,i//3*3+3):
                for y in range(j//3*3,j//3+3):
                    if num == values[x][y]:
                        return False
            return True
    return False
            

def sudoku_solver(values= 'NULL',mode = 'naive'):
    if values == 'NULL':
        values = get_entries()
    if mode == 'naive':
        i,j = find_empty_cell(values)
        if i==10 and j ==10:
            return (True,values)
        for num in range(1,10):
            if check_cell_valid(values,i,j,num):
                values[i][j]=num
                if sudoku_solver(mode='naive',values=values)[0]:
                    return (True,values)
                
                values[i][j]=-1
        return (False,values)
                
        
        
        # print(values)
def fill_table(res):
    
    for i,entry in enumerate(entries):
        entry.delete(0,tkinter.END)
        entry.insert(0,res[i])
    

def sudoku_main(values= 'NULL',mode = 'naive'):
    boolres, res = sudoku_solver(values= 'NULL',mode = 'naive')
    if boolres:
        fill_table(res.flatten())
    else:
        print('no solution')
        


def random_generator():
    test_sample = [4, -1, 2, -1, -1, -1, 7, -1, -1,
                   -1, 7, -1, -1, 2, -1, 8, -1, -1, 
                   -1, 6, -1, 4, 5, 7, -1, -1, -1,
                   2, 5, -1, 9, -1, -1, -1, -1, -1, 
                   -1, 1 ,-1, -1, -1, -1,-1, 7, -1,
                   -1, -1, -1, -1, -1, 2, -1, 5, 3,
                   -1, -1, -1, 7, 6, 3, -1, 1, -1,
                   -1, -1, 1, -1, 8, -1, -1, 3, -1,
                   -1, -1, 7, -1, -1, -1, 4, -1, 8]
    for i,entry in enumerate(entries):
        entry.delete(0,tkinter.END)
        if test_sample[i] > 0:
            entry.insert(0,test_sample[i])


def reset():
    for i,entry in enumerate(entries):
        entry.delete(0,tkinter.END)


rand_btn = tkinter.Button(main,
                    text="Random",
                    bg='#0052cc', fg='#ffffff',
                    command=random_generator,
                    font = btn_fonts)
rand_btn.place(x=2100, y=500,width=250, height=200)


sol_btn = tkinter.Button(main,
                    text="Solve",
                    bg='#0052cc', fg='#ffffff',
                    command=sudoku_main,
                    font = btn_fonts)
sol_btn.place(x=2100, y=1000,width=250, height=200)

reset_btn = tkinter.Button(main,
                    text="Reset",
                    bg='#0052cc', fg='#ffffff',
                    command=reset,
                    font = btn_fonts)
reset_btn.place(x=2100, y=1500,width=250, height=200)

main.mainloop()
