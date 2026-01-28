from flask import Flask, render_template, request
from func import calcular_hora_muerte

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def perito():
    if request.method == 'POST':
        try:
            Ta = float(request.form['Ta'])
            hora1 = request.form['hora1']
            T1 = float(request.form['T1'])
            hora2 = request.form['hora2']
            T2 = float(request.form['T2'])

            resultado = calcular_hora_muerte(Ta, hora1, T1, hora2, T2)
            return render_template('resultado.html', resultado=resultado)
        except ValueError:
            return render_template('resultado.html', resultado="Error: Ingresa números válidos y horas en formato HH:MM")
    
    return render_template('perito.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)