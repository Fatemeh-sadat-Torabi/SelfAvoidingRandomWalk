# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 17:01:38 2022

@author: FARZANE.T
"""

import sys
import random

lattice_size=int(sys.argv[1])
test_itterate=int(sys.argv[2])
lattice=[]
deadEnds=0


for t in range(test_itterate):
    lattice= [[False] * lattice_size for i in range(lattice_size)]
    walker_x = lattice_size // 2
    walker_y = lattice_size // 2
    while 0 < walker_x < lattice_size-1 and 0 < walker_y < lattice_size-1:
        if lattice[walker_x][walker_y+1] and lattice[walker_x][walker_y-1] and lattice[walker_x-1][walker_y] and lattice[walker_x+1][walker_y]:
            deadEnds+=1
            break
        lattice[walker_x][walker_y]= True ## mark it as visitted
        rand = random.randrange(0,4)
        if rand == 0 : 
            if not lattice[walker_x + 1][walker_y] : walker_x = walker_x + 1
        elif rand == 1 :
            if not lattice[walker_x - 1][walker_y] : walker_x = walker_x - 1
        elif rand == 2 : 
            if not lattice[walker_x][walker_y + 1] : walker_y = walker_y + 1
        else:#rand == 3  
            if not lattice[walker_x][walker_y - 1] : walker_y = walker_y - 1
deadEndsProb = deadEnds / test_itterate
print(" Probability of Dead End is : " , 100 * deadEndsProb)
            
            
        
        
            
    