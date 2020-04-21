#!/usr/bin/env python3

import morse_talk as mtalk
import yaml

class Morse:

    def __init__(self):
        f = open('data/morsetable.yaml', 'r')
        self.wordcodes = yaml.load(f, Loader = yaml.FullLoader)['wordcodes']
            
    def run(self):
        system = input('input type, morse or text\n')
        if system == 'text':
            word = input('put in the word\n')
            print(self.wordcodes[word])
        else:
            morse = input('input morse string using . and  - \n ')
            word = mtalk.decode(morse)
            print(self.wordcodes[word.lower()])


if __name__ == "__main__":
    k = morse()
    k.run()
