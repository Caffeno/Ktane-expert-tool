#!/usr/bin/env python3

class Memory:
    positionstring = 'press the button in the {} position'
    valuestring = 'press the button labled {}'
    positions = [None, 'first', 'second', 'third', 'fourth']
    
    def __init__(self):
        self.stored = [None]

    def press(self, value, string):
        if string == 'number':
            print(self.valuestring.format(value) + '\n')
            position = input('what position did you press: \n')
            self.stored.append([value, int(position)])
        elif string == 'position':
            print(self.positionstring.format(self.positions[value]) + '\n')
            number = input('what number did you press: \n')
            self.stored.append([int(number), value])

    def round1(self):
        print('ROUND 1')
        display = input('number displayed: \n')
        if display == '1':
            value = 2
        else:
            value = int(display)
        button = 'position'
        self.press(value, 'position')

    def round2(self):
        print('ROUND 2')
        display = input('number displayed: \n')
        if display == '1':
            value = 4
            button = 'number'
        elif display == '2' or display == '4':
            value = self.stored[1][1]
            button = 'position'
        elif display == '3':
            value = 1
            button = 'position'
        self.press(value, button)

    def round3(self):
        print('ROUND 3')
        display = input('number displayed: \n')
        if display == '1':
            value = self.stored[2][0]
            button = 'number'
        elif display == '2':
            value = self.stored[1][0]
            button = 'number'
        elif display == '3':
            value = 3
            button = 'position'
        elif display == '4':
            value = 4
            button = 'number'
        self.press(value, button)

    def round4(self):
        print('ROUND 4')
        display = input('number displayed: \n')
        button = 'position'
        if display == '1':
            value = self.stored[1][1]
        elif display == '2':
            value = 1
        elif display == '3' or display == '4':
            value = self.stored[2][1]
        self.press(value, button)

    def round5(self):
        print('ROUND 5')
        button = 'number'
        display = input('number displayed: \n')
        if display == '1' or display == '2':
            value = self.stored[int(display)][0]
        elif display == '3':
            value = self.stored[4][0]
        elif display == '4': 
            value = self.stored[3][0]
        self.press(value, button)

    def module(self):
        self.round1()
        print(self.stored)
        self.round2()
        print(self.stored)
        self.round3()
        print(self.stored)
        self.round4()
        print(self.stored)
        self.round5()

if __name__ == "__main__":
    test = Memory()
    test.module()
