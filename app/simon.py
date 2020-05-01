#!/usr/bin/env python3

import yaml
import re
from edgework import Edgework

class Simon:
    table = {}
    strikekeys = ['No Strikes', '1Strike', '2Strike']

    def __init__(self, edgework):
        f = open('data/simontable.yaml', 'r')
        rawtables = yaml.load(f, Loader = yaml.FullLoader)
        self.key = rawtables['key']
        self.table['vowel'] = rawtables['vowel']
        self.table['no vowel'] = rawtables['no vowel']
        self.serialvowel = False
        if re.search("[AEIOU]+", edgework.serial):
            self.serialvowel = True
        self.strikes = edgework.strikes

    def run(self):
        newcolors = self.gettable(self.strikes)
        sequence = []
        done = ''
        while done != 'end':
            response = self.findswap(newcolors)
            done = response
            if done != 'end':
                sequence.append(response)
                print('\ncolor sequence')
                for color in sequence:
                    print(color)

    def findswap(self, newcolors):
        while True:
            flashed = input('\nColor flashed \n')
            if flashed == 'Blue' or flashed == 'Yellow' or flashed == 'Green' or flashed == 'Red':
                response = newcolors[self.key.index(flashed)]
                return response
            elif flashed == 'end':
                return flashed
            else:
                print('input a valid color, Red Green Yellow Blue, capitalized or end')

    def gettable(self, strikes):
        if self.serialvowel:
            colorswaps = self.table['vowel'][self.strikekeys[strikes]] 
        else:
            colorswaps = self.table['no vowel'][self.strikekeys[strikes]] 
        return colorswaps
 
if __name__ == "__main__":
    edge = Edgework()
    test = Simon(edge)
    test.run(edge)
