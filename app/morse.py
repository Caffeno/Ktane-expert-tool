#!/usr/bin/env python3

import morse_talk as mtalk
import yaml

class Morse:
    
    #TODO: make it possible to find code using partial words
    def __init__(self):
        f = open('app/data/morsetable.yaml', 'r')
        self.wordcodes = yaml.load(f, Loader = yaml.FullLoader)['wordcodes']
            
    def run(self, text):
        if text[0] == '.' or text[0] == '-':
            morseword = mtalk.decode(text)
            if morseword.lower() in self.wordcodes.keys():
                return self.wordcodes[morseword.lower()]
            else:
                return 'INVALID MORSE WORD'
        else:
            if text in self.wordcodes.keys():
                return self.wordcodes[text]
            else:
                return 'INVALID WORD'


if __name__ == "__main__":
    k = morse()
    k.run()
