#!/usr/bin/env python3

import yaml

class Password:
    wordsbyletter = {}
    positions = [None, 'first', 'second', 'third', 'fourth', 'fifth']
 
    def __init__(self):
        letters = 'abcefghlnoprstw'
        
        for letter in letters:
            self.wordsbyletter[letter] = []
        f = open('app/data/passworddict.yaml', 'r')
        wordlist = yaml.load(f, Loader=yaml.FullLoader)['wordlist']
        for word in wordlist:
            self.wordsbyletter[word[0]].append(word)
        
    def wheel(self, number, groups, possibleletters, letters):
        possiblewords = []
        newletters = ''
        for letter in letters:
            if possibleletters.count(letter) > 0:
                for word in groups[letter]:
                    possiblewords.append(word)
                    if number < 5:    
                        newletters += word[number]
        possiblewords.append(newletters)
        return possiblewords
            
    def run(self, wheels):
        avalableletters = 'abcefghlnoprstw'
        row = 1
        wordsbyXletter = self.wordsbyletter
        possible = [None, None]
        for positionletters in wheels:
            possible = self.wheel(row, wordsbyXletter, avalableletters, positionletters)
            avalableletters = possible.pop()
            wordsbyXletter = {}
            for letter in avalableletters:
                wordsbyXletter[letter] = []
            if row < 5:
                for word in possible:
                    wordsbyXletter[word[row]].append(word)
            row += 1
        if len(possible) == 1:
            return possible[0]
        elif len(possible) == 0:
            return 'Invalid Wheel Set'
        else:
            return 'Need Another Wheel'

if __name__ == "__main__":
    test = Password()
    test.run()
