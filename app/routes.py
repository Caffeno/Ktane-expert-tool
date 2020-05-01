#!/usr/bin/env/ python3

from app import app, db
from flask import flash, make_response, render_template, url_for, redirect, request
from app.forms import needyknobform, keypadform, EdgeworkPrepForm, FullEdgeworkForm, wiresform, buttonform, wiresequenceform
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
            flash('select a new module from above when finnished')
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
                answer = module.run(symbols)
                if answer == 'FAIL':
                    flash('Invalid set')
                else:
                    for sym in answer:
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
        answer = module.run(rowone, rowtwo)
        flash(answer)
        if answer == 'INVALID LIGHTS':
            pass
        else:
            return redirect(url_for('home'))
    else:
        form = needyknobform()
    return render_template('needyknob.html', form=form)
    









@app.route('/test', methods=['GET', 'POST'])
def testroute():
    return 'test'
