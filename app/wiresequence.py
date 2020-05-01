#!/usr/bin/env python3

import yaml
import pprint
class WireSequence:

    def __init__(self):
        f = open('app/data/wiresequencetable.yaml', 'r')
        self.cuttables = yaml.load(f, Loader = yaml.FullLoader)
    
    def run(self, color, instance, letter):
        if self.cuttables[color][int(instance)].count(letter) == 1:
            return "Yes, cut"
        else:
            return "No, do not cut"



