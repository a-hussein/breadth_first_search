# shortest path finder walkthrough along with 'tech with tim'

import curses
from curses import wrapper
import queue
from re import S
import time
import math

maze = [
    ["#", "O", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
]

def print_maze(maze, stdscr, path=[]):
    blue = curses.color_pair(1)
    white = curses.color_pair(2)
    
    for i, row, in enumerate(maze):
        for j, value in enumerate(row):
            if (i,j) in path:
                stdscr.addstr(i, j*2, "X", blue)
            else:
                stdscr.addstr(i, j*2, value, white)
            
          
# breadth-search-first alg

def find_start(maze, start):
    for i,row in enumerate(maze):
        for j, value in enumerate(row):
            if value == start:
                return i,j   
    return None
             
def find_path(maze, stdscr):
    start = "O"
    end = "X"
    start_pos = find_start(maze, start)
    
    q = queue.Queue()
    # this will allow us to see the path (path) up to each point
    q.put((start_pos, [start_pos]))
    
    visited = set()
    while not q.empty():   # while the set is not empty
        current_pos, path = q.get()
        row, col = current_pos
        
        # add these 3 lines so that we can see the path every while loop iter
        stdscr.clear()
        print_maze(maze, stdscr, path)
        time.sleep(0.07)
        stdscr.refresh()      
          
        #start processing all neighbors if they are not the end node
        if maze[row][col] == end:
            return path

        neighbors = find_neighbors(maze, row, col)
        for neighbor in neighbors:
            if neighbor in visited:
                continue
            
            r, c = neighbor
            if maze[r][c] == "#":
                continue
            
            new_path = path + [neighbor]
            q.put((neighbor, new_path))
            visited.add(neighbor)
        
def find_neighbors(maze, row, col):
    neighbors = []
    
    if row > 0: # UP
        neighbors.append((row - 1, col))
    if row + 1 < len(maze): # DOWN
        neighbors.append((row + 1, col))          
    if col > 0: # LEFT
        neighbors.append((row, col - 1))  
    if col + 1 < len(maze[0]): # RIGHT
        neighbors.append((row, col + 1))     
             
    return neighbors

# use wrapper on main to see maze in termna
def main(stdscr):
    #initiate colors
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)

    stdscr.clear()
    # the below line will add the third paramter in the coordinates preceeding it
    # so, simply call the function to print the maze
    # stdscr.addstr(5,0,"hello")
    print_maze(maze, stdscr)
    stdscr.refresh()
    
    find_path(maze, stdscr)
    # this enables the code to not quit unless you type a letter
    stdscr.getch()

wrapper(main)
 


# Notes
## Queue - first in, first out

# Outline
## start with main and call 'find_path'
## find start by looping through all rows columns and looking at values 'find_start'
## create queue and keep track of all elements you visited
## the idea is to look at all neighbors and check if end node


