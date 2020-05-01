#!/usr/bin/env python3

import yaml

class NeedyKnob:
    def __init__(self):
        f = open('app/data/needyknoblights.yaml', 'r')
        self.lightpositions = yaml.load(f, Loader = yaml.FullLoader)['lightpositions']

    def run(self, firstrow, secondrow):
        if (firstrow + ',' + secondrow) in self.lightpositions.keys():
            return self.lightpositions[firstrow + ',' + secondrow]
        else:
            return 'INVALID LIGHTS'

if __name__ == "__main__":
    test = NeedyKnob()
    test.run()
