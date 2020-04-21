#!/usr/bin/env python3


class Edgework:
    portplates = []
    batteries = {}
    indicators = []

    def __init__(self):
        self.serial = input('What is the seiral number? \n').upper()
        self.addplates()
        self.addbatteries()
        self.addindicators()
        self.strikes = 0
        
    def addplates(self):
        numberofplates = input('How many port plates are there? \n')
        for i in range(int(numberofplates)):
            plate = []
            port = ''
            print('plate start, enter f to finnish the plate')
            while port != 'f':
                port = input("next port \n")
                if port != 'f':
                    plate.append(port)
            self.portplates.append(plate)

    def addbatteries(self): 
        numberofbatteries = input('How many batteries are there? \n')
        numberofbatteryholders = input('How many battery holders are there? \n')
        AA = 2 * (int(numberofbatteries) - int(numberofbatteryholders))
        D = int(numberofbatteries) - AA
        self.batteries['AA'] = AA
        self.batteries['D'] = D
    
    def addindicators(self):
        count = int(input('How many indicators are there? \n'))
        for x in range(count):
            light = input('Lit or unlit, 1/0? \n')
            lable = input("What's the label? \n").upper()
            self.indicators.append([int(light), lable])


if __name__ == "__main__":
    test = Edgework()
    print(test.batteries, test.portplates, test.indicators, test.serial)
