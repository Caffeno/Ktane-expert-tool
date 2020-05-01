#!/usr/bin/env/ python3

from password import Password
from edgework import Edgework
from wires import Wires
from complexwires import ComplexWires
from wiresequence import WireSequence
from keypad import Keypad
from mazes import Mazes
from needyknob import NeedyKnob
from button import Button
from password import Password
from WOF import WOF
from memory import Memory
from morse import Morse
from simon import Simon

class Bomb:
    def __init__(self):
        self.edgework = Edgework()
    
    def callmodule(self):
        moduleinput = input("what module is next")
        if moduleinput == "wires":
            module = Wires(self.edgework)
        elif moduleinput == "complex wires":
            module = ComplexWires(self.edgework)
        elif moduleinput == "wire sequence":
            module = WireSequence()
        elif moduleinput == "keypad":
            module = Keypad()
        elif moduleinput == "mazes":
            module = Mazes()
        elif moduleinput == "needy knob":
            module = NeedyKnob()
        elif moduleinput == "button":
            module = Button(self.edgework)
        elif moduleinput == "password":
            module = Password()
        elif moduleinput == "WOF" or module == "whos on first":
            module = WOF()
        elif moduleinput == "memory":
            module = Memory()
        elif moduleinput == "morse":
            module = Morse()
        elif moduleinput == "simon":
            module = Simon(self.edgework)
        else:
            moduleinput = 'fail'
            print('input a valid module')
        if moduleinput != 'fail':
            module.run()

    def addstrike(self):
        self.edgework.strikes += 1
