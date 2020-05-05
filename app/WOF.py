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
        f = open('app/data/WOFwords.yaml', 'r')
        self.wordlists = yaml.load(f, Loader=yaml.FullLoader)['wordlists']

    def getposition(self, shownword):
            if shownword in self.display.keys():
                position = self.display[shownword]
                return "{} {}".format(self.positionwords[position[0]], self.positionwords[position[1]])
            else:
                return 'INVALID DISPLAY WORD'

    def getlist(self, word):
        if word in self.wordlists.keys():
            return self.wordlists[word]
        else:
            return 'INVALID POSITION WORD'

if __name__ == "__main__":
    test = WOF()
    test.run()
