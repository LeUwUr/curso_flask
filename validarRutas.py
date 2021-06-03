from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hola mundito como estas'

@app.route('/params/')
@app.route('/params/<name>/')
@app.route('/params/<name>/<last_name>/')
@app.route('/params/<name>/<int:num>/')
def params(name = 'este es un valor por default', last_name = 'nada', num = 'nada'):


    
    return 'El parametro es {}'.format(name, last_name, num)

if __name__ == '__main__':
    app.run(debug = True, port= 8003)