#!/usr/bin/env python3
from pprint import pprint

class ComplexWires:

    def __init__(self, edgework):
        self.evenserial = False
        if int(edgework.serial[len(edgework.serial) - 1]) % 2 == 0:
            self.evenserial = True
        self.batteries = edgework.batteries['AA'] + edgework.batteries['D']
        self.parallelport = False
        for plate in edgework.portplates:
            pprint(plate)
            for port in plate:
                if port == 'parallel':
                    self.parallelport = True

    def run(self):
        wirestocut = ['white', 'white Star', 'red Star']
        if self.evenserial:
            wirestocut.extend(['red', 'blue', 'red & blue', 'red & blue LED'])
        if self.batteries >= 2:
            wirestocut.extend(['LED Star', 'red LED Star', 'red LED'])
        if self.parallelport:
            wirestocut.extend(['red & blue Star', 'blue LED', 'blue LED Star'])
        return wirestocut

if __name__ == "__main__":
    edge = Edgework()
    test = ComplexWires(edge)
    test.run()
    
    
