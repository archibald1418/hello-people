# -*- coding: utf-8 -*-
"""
Created on Wed May 16 20:03:34 2018

@author: oleg
"""


# utf-8, Oleg Valiulin, 15.05.2018

from math import sin, cos

'''Game of Life'''

from collections import Counter
import time

import numpy as np

import random


'''

PRESETS:
    
    1 - GLIDER
    2 - BEACON
    3 - BLINKER
    4 - RPENTAMINO
    5 - SPACESHIP

'''

def glider(y0, x0): # From the uppermost
    
    y1, x1 = y0 + 1, x0 + 1
    y2, x2 = y1 + 1, x1
    y3, x3 = y2, x2 - 1
    y4, x4 = y3, x3 - 1
    
    return [(y0, x0), (y1, x1), (y2, x2),(y3, x3),(y4, x4)]

def beacon (y0, x0): # From the leftmost
    
    y1, x1 = y0, x0 + 1
    y2, x2 = x1, y1 - 1
    y3, x3 = y2 + 2, x2 - 3 
    y4, x4 = y3 + 1, x3
    y5, x5 = y3, x3 + 1
    
    return [(y0, x0), (y1, x1), (y2, x2), (y3, x3), (y4, x4), (y5, x5)]
  
def blinker (y0, x0): # From the left lowest
    
    y1, x1 = y0 + 1, x0
    y2, x2 = y1 + 1, x1

    return [(y0, x0), (y1, x1), (y2, x2)]

def rpentamino (y0, x0): # From the lowest
    
    y1, x1 = y0 - 1, x0
    y2, x2 = y1, x1 - 1
    y3, x3 = y2 - 1, x2 + 1
    y4, x4 = y3, x3 + 1

    return [(y0, x0),(y1, x1), (y2, x2), (y3, x3), (y4, x4)]

def spaceship (y0, x0): # From the right upper corner
    
    y1, x1 = y0 + 2, x0
    y2, x2 = y1 + 1, x1 - 1
    y3, x3 = y2, x2 - 1 
    y4, x4 = y3, x3 - 1
    y5, x5 = y4, x4 - 1
    y6, x6 = y5 - 1, x5
    y7, x7 = y6 - 1, x6
    y8, x8 = y7 - 1, x7 + 1
    
    return [(y0,x0),(y1,x1),(y2,x2),(y3,x3),(y4,x4),(y5,x5),(y6,x6),(y7,x7),(y8,x8)]

def square (y0,x0): # From the leftmost angle
    
    side = int(input("Side of the square?: "))
    return [(i, j) for i in range(y0, y0 + side + 1) for j in range(x0, x0 + side + 1)]

def triangle (y0, x0):
    '''Equilateral'''
    
    base = int(input("Length of the base?: "))
    
    b = base // 2
    
    return [(i, j) for i in range(y0, y0 + b + 1) for j in range(x0 - abs(i - y0), x0 + abs(i - y0) + 1)]

def full ():
    return [(i, j) for j in range(m) for i in range(n - j)]  

def glider ():
    pass
   
    
def generator (q):
    return ((random.randrange(n), random.randrange(m)) for i in range(q))

def show ():
    '''Show the field'''
    s = '+ ' * (m + 2) + '\n'
    for i in range(n):
        s += '+ '
        for j in range(m):
            s += (field[i][j] + ' ')
        s += '+\n'
    s += '+ ' * (m + 2) + '\n'
    return s


def look_around (cell: tuple):
    '''Return subjacent cells'''
    '''n x n array'''
    
    y, x = cell
    
    radius = [(yi, xi)  for xi in [x - 1, x, x + 1] 
                        for yi in [y - 1, y, y + 1]
                        if ((m > xi > 0 and n > yi > 0) and
                            (x != xi or y != yi) and
                            (0 < xi < m and 0 < yi < n))]
                        # 3^2 вариантов минус вариант xi==x yi==y (исх. коорд)
                        # С учетом краёв. ЛЮБЫХ.
    
    return cell, radius
 

def born (cell):
    field[cell] = '*'

def die (cell):
    field[cell] = ' '
       
def check_environment (cell:tuple, neighbors:list, copy):
    '''Check the population around the neighbors of a cell'''
            
    environment = Counter ([copy[c] for c in neighbors])
    alive = environment['*']
    
    if copy[cell] == '*':
        if not 2 <= alive <= 3:
            die(cell) 
        
    elif copy[cell] == ' ':
        if alive == 3:
            born(cell)

def config (arg=None):
    '''Set configurations'''
    
    if callable(arg): # If user wants a shape
        cells = arg(*map(int, input('Give starting coords y0, x0: ').split()))
        s = input('You can put more: ')
        i = 0
        while s != '':
            if s.isdigit():
                y0, x0 = s.split()
                cells.extend(arg(int(y0), int(x0)))
                s = input('And more: ')
            if i > 2:
                s = input("Try a generator to help you. Type 'gen'\n")
            if s == 'gen':
                num = int(input('Generate how many shapes?: '))
                for cell in generator(num):
                    y, x = cell
                    cells.extend(arg(y, x))
                s = input("You can press Enter if it's enough")
            i += 1
    else:
        cells = [(15,15), (16,15),(17,15),(15,16),(16,14)] # CUSTOM CELLS
    
    cells = list(filter(lambda p: p[0] < n and p[1] < m, cells)) # Защита от дурака
    
    for c in cells:
        field[c] = '*'
        

def check_config ():
    '''Select configurations for the game'''
    
    options = {'1':glider,
               '2':beacon,
               '3':blinker,
               '4':rpentamino, 
               '5':spaceship,
               '6':square,     # New
               '7':triangle,   # New
               '8':full,
               '9':glider}
    
    output = ['{} -- {}'.format(k, v.__name__.capitalize()) for k, v in options.items()]
    
    print('Input one of the configs',
          'Press Enter otherwise',
          *output, sep = '\n')
    
    num = input()
    
    while num != '':
        arg = options[num] if num in options.keys() else None
        config(arg)
        num = input('You can put more configs if you want: \n')
        # Arg may be there, check defenition
    
    print(show())
    
    s = input('Press Enter if config is OK. If not type "stop": ')
    
    if 'stop' not in s.lower():
        start (field)
    else:
        print ("Come back when you've finished!")

def start (field):
    '''Play the game'''
    k = 0
    s = show()
    print(s)
    prev_s = ''
    print()
    try:
        while ('*' in s) and (prev_s != s): # Все умрут или все зациклится
            copy = field.copy()
            for i in range(n):
                for j in range(m):
                    cell = i, j
                    check_environment(*look_around(cell), copy)
            print(s)
            time.sleep(0.2)
            prev_s = s
            s = show()
            k += 1
    except KeyboardInterrupt:
        pass
    print(show())
    print("Finished", k, " rounds")



n = 30
m = 70

field = np.array([[' ' for i in range(m)] for j in range(n)])


check_config ()
        
        
    
    
    
    
    
    
