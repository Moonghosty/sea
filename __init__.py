from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/resultado', methods=['POST'])
def resultado():
    desenvolvedor = request.form['desenvolvedor']
    turma = request.form['turma']
    professor = request.form['professor']
    data = request.form['data']
    dificuldade = request.form['dificuldade']
    confianca = request.form['confianca']
    
    return render_template('result.html', 
                           desenvolvedor=desenvolvedor, 
                           turma=turma, 
                           professor=professor, 
                           data=data, 
                           dificuldade=dificuldade, 
                           confianca=confianca)

if __name__ == '__main__':
    app.run(debug=True)