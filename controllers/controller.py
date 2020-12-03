from app import app
from modules.calculator import *

@app.route ('/add/<number1>/<number2>')
def browser_add(number1, number2):
    return add_numbers(number1, number2)

@app.route ('/subtract/<number1>/<number2>')
def browser_subtract(number1, number2):
    return subtract_numbers(number1, number2)

@app.route ('/multiply/<number1>/<number2>')
def browser_multiply(number1, number2):
    return multiply_numbers(number1, number2)

@app.route ('/divide/<number1>/<number2>')
def browser_divide(number1, number2):
    return divide_numbers(number1, number2)