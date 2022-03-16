# tallon.py
#
# The code that defines the behaviour of Tallon. This is the place
# (the only place) where you should write code, using access methods
# from world.py, and using makeMove() to generate the next move.
#
# Written by: Simon Parsons
# AI written by: Mehedi Hassan Rupok (Github: MHRupok)
# Last Modified: 12/01/22

import world
import random
import utils
from utils import Directions
import math
import sys
from collections import deque
import time


class Tallon():

    def __init__(self, arena):

        # Make a copy of the world an attribute, so that Tallon can
        # query the state of the world
        self.gameWorld = arena

        # What moves are possible.
        self.moves = [Directions.NORTH, Directions.SOUTH, Directions.EAST, Directions.WEST]
        
        self.maxX = self.gameWorld.maxX + 1
        self.maxY = self.gameWorld.maxY + 1
        self.pit = 88
        self.meanie = 88
        self.bonus = 77
        self.smelly = 2
        self.tallon = 55
        self.empty = 0
        self.world_map = []
        self.converted_map = []
        self.survive = 0
        self.nextSurvivalLoc = []
        self.start_i, self.start_j = 0,0
        self.end_i, self.end_j = 0,0
        self.path_so_far = []
        self.dfs = []
        self.reset_map()
    
    #Reset game world map positions to zero
    def reset_map(self):
        self.world_map = [ [0]* self.maxX for i in range(self.maxY)]
    
    #For each step it resets map, then update pit locations, bonus along with the meanies movement
    #and update tallons own position in the map
    #considers danger zone
    def update_map(self, pLoc, mLoc, bLoc):
        self.reset_map()
        self.update_pit(pLoc)
        self.update_bonus(bLoc)
        self.update_meanie(mLoc)
        my_position = self.gameWorld.getTallonLocation()
        self.world_map[my_position.y][my_position.x] =  self.tallon
        
    # not considering danger zone
    def update_map_danger(self, pLoc, mLoc, bLoc):
        self.reset_map()
        self.update_pit(pLoc)
        self.update_bonus(bLoc)
        self.update_meanie_danger_zone(mLoc)
        my_position = self.gameWorld.getTallonLocation()
        self.world_map[my_position.y][my_position.x] =  self.tallon
        
    #Search maps and update the pit locations
    def update_pit(self, pitLoc):
        for y in range(self.maxX):
            for x in range(self.maxY):
                for loc in pitLoc:
                    if(x == loc.x and y == loc.y):
                        self.world_map[y][x] = self.pit
    #search meanie locations and update the map    
    #considers danger zone              
    def update_meanie(self, mLoc):
        for y in range(self.maxX):
            for x in range(self.maxY):
                for loc in mLoc:
                    if(x == loc.x and y == loc.y):
                        self.world_map[y][x] = self.meanie
                        if(y+1 < self.maxY and y+1 != self.bonus):
                            self.world_map[y+1][x] = self.meanie
                        if(y-1 > 0 and y-1 != self.bonus):
                            self.world_map[y-1][x] = self.meanie
                        if(x+1 < self.maxX and x+1 != self.bonus):
                            self.world_map[y][x+1] = self.meanie
                        if(x-1 > 0 and x-1 != self.bonus):
                            self.world_map[y][x-1] = self.meanie
                        # if(y+2 < self.maxY and y+2 != self.bonus):
                        #     self.world_map[y+2][x] = self.meanie
                        # if(y-2 > 0 and y-2 != self.bonus):
                        #     self.world_map[y-2][x] = self.meanie
                        # if(x+2 < self.maxX and x+2 != self.bonus):
                        #     self.world_map[y][x+2] = self.meanie
                        # if(x-2 > 0 and x-2 != self.bonus):
                        #     self.world_map[y][x-2] = self.meanie
                        
    #update meanies position not considering the danzer zones
    def update_meanie_danger_zone(self, mLoc):
        for y in range(self.maxX):
            for x in range(self.maxY):
                for loc in mLoc:
                    if(x == loc.x and y == loc.y):
                        self.world_map[y][x] = self.meanie
        
    #search for bonus and update the bons locations in the map
    def update_bonus(self, bLoc):
        for y in range(self.maxX):
            for x in range(self.maxY):
                for loc in bLoc:
                    if(x == loc.x and y == loc.y):
                        self.world_map[y][x] = self.bonus
    
    
               
    def makeMove(self):
        # This is the function you need to define

        # For now we have a placeholder, which always moves Tallon
        # directly towards any existing bonuses. It ignores Meanies
        # and pits.
        # 
        # Get the location of the Bonuses.
        all_bonus = self.gameWorld.getBonusLocation()
        meanie_locations = self.gameWorld.getMeanieLocation()
        pitLocations = self.gameWorld.getPitsLocation()
        self.update_map(pitLocations, meanie_locations,all_bonus)
        my_position = self.gameWorld.getTallonLocation()
        
        #When there are many bonus tallon finds the nearest bonus
        #run bfs to calculate shortest path and navigate to bonus
        #avoiding the meanies
        if(len(all_bonus)>0):
            try:
                pathLen, paths = self.eat_bonus(self.world_map)
                nextMove = paths[1]
                if(nextMove[1]< my_position.x):
                    return Directions.WEST
                elif(nextMove[1]> my_position.x):
                    return Directions.EAST
                elif(nextMove[0] >my_position.y):
                    return Directions.SOUTH
                elif(nextMove[0] <my_position.y):
                    return Directions.NORTH
            except:
                print("Go Danger")
                all_bonus = self.gameWorld.getBonusLocation()
                meanie_locations = self.gameWorld.getMeanieLocation()
                pitLocations = self.gameWorld.getPitsLocation()
                self.update_map_danger(pitLocations,meanie_locations,all_bonus)
                my_position = self.gameWorld.getTallonLocation()
                try:
                    pathLen, paths = self.eat_bonus(self.world_map)
                    nextMove = paths[1]
                    if(nextMove[1]< my_position.x):
                        return Directions.WEST
                    elif(nextMove[1]> my_position.x):
                        return Directions.EAST
                    elif(nextMove[0] >my_position.y):
                        return Directions.SOUTH
                    elif(nextMove[0] <my_position.y):
                        return Directions.NORTH
                except:
                    print("Can't find a path")
                
        #when there are no bonuses then it finds random coordinates where meanies density is less
        if(len(all_bonus)==0):
            loc = self.calculate_next()
            self.world_map[loc[0]][loc[1]] = 77
            try:
                pathLen, paths = self.eat_bonus(self.world_map)
                nextMove = paths[1]
                if(nextMove[1]< my_position.x):
                    return Directions.WEST
                elif(nextMove[1]> my_position.x):
                    return Directions.EAST
                elif(nextMove[0] >my_position.y):
                    return Directions.SOUTH
                elif(nextMove[0] <my_position.y):
                    return Directions.NORTH
            except:
                print("error")
            
    # calculates next random moves for survival
    def calculate_next(self):
        points = []
        ind = 0
        maxH = 0
        for x in range(4):
            while(True):
                newLoc = utils.pickUniquePose(self.maxX-1, self.maxY-1, self.gameWorld.locationList)
                if(self.world_map[newLoc.y][newLoc.x] == 0):
                    points.append([newLoc.x, newLoc.y]) 
                    break

        my_position = self.gameWorld.getTallonLocation()
        for j in range(len(points)):
            temp =self.calc_heuristic([my_position.x, my_position.y], points[j])
            if(temp>maxH):
                maxH = temp
                ind = j
        return points[ind]
            
    #calculates the cost from current position to goal position        
    def calc_heuristic(self,pointA, pointB):
        
        x1 = pointA[0]
        y1 = pointA[1]
        x2 = pointB[0]
        y2 = pointB[1]
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    #dfs to find the longest route
    def go_to(self,i, j, maze):
        a = maze
        if i < 0 or j < 0 or i > len(a)-1 or j > len(a[0])-1:
            return
        if (i, j) in self.path_so_far or a[i][j] > 0:
            return
        self.path_so_far.append((i, j))
        a[i][j] = 2
    
        if (i, j) == (self.end_i, self.end_j):   
            self.dfs = self.path_so_far     
            return self.path_so_far
        else:
            self.go_to(i - 1, j, a)  # check top
            self.go_to(i + 1, j, a)  # check bottom
            self.go_to(i, j + 1, a)  # check right
            self.go_to(i, j - 1, a)  # check left
        self.path_so_far.pop()
        
    #bfs to find the shortest path to bonus
    def eat_bonus(self, maze):
        R, C = len(maze), len(maze[0])
        start = (0, 0)
        for r in range(R):
            for c in range(C):
                if maze[r][c] == self.tallon:
                    start = (r, c)
                    break
            else:
                continue
            break
        else:
            return None
        queue = deque()
        queue.appendleft((start[0], start[1], 0, [start[0] * C + start[1]]))
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visited = [[False] * C for _ in range(R)]

        while len(queue) != 0:
            coord = queue.pop()
            visited[coord[0]][coord[1]] = True

            if maze[coord[0]][coord[1]] == 77:
                return coord[2], [[i//C, i%C] for i in coord[3]] # Return path length, boxes on path

            for dir in directions:
                nr, nc = coord[0] + dir[0], coord[1] + dir[1]
                if (nr < 0 or nr >= R or nc < 0 or nc >= C or maze[nr][nc] == 88 or visited[nr][nc]): continue
                queue.appendleft((nr, nc, coord[2] + 1, coord[3] + [nr * C + nc]))
                
    
    