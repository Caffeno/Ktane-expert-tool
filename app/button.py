#!/usr/bin/env python3


class Button:
    lightcolorkey = {}
    lightcolorkey['Blue'] = 4
    lightcolorkey['Yellow'] = 5
    lightcolorkey['Other'] = 1

    def __init__(self, edgework):
        self.batterycount = edgework.batteries['AA'] + edgework.batteries['D']
        self.releventindicators = {}
        self.releventindicators['CAR'] = False
        self.releventindicators['FRK'] = False
        for indicator in edgework.indicators:
            if indicator[0] == 1 and (indicator[1] == 'CAR' or indicator[1] == 'FRK'):
                self.releventindicators[indicator[1]] = True

    def run(self, color, label):
        action = self.operation(color, label)
        return action

    def findrelease(self, lightcolor):
        return 'Release on {}'.format(self.lightcolorkey[lightcolor])

    def operation(self, color, label):
        if color == 'Blue' and label == 'Abort':
            action = 'Hold'
        elif label == 'Detonate' and self.batterycount > 1:
            action = 'Quick Press'
        elif color == 'White' and self.releventindicators['CAR']:
            action = 'Hold'
        elif self.batterycount > 2 and self.releventindicators['FRK']:
            action = 'Quick Press'
        elif color == 'Yellow':
            action = 'Hold'
        elif color == 'Red' and label == 'Hold':
            action = 'Quick Press'
        else:
            action = 'Hold'
        return action


if __name__ == "__main__":
    edge = Edgework()
    test = Button(edge)
    test.run()

