#!/usr/bin/env python3

import yaml

class WireSequence:

    def __init__(self):
        f = open('data/wiresequencetable.yaml', 'r')
        self.cuttables = yaml.load(f, Loader = yaml.FullLoader)
    
    def run(self):
        colorcounts = {}
        colors = {}
        colors['r'] = 'Red'
        colors['b'] = 'Black'
        colors['u'] = 'Blue'
        colorcounts['r'] = 0
        colorcounts['b'] = 0
        colorcounts['u'] = 0
        print('black = b, blue = u, red = r')
        while True:
            query = input('color(c) to letter(l): format "cl" \n')
            print(self.cuttables[colors[query[0]]])
            if self.cuttables[colors[query[0]]][colorcounts[query[0]]].count(query[1].upper()) == 1:
                print('\nYes, cut\n')
            else:
                print('\nNo, do not cut\n')
            colorcounts[query[0]] += 1



