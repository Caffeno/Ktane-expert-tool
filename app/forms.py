#!/usr/bin/env/ python3

from flask_wtf import FlaskForm
from wtforms import RadioField, HiddenField, StringField, FieldList, PasswordField, BooleanField, SubmitField, IntegerField, SelectField, FormField
from wtforms.validators import DataRequired, Length, AnyOf, NumberRange
import pprint

class EdgeworkPrepForm(FlaskForm):
    plates = SelectField("Number of port plates:", choices=[0, 1, 2, 3, 4, 5])
    indicators = SelectField("Number of indicators:", choices=[0, 1, 2, 3, 4, 5])
    submit = SubmitField('Confirm')

class Portplate(FlaskForm):
    RJ = BooleanField("RJ-45")
    PS2 = BooleanField("PS/2")
    parallel = BooleanField("parallel")
    serial = BooleanField("serial")
    DVI = BooleanField("DVI")
    RCA = BooleanField("sterio RCA")

class testform(FlaskForm):
    string = StringField('teste')
    testfield = SelectField('TEST', choices=[(1, '1'), (2, '2'), (3, '3')], validate_choice=False)
    booltest = BooleanField('test')
    submit = SubmitField('test it')

class FullEdgeworkForm(FlaskForm):
    serial = StringField("Serial Number:", validators=[Length(min=6, max=6)])
    submit = SubmitField('Submit Edgework') 
    batteries = IntegerField("Battery count:")
    holders = IntegerField("Battery holder count:")
    Pcount = HiddenField('Pcount')
    Icount = HiddenField('Icount')

    PS21 = BooleanField("PS/2")
    RJ1 = BooleanField("RJ-45")
    DVI1 = BooleanField("DVI-D") 
    RCA1 = BooleanField("Sterio RCA") 
    parallel1 = BooleanField("Parallel") 
    serial1 = BooleanField("Serial")

    PS22 = BooleanField("PS/2")
    RJ2 = BooleanField("RJ-45")
    DVI2 = BooleanField("DVI-D") 
    RCA2 = BooleanField("Sterio RCA") 
    parallel2 = BooleanField("Parallel") 
    serial2 = BooleanField("Serial")

    PS23 = BooleanField("PS/2")
    RJ3 = BooleanField("RJ-45")
    DVI3 = BooleanField("DVI-D") 
    RCA3 = BooleanField("Sterio RCA") 
    parallel3 = BooleanField("Parallel") 
    serial3 = BooleanField("Serial")

    PS24 = BooleanField("PS/2")
    RJ4 = BooleanField("RJ-45")
    DVI4 = BooleanField("DVI-D") 
    RCA4 = BooleanField("Sterio RCA") 
    parallel4 = BooleanField("Parallel") 
    serial4 = BooleanField("Serial")

    PS25 = BooleanField("PS/2")
    RJ5 = BooleanField("RJ-45")
    DVI5 = BooleanField("DVI-D") 
    RCA5 = BooleanField("Sterio RCA") 
    parallel5 = BooleanField("Parallel") 
    serial5 = BooleanField("Serial")

    light1 = BooleanField("light on")
    label1 = SelectField("Label", choices=['BOB','CAR', 'CLR', 'FRK', 'FRQ', 'IND', 'MSA', 'NSA', 'SND', 'TRN'], validate_choice=False)

    light2 = BooleanField("light on")
    label2 = SelectField("Label", choices=['BOB','CAR', 'CLR', 'FRK', 'FRQ', 'IND', 'MSA', 'NSA', 'SND', 'TRN'], validate_choice=False)

    light3 = BooleanField("light on")
    label3 = SelectField("Label", choices=['BOB','CAR', 'CLR', 'FRK', 'FRQ', 'IND', 'MSA', 'NSA', 'SND', 'TRN'], validate_choice=False)

    light4 = BooleanField("light on")
    label4 = SelectField("Label", choices=['BOB','CAR', 'CLR', 'FRK', 'FRQ', 'IND', 'MSA', 'NSA', 'SND', 'TRN'], validate_choice=False)

    light5 = BooleanField("light on")
    label5 = SelectField("Label", choices=['BOB','CAR', 'CLR', 'FRK', 'FRQ', 'IND', 'MSA', 'NSA', 'SND', 'TRN'], validate_choice=False)

class wiresform(FlaskForm):
    wire1 = SelectField("Wire1", choices=['None','Black', 'White', 'Blue', 'Yellow', 'Red'], validate_choice=False)
    wire2 = SelectField("Wire2", choices=['None','Black', 'White', 'Blue', 'Yellow', 'Red'], validate_choice=False)
    wire3 = SelectField("Wire3", choices=['None','Black', 'White', 'Blue', 'Yellow', 'Red'], validate_choice=False)
    wire4 = SelectField("Wire4", choices=['None','Black', 'White', 'Blue', 'Yellow', 'Red'], validate_choice=False)
    wire5 = SelectField("Wire5", choices=['None','Black', 'White', 'Blue', 'Yellow', 'Red'], validate_choice=False)
    wire6 = SelectField("Wire6", choices=['None','Black', 'White', 'Blue', 'Yellow', 'Red'], validate_choice=False)
    submit = SubmitField("Process")    

class wiresequenceform(FlaskForm):
    color = RadioField("Color", choices=['Red', 'Black', 'Blue'])
    letter = RadioField("Letter", choices=['A', 'B', 'C'])
    submit = SubmitField('Check')
    hiddenred = HiddenField('red', default=0)
    hiddenblue = HiddenField('blue', default=0)
    hiddenblack = HiddenField('black', default=0)

class buttonform(FlaskForm):
    color = SelectField('Button Color', choices=['Other', 'Blue', 'White', 'Red', 'Yellow'], validate_choice=False) 
    label = SelectField('Button Label', choices=['Other', 'Abort', 'Detonate', 'Hold'], validate_choice=False)
    hold = HiddenField('hold?', default='False')
    light = SelectField('Light Color', choices=['Other', 'Yellow', 'Blue'], validate_choice=False)
    submit = SubmitField('PRESS!')

class keypadform(FlaskForm):
    symbol1 = RadioField('Symbol 1', choices=[u"ϙ", u"Ω", u"Ψ", u"Ϟ", u"Ж", u"Ѭ", u"Ѧ", u"Ԇ", u"¿", u"©", u"Ѯ", u"Ѣ", u"Ҋ", u"б", u"★", u"☆", u"ټ", u"Ѽ", u"ϗ", u"æ", u"Ӭ", u"¶", u"Ͼ", u"Ͽ", u"Ҩ", u"ƛ", u"҂"], validate_choice=False)
    symbol2 = RadioField('Symbol 2', choices=[ u"ϙ", u"Ω", u"Ψ", u"Ϟ", u"Ж", u"Ѭ", u"Ѧ", u"Ԇ", u"¿", u"©", u"Ѯ", u"Ѣ", u"Ҋ", u"б", u"★", u"☆", u"ټ", u"Ѽ", u"ϗ", u"æ", u"Ӭ", u"¶", u"Ͼ", u"Ͽ", u"Ҩ", u"ƛ", u"҂"], validate_choice=False)
    symbol3 = RadioField('Symbol 3', choices=[u"ϙ", u"Ω", u"Ψ", u"Ϟ", u"Ж", u"Ѭ", u"Ѧ", u"Ԇ", u"¿", u"©", u"Ѯ", u"Ѣ", u"Ҋ", u"б", u"★", u"☆", u"ټ", u"Ѽ", u"ϗ", u"æ", u"Ӭ", u"¶", u"Ͼ", u"Ͽ", u"Ҩ", u"ƛ", u"҂"], validate_choice=False)
    symbol4 = RadioField('Symbol 4', choices=[u"ϙ", u"Ω", u"Ψ", u"Ϟ", u"Ж", u"Ѭ", u"Ѧ", u"Ԇ", u"¿", u"©", u"Ѯ", u"Ѣ", u"Ҋ", u"б", u"★", u"☆", u"ټ", u"Ѽ", u"ϗ", u"æ", u"Ӭ", u"¶", u"Ͼ", u"Ͽ", u"Ҩ", u"ƛ", u"҂"], validate_choice=False)
    submit = SubmitField('Solve')

class needyknobform(FlaskForm):
    light11 = BooleanField('l11')
    light12 = BooleanField('l12')
    light13 = BooleanField('l13')
    light21 = BooleanField('l21')
    light22 = BooleanField('l22')
    light23 = BooleanField('l23')
    submit = SubmitField('Check')
