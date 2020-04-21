#!/usr/bin/env python3

import yaml

class WOF:
    
    display = {}
    display['YES'] = 'ML'
    display['FIRST'] = 'TR'
    display['DISPLAY'] = 'BL'
    display['OKAY'] = 'TR'
    display['SAYS'] = 'BR'
    display['NOTHING'] = 'ML'
    display[''] = 'BR'
    display['BLANK'] = 'MR'
    display['NO'] = 'BR'
    display['LED'] = 'ML'
    display['LEAD'] = 'BR'
    display['READ'] = 'MR'
    display['RED'] = 'MR'
    display['REED'] = 'BL'
    display['LEED'] = 'BL'
    display['HOLD ON'] = 'BR'
    display['YOU'] = 'MR'
    display['YOU ARE'] = 'BR'
    display['YOUR'] = 'MR'
    display["YOU'RE"] = 'MR'
    display['UR'] = 'TL'
    display['THERE'] = 'BR'
    display["THEY'RE"] = 'BL'
    display['THEIR'] = 'MR'
    display['THEY ARE'] = 'ML'
    display['SEE'] = 'BR'
    display['C'] = 'TR'
    display['CEE'] = 'BR'
    positionwords = {}
    positionwords['T'] = 'top'
    positionwords['M'] = 'middle'
    positionwords['B'] = 'botton'
    positionwords['R'] = 'right'
    positionwords['L'] = 'left'

    def __init__(self):
        f = open('data/WOFwords.yaml', 'r')
        self.wordlists = yaml.load(f, Loader=yaml.FullLoader)['wordlists']

    def run(self):
        while True:
            shownword = input('whats on the display'.upper() + '\n').upper()
            position = self.display[shownword]
            listword = input('What is in the {} {} position'.format(self.positionwords[position[0]], self.positionwords[position[1]]) + '\n').upper()
            self.printlist(listword)

    def printlist(self, word):
        for entry in self.wordlists[word]:
            print(entry)
            x = input('Input anything if word was found')
            if x != '':
                break


if __name__ == "__main__":
    test = WOF()
    test.run()
