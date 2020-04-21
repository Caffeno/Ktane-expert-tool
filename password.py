#!/usr/bin/env python3

import yaml

class Password:
    wordsbyletter = {}
    positions = [None, 'first', 'second', 'third', 'fourth', 'fifth']
 
    def __init__(self):
        letters = 'abcefghlnoprstw'
        
        for letter in letters:
            self.wordsbyletter[letter] = []
        f = open('data/passworddict.yaml', 'r')
        wordlist = yaml.load(f, Loader=yaml.FullLoader)['wordlist']
        for word in wordlist:
            self.wordsbyletter[word[0]].append(word)
        
    def wheel(self, number, groups, possibleletters):
        letters = input('letters in {} wheel'.format(self.positions[number]) + '\n')        
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
            
    def run(self):
        avalableletters = 'abcefghlnoprstw'
        row = 1
        wordsbyXletter = self.wordsbyletter
        possible = [None, None]
        while len(possible) > 1:
            possible = self.wheel(row, wordsbyXletter, avalableletters)
            avalableletters = possible.pop()
            wordsbyXletter = {}
            for letter in avalableletters:
                wordsbyXletter[letter] = []
            if row < 5:
                for word in possible:
                    wordsbyXletter[word[row]].append(word)
            row += 1
        print(possible[0])

if __name__ == "__main__":
    test = Password()
    test.run()
