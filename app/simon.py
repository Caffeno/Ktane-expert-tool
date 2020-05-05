#!/usr/bin/env python3

import yaml
import re

class Simon:
    table = {}
    strikekeys = ['No Strikes', '1Strike', '2Strike']

    def __init__(self, edgework):
        f = open('app/data/simontable.yaml', 'r')
        rawtables = yaml.load(f, Loader = yaml.FullLoader)
        self.key = rawtables['key']
        self.table['vowel'] = rawtables['vowel']
        self.table['no vowel'] = rawtables['no vowel']
        self.serialvowel = False
        if re.search("[AEIOU]+", edgework.serial):
            self.serialvowel = True
        self.strikes = edgework.strikes

    def run(self, flashed):
        newcolors = self.gettable(self.strikes)
        return newcolors[self.key.index(flashed)]

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
