#!/usr/bin/env python3

class Wires:
    position_words = ['Last', 'First' , 'Second', 'Third', 'Fourth', 'Fifth', 'sixth']
    result = 'Cut the {} wire'

    def __init__(self, edgework):
        self.oddserial = False
        if int(edgework.serial[5]) % 2 == 1:
            self.oddserial = True

    def run(self, wiresequence):
        answer  = self.solve(wiresequence)
        return answer

    def getwires(self):
        posiotion = 1
        sequence = []
        while posiotion < 7:
            if posiotion > 3:
                prompt = '{} Wire, or P to process'
            else:
                prompt = '{} Wire'
            entry = input(format(self.position_words[posiotion]) + '\n')
            entry.lower()
            if entry == 'r'or entry == 'red':
                sequence.append('r')
            elif entry == 'w' or entry == 'white':
                sequence.append('w')
            elif entry == 'u' or entry == 'blue':
                sequence.append('u')
            elif entry == 'b' or entry == 'black':
                sequence.append('b')
            elif entry == 'y' or entry == 'yellow':
                sequence.append('y')
            elif entry == 'p' or entry == 'process' and position > 3:
                break
            else:
                print('Enter a valid color (red, white, blue, black, yellow)')
                posiotion -= 1
            posiotion += 1
        return sequence
    
    def solve(self, wiresequence):
        wirecount = len(wiresequence)
        if wirecount == 3:
            return self.solve3(wiresequence)
        elif wirecount == 4:
            return self.solve4(wiresequence)
        elif wirecount == 5:
            return self.solve5(wiresequence)
        elif wirecount == 6:
            return self.solve6(wiresequence)

    def solve3(self, wiresequence):
        if wiresequence.count('r') == 0:
            return self.result.format(self.position_words[2])
        elif wiresequence[2] == 'w':
            return self.result.format(self.position_words[3])
        elif wiresequence.count('u') > 1:
            return self.result.format('last blue')
        else:
            return self.result.format('last')

    def solve4(self, wiresequence):
        reds = wiresequence.count('r')
        if reds > 1 and self.oddserial:
            return self.result.format('last red')
        elif wiresequence[3] == 'y' and reds == 0:
            return self.result.format(self.position_words[1])
        elif wiresequence.count('b') == 1:
            return self.result.format(self.position_words[1])
        elif wiresequence.count('y') >  1:
            return self.result.format(self.position_words[0])
        else:
            return self.result.format(self.position_words[2])

    def solve5(self, wiresequence):
        if wiresequence[4] == 'b' and self.oddserial:
            return self.result.format(self.position_words[4])
        elif wiresequence.count('r') == 1 and wiresequence.count('y') > 1:
            return self.result.format(self.position_words[1])
        elif wiresequence.count('b') == 0:
            return self.result.format(self.position_words[2])
        else:
            return self.result.format(self.position_words[1])

    def solve6(self, wiresequence):
        yellows = wiresequence.count('y')
        if yellows == 0 and self.oddserial:
            return self.result.format(self.position_words[3])
        elif yellows == 1 and wiresequence.count('w'):
            return self.result.format(self.position_words[4])
        elif wiresequence.count('r') == 0:
            return self.result.format(self.position_words[0])
        else:
            return self.result.format(self.position_words[4])


if __name__ == "__main__":
    edge = Edgework()
    test = Wires(edge)
    test.run()
