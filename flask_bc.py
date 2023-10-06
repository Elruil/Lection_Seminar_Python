from flask import Flask
app = Flask(__name__)
@app.route('/')
def main():
    return '<h1>HELLO, World</h1>'
@app.route('/info')
def info():
    return '<h1>Меня создали сегодня для обучения</h1>' 
@app.route('/summa/<x>/<y>')
def summa(x, y):
    return f'<h1>{x} + {y} = {int(x) + int(y)}</h1>' 

if __name__ =='__main__':
    app.run()