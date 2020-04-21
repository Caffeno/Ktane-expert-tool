#!/usr/bin/env python3

import yaml

class NeedyKnob:
    def __init__(self):
        f = open('data/needyknoblights.yaml', 'r')
        self.lightpositions = yaml.load(f, Loader = yaml.FullLoader)['lightpositions']
        print(self.lightpositions)

    def run(self):
        print('use x and _ for on and off')
        firstrow = input('what are the first 3 lights in the first row\n')
        secondrow = input('what are the first 3 lights in the second row\n')
        print(self.lightpositions[firstrow + ',' + secondrow])


if __name__ == "__main__":
    test = NeedyKnob()
    test.run()
