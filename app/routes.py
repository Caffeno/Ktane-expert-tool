#!/usr/bin/env/ python3

from app import app, db
from flask import flash, make_response, render_template, url_for, redirect, request
from app.forms import simonform, memoryform, mazesform, passwordform, morseform, needyknobform, keypadform, EdgeworkPrepForm, FullEdgeworkForm, wiresform, buttonform, WOFform, wiresequenceform
from app.edgework import Edgework
from pprint import pprint
from app.models import ewmodel
import re
from app.wires import Wires
from app.wiresequence import WireSequence
from app.complexwires import ComplexWires
from app.button import Button
from app.keypad import Keypad
from app.needyknob import NeedyKnob
from app.morse import Morse
from app.simon import Simon
from app.password import Password
from app.WOF import WOF
from app.memory import Memory
from app.mazes import Mazes
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from pathfinding.core.diagonal_movement import DiagonalMovement


@app.route('/edgeprep', methods=['GET', 'POST'])
def edgeworkprep():
    form = EdgeworkPrepForm()
    return render_template('edgeworkprep.html', form=form) 

@app.route('/edgework', methods=['GET', 'POST'])
def fulledgework():
    form = EdgeworkPrepForm()
    if type(form.indicators.data) == str:
        fullform = FullEdgeworkForm(Icount =  form.indicators.data, Pcount = form.plates.data)
    else:
        fullform = FullEdgeworkForm(request.form)
    if fullform.validate_on_submit():
        return redirect(url_for('home'))
    return render_template('fulledgework.html', form=fullform)

@app.route('/strike')
def strike():
   bomb = ewmodel.query.filter_by(serial=request.cookies.get('bomb serial')).first()
   bomb.strikes += 1
   db.session.add(bomb) 
   db.session.commit()
   flash('Strikes incressed to {}'.format(bomb.strikes))
   if bomb.strikes >= 3:
       flash('Woops you blew up')
       return redirect(url_for('edgeworkprep'))
   return redirect(url_for('home'))

@app.route('/index', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        fullewform = FullEdgeworkForm(request.form)
        if fullewform.validate_on_submit() and re.search("[0-9]", fullewform.serial.data[5]):
            bombedgework = Edgework()
            bombedgework.populatefromform(fullewform)
            bombedgework.populatedb()
            page = make_response(render_template('home.html'))
            page.set_cookie('bomb serial', fullewform.serial.data.upper())
            return page
        else:
            flash('Invalid Edgework, please try again')
            return redirect(url_for('edgeworkprep'))
    return render_template("home.html")

@app.route('/wires', methods=['GET', 'POST'])
def wiresm():
    if request.method=='POST':
        form = wiresform(request.form)
        if form.wire1.data != "None" and form.wire2.data != "None" and form.wire3.data != "None":
            sequence = []
            sequence.append(form.wire1.data)
            sequence.append(form.wire2.data)
            sequence.append(form.wire3.data)
            if form.wire4.data != "None":
                sequence.append(form.wire4.data)
                if form.wire5.data != "None":
                    sequence.append(form.wire5.data)
                    if form.wire6.data != "None":
                        sequence.append(form.wire6.data)
            ew = Edgework()
            ew.populatefromdb(request.cookies.get('bomb serial'))
            module = Wires(ew)
            flash(module.run(sequence))
            return redirect(url_for('home'))
        else:
            flash('must have first 3 wires')
    form = wiresform()
    return render_template("wires.html", form=form)

@app.route('/wiresequence', methods=["GET", "POST"])
def wiresequencem():
    if request.method == 'POST':
        form = wiresequenceform(request.form)
        if form.color.data and form.letter.data:
            module = WireSequence()
            pprint(module.cuttables)
            if form.color.data == 'Red':
                print(type(form.hiddenred.data))
                flash(module.run(form.color.data, form.hiddenred.data, form.letter.data))
                form.hiddenred.data = str(int(form.hiddenred.data) + 1)
            elif form.color.data == 'Blue':
                flash(module.run(form.color.data, form.hiddenblue.data, form.letter.data))
                form.hiddenblue.data = str(int(form.hiddenblue.data) + 1)
            elif form.color.data == 'Black':
                flash(module.run(form.color.data, form.hiddenblack.data, form.letter.data))
                form.hiddenblack.data = str(int(form.hiddenblack.data) + 1)
        else:
            flash('select both a color and letter')
        if int(form.hiddenred.data) + int(form.hiddenblue.data) + int(form.hiddenblack.data) > 6:
            flash('select a new module from above when finished')
    else:    
        form = wiresequenceform()
    return render_template('wiresequence.html', form=form)

@app.route('/complexwires')
def complexwiresm():
    ew = Edgework()
    ew.populatefromdb(request.cookies.get('bomb serial'))
    module = ComplexWires(ew)
    tocut = module.run()
    for wire in tocut:
        flash('cut {}'.format(wire))
    return redirect(url_for('home'))

@app.route('/button', methods=['GET', 'POST'])
def buttonm():
    if request.method == 'POST':
        form = buttonform(request.form)
        ew = Edgework()
        ew.populatefromdb(request.cookies.get('bomb serial'))
        module = Button(ew)
        if form.hold.data == 'True':
            flash(module.findrelease(form.light.data))
            return redirect(url_for('home'))
        else:
            response = module.run(form.color.data, form.label.data)
            if response == 'Hold':
                form.hold.data = 'True'
                flash(response)
                return render_template('button.html', form=form)
            else:
                flash(response)
                return redirect(url_for('home'))
    else:
        form = buttonform()
    print(form.hold.data)
    return render_template('button.html', form=form)

@app.route('/keypad', methods=['GET', 'POST'])
def keypadm():
    if request.method == 'POST':
        form = keypadform(request.form)
        if form.symbol1.data and form.symbol2.data and form.symbol3.data and form.symbol4.data:
            symbols = [form.symbol1.data, form.symbol2.data, form.symbol3.data, form.symbol4.data]
            if len(list(dict.fromkeys(symbols))) == 4:
                module = Keypad()
                response = module.run(symbols)
                if response == 'FAIL':
                    flash('Invalid set')
                else:
                    for sym in response:
                        flash(sym[1])
                    return redirect(url_for('home'))
            else:
                flash("Select 4 DIFFERENT Symbols")
        else:
            flash("Select 4 Symbols")
    else:
        form = keypadform()
    return render_template('keypad.html', form=form)

@app.route('/needyknob', methods=['GET', 'POST'])
def needyknobm():
    if request.method=='POST':
        form = needyknobform(request.form)
        rowone = ''
        rowtwo = ''
        if form.light11.data:
            rowone += 'x'
        else:
            rowone += '_'
        if form.light12.data:
            rowone += 'x'
        else:
            rowone += '_'
        if form.light13.data:
            rowone += 'x'
        else:
            rowone += '_'
        if form.light21.data:
            rowtwo += 'x'
        else:
            rowtwo += '_'
        if form.light22.data:
            rowtwo += 'x'
        else:
            rowtwo += '_'
        if form.light23.data:
            rowtwo += 'x'
        else:
            rowtwo += '_'
        module = NeedyKnob()
        response = module.run(rowone, rowtwo)
        flash(response)
        if response == 'INVALID LIGHTS':
            pass
        else:
            return redirect(url_for('home'))
    else:
        form = needyknobform()
    return render_template('needyknob.html', form=form)
    
@app.route('/morse', methods=['GET', 'POST'])
def morsem():
    if request.method == 'POST':
        form = morseform(request.form)
        module = Morse()
        response = module.run(form.text.data)
        flash(response)
        if type(response) == float:
            return redirect(url_for('home'))
    else:
        form = morseform()
    return render_template('morse.html', form=form)

@app.route('/simon', methods=['GET', 'POST'])
def simonm():
    if request.method == 'POST':
        form = simonform(request.form)
        ew = Edgework()
        ew.populatefromdb(request.cookies.get('bomb serial'))
        module = Simon(ew)
        response = module.run(form.flash.data)
        form.sequence.data += response + ','
        colorsequence = form.sequence.data.split(',')
        for color in colorsequence:
            flash(color)
    else:
        form = simonform()
    return render_template('simon.html', form=form)

@app.route('/password', methods=['GET', 'POST'])
def passwordm():
    if request.method == 'POST':
        form = passwordform(request.form)
        if len(list(dict.fromkeys(form.wheel.data))) == 6:
            if form.wheelnumber.data == '1':
                form.oldwheels.data = form.wheel.data
                wheellist = [form.wheel.data]
            else:
                form.oldwheels.data += ','  + form.wheel.data
                wheellist = form.oldwheels.data.split(',')
            module = Password()
            print(wheellist)
            response = module.run(wheellist)
            
            flash(response)
            if response == "Need Another Wheel":
                form.wheelnumber.data = str(1 + int(form.wheelnumber.data))
            elif response == "Invalid Wheel Set":
                return redirect(url_for('passwordm'))
            else:
                return redirect(url_for('home'))
    else:
        form = passwordform()
    return render_template('password.html', form=form)

@app.route('/WOF', methods=['GET', 'POST'])
def WOFm():
    if request.method=='POST':
        form = WOFform(request.form)
        if form.step.data == '0':
            module = WOF()
            response = module.getposition(form.display.data)
            flash(response)
            if response == 'INVALID DISPLAY WORD':
                pass 
            else:
                form.step.data = '1'
        elif form.step.data == '1':
            module = WOF()
            response = module.getlist(form.position.data)
            if response == 'INVALID POSITION WORD':
                pass
            else:
                string = ''
                for word in response:
                    string += word + ', '
                string = string[:len(string) - 2]
                flash(string)
                form.step.data = '0'
        print(form.step.data, type(form.step.data))
    else:
        form = WOFform()
    return render_template('WOF.html', form=form)

@app.route('/memory', methods=['GET', 'POST'])
def memorym():
    if request.method == 'POST':
        form = memoryform(request.form)
        if form.holder.data == "":
            display = int(form.display.data)
            if display > 0 and display < 5:
                module = Memory()
                response = module.run(form.stage.data, form.display.data, form.previousrounds.data)
                if int(form.stage.data) > 2 and response[1] == 'Position':
                    flash(response[0])
                    form.previousrounds.data += str(response[2]) + ',x:'
                    form.stage.data = str(int(form.stage.data) + 1)
                else:
                    flash(response[0])
                    form.missingtype.data = response[1]
                    form.holder.data = str(response[2])
            else:
                flash('Display can only be 1-4')
        else:
            if form.missingtype.data == 'Value':
                value = int(form.missingvalue.data)
                if value < 5 and value > 0:
                    form.previousrounds.data += str(value) + ',' + form.holder.data + ':'
                    form.holder.data = ''
                    form.missingtype.data = ''
                    form.stage.data = str(int(form.stage.data) + 1)
                else:
                    flash("Invalid number")
                    flash("What is actualy the number")
            else:
                value = int(form.missingpos.data)
                if value < 5 and value > 0:
                    form.previousrounds.data += form.holder.data + ',' + str(value) + ':'
                    form.holder.data = ''
                    form.missingtype.data = ''
                    form.stage.data = str(int(form.stage.data) + 1)
                else:
                    flash('Invalid position')
                    flash('what was the actual position')
    else:
        form = memoryform()
    if int(form.stage.data) > 5:
        return redirect(url_for('home'))
    else:
        flash('ROUND ' + form.stage.data)
    return render_template('memory.html', form=form)

@app.route('/mazes', methods=['GET', 'POST'])
def mazesm():
    if request.method != 'POST':
        form = mazesform()
    else:
        form = mazesform(request.form)
        module = Mazes()
        positions = module.parseform(form)
        circle = positions[0] == 'Invalid/No Circle Specified'
        start = positions[1] == 'No Start Specified'
        end =  positions[2] == 'No End Specified'
        if circle:
            flash(positions[0])
        if start:
            flash(positions[1])
        if end:
            flash(positions[2])
        if not start and not circle and not end:
            response = module.run(positions[0], positions[1], positions[2])
            for move in response:
                flash(move)
            return redirect(url_for('home'))
    return render_template('mazes.html', form=form)





@app.route('/test', methods=['GET', 'POST'])
def testroute():
    return 'test'
