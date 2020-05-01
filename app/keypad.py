#!/usr/bin/env python3

import yaml

class Keypad:
    columns = []
    
    def __init__(self):
        f = open('app/data/keypadsymbols.yaml', 'r')
        yamlcolumns = yaml.load(f, Loader = yaml.FullLoader)['keypadcolumns']
        for column in yamlcolumns:
            self.columns.append(yamlcolumns[column])

    def run(self, symbols):
       column = self.findcolumn(symbols)
       if column == 'FAIL':
           return column
       else:
           orderedsymbols = self.findorder(symbols, column)
           return orderedsymbols

    def findcolumn(self, symbols):
        for column in self.columns:
            count = 0
            for symbol in symbols:
                count += column.count(symbol)
            if count == 4:
                break
        print(column)
        print(symbols)
        print(count)
        if count != 4:
            column = 'FAIL'
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
