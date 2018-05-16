#!/usr/bin/python3
"""
Python3 implementation of Langton's Loops
Copyright (C) 2018 Romain Fontaine <contact@romainfontaine.com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
import numpy as np
from termcolor import colored
from time import sleep

from rules import rules

def display():
	colors = ["grey", "blue", "red", "green", "yellow","white","cyan","white"]
	for i in range(SIZE_H):
		for j in range(SIZE_W):
			print(colored(grid[i,j],colors[grid[i,j]]), end=" ")
		print("")

def new_value(i, j):
	c = str(grid[i, j])
	a = [str(grid[i-1, j]), str(grid[i, j+1]), str(grid[i+1, j]), str(grid[i, j-1])]
	for i in range(4): # Try every rotation of this array: [TOP, RIGHT, BOTTOM, LEFT]
		try:
			return rules["".join([c, a[i%4], a[(i+1)%4], a[(i+2)%4], a[(i+3)%4]])]
		except KeyError:
			pass
	return grid[i, j] # if no rule is found, return the previous value

def iterate(new_grid):
	for i in range(1, SIZE_H-1):
		for j in range(1, SIZE_W-1):
			new_grid[i,j]=new_value(i, j)
	return new_grid, grid
 
def initialize():
	init_pattern = ["02222222200000",
			"21701401420000",
			"20222222020000",
			"27200002120000",
			"21200002120000",
			"20200002120000",
			"27200002120000",
			"21222222122222",
			"20710710711111",
			"02222222222222"]
	for i, line in enumerate(init_pattern):
		for j, char in enumerate(line):
			grid[i+int(SIZE_H/2)-5, j+int(SIZE_W/2)-7] = int(char)

SIZE_H = 46
SIZE_W = 83

grid = np.zeros((SIZE_H, SIZE_W), dtype="int")
new_grid = np.zeros((SIZE_H, SIZE_W), dtype="int")
initialize()
while True:
	grid, new_grid = iterate(new_grid) # Iterate & swap the two grids
	sleep(.1)
	display()
