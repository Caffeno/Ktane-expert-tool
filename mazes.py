#!/usr/bin/env python3

import yaml
from pprint import pprint
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from pathfinding.core.diagonal_movement import DiagonalMovement


class Mazes:
    mazegrids = {}

    def __init__(self):
        f = open('data/mazes.yaml', 'r')
        mazelist = yaml.load(f, Loader = yaml.FullLoader)
        for mazekey in mazelist['mazes']:
            maze = []
            for rawline in mazelist['mazes'][mazekey].splitlines():
                pprint(rawline)
                line = []
                for character in rawline:
                    if character == '#':
                        line.append(0)
                    else:
                        line.append(1)
                maze.append(line)
            self.mazegrids[mazekey] = maze

    def getdirections(self, path):
        path = path[::2]
        directions = []
        for x in range(1, len(path)):
            if path[x][0] == path[x-1][0] and path[x][1] - path[x - 1][1] < 0:
                directions.append('up')
            elif path[x][0] == path[x-1][0] and path[x][1] - path[x - 1][1] > 0:
                directions.append('down')
            elif path[x][1] == path[x - 1][1] and path[x][0] - path[x - 1][0] < 0:
                directions.append('left')
            elif path[x][1] == path[x - 1][1] and path[x][0] - path[x - 1][0] > 0:
                directions.append('right')
        return directions 

    def findmaze(self):
        circle1 = input('coordinates of first circle').replace(',', '').replace(' ', '')
        circle2 = input('coordinates of second circle').replace(',', '').replace(' ', '')
        circlelist = [[circle1[0], circle1[1]], [circle2[0], circle2[1]]]
        circlelist.sort()
        return 'maze{}{}{}{}'.format(circlelist[0][0], circlelist[0][1], circlelist[1][0], circlelist[1][1])
        
    def pathfind(self, maze, rawstart, rawend):
        matrix = maze
        grid = Grid(matrix=matrix)
        start = grid.node(int(rawstart[1]) * 2 - 1, int(rawstart[0]) * 2 - 1)
        end = grid.node(int(rawend[1]) * 2 - 1, int(rawend[0]) * 2 - 1)
        finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
        path, runs = finder.find_path(start, end, grid)
        print(grid.grid_str(path=path, start=start, end=end))
        return path

    def run(self):
        mazekey = self.findmaze()
        start = input('starting location \n').replace(',', '').replace(' ', '')
        end = input('ending location \n').replace(',', '').replace(' ', '')
        path = self.pathfind(self.mazegrids[mazekey], start, end)
        directions = self.getdirections(path)
        for step in directions:
            print(step)

 
if __name__ == "__main__":
    test = Mazes()
    test.run()

