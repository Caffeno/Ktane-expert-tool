#!/usr/bin/env python3

from pprint import pprint
from app import db
from app.models import ewmodel, indicatormodel, platemodel

class Edgework:
    portplates = []
    batteries = {}
    indicators = []

    def populatefromform(self, fullewform):
        pprint(fullewform.data)
        self.serial = fullewform.serial.data.upper()
        self.addplatesfromform(fullewform)
        self.addbatteries(fullewform.batteries.data, fullewform.holders.data)
        self.addindicatorsfromform(fullewform)
        self.strikes = 0
        
    def populatefromdb(self, bomb_serial):
        self.serial = bomb_serial
        bomb = ewmodel.query.filter_by(serial=bomb_serial).first()
        self.addbatteries(bomb.batteries, bomb.holders)
        for plate in bomb.plates:
            p = []
            if plate.RJ:
                p.append('RJ-45')
            if plate.PS2:
                p.append('PS2')
            if plate.DVI:
                p.append('DVI-D')
            if plate.RCA:
                p.append('Sterio RCA')
            if plate.parallel:
                p.append('Parallel')
            if plate.serial:
                p.append('Serial')
            self.portplates.append(p)
        for ind in bomb.indicators:
            self.indicators.append([ind.light, ind.label])        
        self.strikes = bomb.strikes

    def populatedb(self):
        dbew = ewmodel(serial=self.serial, batteries=(self.batteries['AA']+self.batteries['D']), holders=(self.batteries['D']+self.batteries['AA']/2), strikes=self.strikes)
        db.session.add(dbew)
        db.session.commit()
        for plate in self.portplates:
            PS2 = True if plate.count('PS2') == 1 else False
            RJ  = True if plate.count('RJ-45') == 1 else False
            DVI = True if plate.count('DVI-D') == 1 else False
            RCA = True if plate.count('Sterio RCA') == 1 else False
            parallel = True if plate.count('Parallel') == 1 else False
            serialp = True if plate.count('Serial') == 1 else False
            dbplate = platemodel(PS2=PS2, RJ=RJ, DVI=DVI, RCA=RCA, parallel=parallel, serial=serialp, bomb_id=dbew.id)
            db.session.add(dbplate)
            db.session.commit()
        for ind in self.indicators:
            light = ind[0]
            label = ind[1]
            dbind = indicatormodel(light=light, label=label, bomb_id=dbew.id)
            db.session.add(dbind)
            db.session.commit()

    def addplatesfromform(self, fullewform):
        numberofplates = int(fullewform.Pcount.data)
            
        if numberofplates >= 1:
            plate1 = []
            if fullewform.PS21.data:
                plate1.append('PS2')
            if fullewform.DVI1.data:
                plate1.append('DVI')
            if fullewform.RJ1.data:
                plate1.append('RJ-45')
            if fullewform.RCA1.data:
                plate1.append('Sterio RCA')
            if fullewform.parallel1.data:
                plate1.append('Parallel')
            if fullewform.serial1.data:
                plate1.append('Serial')
            self.portplates.append(plate1)

        if numberofplates >= 2:
            plate2 = []
            if fullewform.PS22.data:
                plate2.append('PS2')
            if fullewform.DVI2.data:
                plate2.append('DVI')
            if fullewform.RJ2.data:
                plate2.append('RJ-45')
            if fullewform.RCA2.data:
                plate2.append('Sterio RCA')
            if fullewform.parallel2.data:
                plate2.append('Parallel')
            if fullewform.serial2.data:
                plate2.append('Serial')
            self.portplates.append(plate2)

        if numberofplates >= 3:
            plate3 = []
            if fullewform.PS23.data:
                plate3.append('PS2')
            if fullewform.DVI3.data:
                plate3.append('DVI')
            if fullewform.RJ3.data:
                plate3.append('RJ-45')
            if fullewform.RCA3.data:
                plate3.append('Sterio RCA')
            if fullewform.parallel3.data:
                plate3.append('Parallel')
            if fullewform.serial3.data:
                plate3.append('Serial')
            self.portplates.append(plate3)
    
        if numberofplates >= 4:
            plate4 = []
            if fullewform.PS24.data:
                plate4.append('PS2')
            if fullewform.DVI4.data:
                plate4.append('DVI')
            if fullewform.RJ4.data:
                plate4.append('RJ-45')
            if fullewform.RCA4.data:
                plate4.append('Sterio RCA')
            if fullewform.parallel4.data:
                plate4.append('Parallel')
            if fullewform.serial4.data:
                plate4.append('Serial')
            self.portplates.append(plate4)
    
        if numberofplates >= 5:
            plate5 = []
            if fullewform.PS25.data:
                plate5.append('PS2')
            if fullewform.DVI5.data:
                plate5.append('DVI')
            if fullewform.RJ5.data:
                plate5.append('RJ-45')
            if fullewform.RCA5.data:
                plate5.append('Sterio RCA')
            if fullewform.parallel5.data:
                plate5.append('Parallel')
            if fullewform.serial5.data:
                plate5.append('Serial')
            self.portplates.append(plate5)
    
       
    def addbatteries(self, batterycount, holdercount): 
        AA = 2 * (int(batterycount) - int(holdercount))
        D = int(batterycount) - AA
        self.batteries['AA'] = AA
        self.batteries['D'] = D
    
    def addindicatorsfromform(self, fullewform):
        count = int(fullewform.Icount.data)
        if count >= 1:
            ind1 = [fullewform.light1.data, fullewform.label1.data]
            self.indicators.append(ind1)
        if count >= 2:
            ind2 = [fullewform.light2.data, fullewform.label2.data]
            self.indicators.append(ind2)
        if count >= 3:
            ind3 = [fullewform.light3.data, fullewform.label3.data]
            self.indicators.append(ind3)
        if count >= 4:
            ind4 = [fullewform.light4.data, fullewform.label4.data]
            self.indicators.append(ind4)
        if count >= 5:
            ind5 = [fullewform.light5.data, fullewform.label5.data]
            self.indicators.append(ind5)
         
if __name__ == "__main__":
    test = Edgework()
    print(test.batteries, test.portplates, test.indicators, test.serial)
