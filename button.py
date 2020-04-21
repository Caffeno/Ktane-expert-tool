#!/usr/bin/env python3

from edgework import Edgework

class Button:
    lightcolorkey = {}
    lightcolorkey['blue'] = 4
    lightcolorkey['yellow'] = 5
    lightcolorkey['other'] = 1

    def __init__(self, edgework):
        self.batterycount = edgework.batteries['AA'] + edgework.batteries['D']
        self.releventindicators = {}
        self.releventindicators['CAR'] = False
        self.releventindicators['FRK'] = False
        for indicator in edgework.indicators:
            if indicator[0] == 1 and (indicator[1] == 'CAR' or indicator[1] == 'FRK'):
                self.releventindicators[indicator[1]] = True

    def run(self):
        color = input('button color?')
        label = input('button label?')
        action = self.operation(color, label)
        print(action)
        if action == 'hold':
            self.findrelease()

    def findrelease(self):
        lightcolor = input('what color is the light?')
        if lightcolor == 'blue' or lightcolor == 'yellow':
            print('Release on {}'.format(self.lightcolorkey[lightcolor]))
        else:
            print('Release on {}'.format(self.lightcolorkey['other']))

    def operation(self, color, label):
        if color == 'blue' and label == 'abort':
            action = 'hold'
        elif label == 'detonate' and self.batterycount > 1:
            action = 'quick press'
        elif color == 'white' and self.releventindicators['CAR']:
            action = 'hold'
        elif self.batterycount > 2 and self.releventindicators['FRK']:
            action = 'quick press'
        elif color == 'yellow':
            action = 'hold'
        elif color == 'red' and label == 'hold':
            action = 'quick press'
        else:
            action = 'hold'
        return action


if __name__ == "__main__":
    edge = Edgework()
    test = Button(edge)
    test.run()

