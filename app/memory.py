#!/usr/bin/env python3

class Memory:
    positionstring = 'press the button in the {} position'
    valuestring = 'press the button labled {}'
    positions = [None, 'first', 'second', 'third', 'fourth']
    
    def press(self, value, string):
        if string == 'number':
            return [self.valuestring.format(value), 'Position', value]
        elif string == 'position':
            return [self.positionstring.format(self.positions[value]), 'Value', value]

    def round1(self, display):
        print('ROUND 1')
        if display == 1:
            value = 2
        else:
            value = display
        button = 'position'
        answer = self.press(value, 'position')
        return answer

    def round2(self, display, stored):
        print('ROUND 2')
        if display == 1:
            value = 4
            button = 'number'
        elif display == 2 or display == 4:
            value = int(stored[1][1])
            button = 'position'
        elif display == 3:
            value = 1
            button = 'position'
        answer = self.press(value, button)
        return answer

    def round3(self, display, stored):
        print('ROUND 3')
        if display == 1:
            value = int(stored[2][0])
            button = 'number'
        elif display == 2:
            value = int(stored[1][0])
            button = 'number'
        elif display == 3:
            value = 3
            button = 'position'
        elif display == 4:
            value = 4
            button = 'number'
        answer = self.press(value, button)
        return answer

    def round4(self, display, stored):
        print('ROUND 4')
        button = 'position'
        if display == 1:
            value = int(stored[1][1])
        elif display == 2:
            value = 1
        elif display == 3 or display == 4:
            value = int(stored[2][1])
        answer = self.press(value, button)
        return answer

    def round5(self, display, stored):
        print('ROUND 5')
        button = 'number'
        if display == 1 or display == 2:
            value = stored[display][0]
        elif display == 3:
            value = int(stored[4][0])
        elif display == 4: 
            value = int(stored[3][0])
        answer = self.press(value, button)
        return answer

    def run(self, stage, display, previousrounds):
        roundbreakdown = previousrounds.split(':')
        stored = [None]
        for r in roundbreakdown:
            stagedata = r.split(',')
            stored.append(stagedata)
        if stage == '1':
            answer = self.round1(display)
        elif stage == '2':
            answer = self.round2(display, stored)
        elif stage == '3':
            answer = self.round3(display, stored)
        elif stage == '4':
            answer = self.round4(display, stored)
        elif stage == '5':
            answer = self.round5(display, stored)
        return answer

if __name__ == "__main__":
    test = Memory()
    test.module()
