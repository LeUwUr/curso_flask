from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hola mundito como estas'

#https://localhost:8002/params?params1=Eva_Mariana&params2=Vidana_aguirre
#https://localhost:8002/params

@app.route('/params')
def params():
    param = request.args.get('params1','no contiene este parametro')
    param_dos = request.args.get('params2','no contiene este parametro')
    
    return 'El parametro es {}, {}'.format(param, param_dos)

if __name__ == '__main__':
    app.run(debug = True, port= 8002)