#!/usr/bin/env python3

import yaml

class Keypad:
    columns = []
    
    def __init__(self):
        f = open('data/keypadsymbols.yaml', 'r')
        yamlcolumns = yaml.load(f, Loader = yaml.FullLoader)['keypadcolumns']
        for column in yamlcolumns:
            self.columns.append(yamlcolumns[column])

    def run(self):
       symbols = []  
       for x in range(4):
           symbol = input('Symbol {} \n'.format(x + 1))
           symbols.append(symbol)
       column = self.findcolumn(symbols)
       orderedsymbols = self.findorder(symbols, column)
       print('The solution is:')
       for symbol in orderedsymbols:
           print(symbol[1])

    def findcolumn(self, symbols):
        for column in self.columns:
            count = 0
            for symbol in symbols:
                count += column.count(symbol)
            if count == 4:
                break
        return column

    def findorder(self, symbols, column):
        symbolsbyindex = []
        for symbol in symbols:
            index = column.index(symbol)
            symbolsbyindex.append([index, symbol])
        symbolsbyindex.sort()
        return symbolsbyindex
        

if __name__ == "__main__":
    test = Keypad()
    test.run()
