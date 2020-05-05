#!/usr/bin/env python3

import yaml
from pprint import pprint
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from pathfinding.core.diagonal_movement import DiagonalMovement


class Mazes:
    mazegrids = {}

    def __init__(self):
        f = open('app/data/mazes.yaml', 'r')
        mazelist = yaml.load(f, Loader = yaml.FullLoader)
        for mazekey in mazelist['mazes']:
            maze = []
            for rawline in mazelist['mazes'][mazekey].splitlines():
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

    def findmaze(self, circle):
        circlelist = circle.split(',')
        return 'maze{}{}'.format(circlelist[0], circlelist[1])
        
    def pathfind(self, maze, rawstart, rawend):
        matrix = maze
        grid = Grid(matrix=matrix)
        start = grid.node(int(rawstart[1]) * 2 - 1, int(rawstart[0]) * 2 - 1)
        end = grid.node(int(rawend[1]) * 2 - 1, int(rawend[0]) * 2 - 1)
        finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
        path, runs = finder.find_path(start, end, grid)
        return path

    def run(self, circle, start, end):
        mazekey = self.findmaze(circle)
        start = start.replace(',', '').replace(' ', '')
        end = end.replace(',', '').replace(' ', '')
        path = self.pathfind(self.mazegrids[mazekey], start, end)
        directions = self.getdirections(path)
        return directions

    def parseform(self, form):
        circle = ''
        if form.circle11.data:
            circle = '1,1'
        elif form.circle21.data:
            circle = '2,1'
        elif form.circle51.data:
            circle = '5,1'
        elif form.circle12.data:
            circle = '1,2'
        elif form.circle42.data:
            circle = '4,2'
        elif form.circle62.data:
            circle = '6,2'
        elif form.circle23.data:
            circle = '2,3'
        elif form.circle43.data:
            circle = '4,3'
        elif form.circle53.data:
            circle = '5,3'
        elif form.circle14.data:
            circle = '1,4'
        elif form.circle44.data:
            circle = '4,4'
        elif form.circle64.data:
            circle = '6,4'
        elif form.circle15.data:
            circle = '1,5'
        elif form.circle25.data:
            circle = '2,5'
        elif form.circle35.data:
            circle = '3,5'
        elif form.circle45.data:
            circle = '4,5'
        elif form.circle36.data:
            circle = '3,6'
        elif form.circle46.data:
            circle = '4,6'
        else:
            circle = "Invalid/No Circle Specified"

        start = ''
        if form.start11.data:
            start = '1,1'
        elif form.start21.data:
            start = '2,1'
        elif form.start31.data:
            start = '3,1'
        elif form.start41.data:
            start = '4,1'
        elif form.start51.data:
            start = '5,1'
        elif form.start61.data:
            start = '6,1'
        elif form.start12.data:
            start = '1,2'
        elif form.start22.data:
            start = '2,2'
        elif form.start32.data:
            start = '3,2'
        elif form.start42.data:
            start = '4,2'
        elif form.start52.data:
            start = '5,2'
        elif form.start62.data:
            start = '6,2'
        elif form.start13.data:
            start = '1,3'
        elif form.start23.data:
            start = '2,3'
        elif form.start33.data:
            start = '3,3'
        elif form.start43.data:
            start = '4,3'
        elif form.start53.data:
            start = '5,3'
        elif form.start63.data:
            start = '6,3'
        elif form.start14.data:
            start = '1,4'
        elif form.start24.data:
            start = '2,4'
        elif form.start34.data:
            start = '3,4'
        elif form.start44.data:
            start = '4,4'
        elif form.start54.data:
            start = '5,4'
        elif form.start64.data:
            start = '6,4'
        elif form.start15.data:
            start = '1,5'
        elif form.start25.data:
            start = '2,5'
        elif form.start35.data:
            start = '3,5'
        elif form.start45.data:
            start = '4,5'
        elif form.start55.data:
            start = '5,5'
        elif form.start65.data:
            start = '6,5'
        elif form.start16.data:
            start = '1,6'
        elif form.start26.data:
            start = '2,6'
        elif form.start36.data:
            start = '3,6'
        elif form.start46.data:
            start = '4,6'
        elif form.start56.data:
            start = '5,6'
        elif form.start66.data:
            start = '6,6'
        else:
            start = "No Start Specified"

        end = ''
        if form.end11.data:
            end = '1,1'
        elif form.end21.data:
            end = '2,1'
        elif form.end31.data:
            end = '3,1'
        elif form.end41.data:
            end = '4,1'
        elif form.end51.data:
            end = '5,1'
        elif form.end61.data:
            end = '6,1'
        elif form.end12.data:
            end = '1,2'
        elif form.end22.data:
            end = '2,2'
        elif form.end32.data:
            end = '3,2'
        elif form.end42.data:
            end = '4,2'
        elif form.end52.data:
            end = '5,2'
        elif form.end62.data:
            end = '6,2'
        elif form.end13.data:
            end = '1,3'
        elif form.end23.data:
            end = '2,3'
        elif form.end33.data:
            end = '3,3'
        elif form.end43.data:
            end = '4,3'
        elif form.end53.data:
            end = '5,3'
        elif form.end63.data:
            end = '6,3'
        elif form.end14.data:
            end = '1,4'
        elif form.end24.data:
            end = '2,4'
        elif form.end34.data:
            end = '3,4'
        elif form.end44.data:
            end = '4,4'
        elif form.end54.data:
            end = '5,4'
        elif form.end64.data:
            end = '6,4'
        elif form.end15.data:
            end = '1,5'
        elif form.end25.data:
            end = '2,5'
        elif form.end35.data:
            end = '3,5'
        elif form.end45.data:
            end = '4,5'
        elif form.end55.data:
            end = '5,5'
        elif form.end65.data:
            end = '6,5'
        elif form.end16.data:
            end = '1,6'
        elif form.end26.data:
            end = '2,6'
        elif form.end36.data:
            end = '3,6'
        elif form.end46.data:
            end = '4,6'
        elif form.end56.data:
            end = '5,6'
        elif form.end66.data:
            end = '6,6'
        else:
            end = "No End Specified"

        return [circle, start, end]




