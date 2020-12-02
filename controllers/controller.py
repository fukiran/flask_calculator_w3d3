from app import app
from modules import calculator

@app.route('/add/<num_1>/<num_2>')
def add(num_1,num_2):
    return str(calculator.add(int(num_1),int(num_2)))

@app.route('/subtract/<num_1>/<num_2>')
def subtract(num_1,num_2):
    return str(calculator.subtract(int(num_1),int(num_2)))

@app.route('/multiply/<num_1>/<num_2>')
def multiply(num_1,num_2):
    return str(calculator.multiply(int(num_1),int(num_2)))

@app.route('/divide/<num_1>/<num_2>')
def divide(num_1,num_2):
    return "The answer is  " + str(calculator.divide(int(num_1),int(num_2)))