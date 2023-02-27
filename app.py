from flask import Flask, render_template, request
from preguntas import preguntas

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def encuesta():
    if request.method == 'POST':
        respuestas = dict(request.form)
        if 'pregunta' in respuestas and 'respuesta' in respuestas:
            preg_num = int(respuestas['pregunta'])
            try:
                resp_num = int(respuestas['respuesta'])
            except ValueError:
                resp_num = None
            if resp_num is not None:
                respuestas[str(preg_num)] = str(resp_num)
            preg_num += 1
        else:
            preg_num = 0
            respuestas = {}
    else:
        preg_num = 0
        respuestas = {}

    if preg_num >= len(preguntas):
        # Mostrar resultados
        return render_template('resultados.html', preguntas=preguntas, respuestas=respuestas)
    else:
        # Mostrar siguiente pregunta
        pregunta_actual = preguntas[preg_num]
        return render_template('encuesta.html', pregunta=pregunta_actual, preg_num=preg_num, respuestas=respuestas)

if __name__ == '__main__':
    app.run()
