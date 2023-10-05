from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def principal():
    return render_template('principal.html')

@app.route('/secundaria')
def secundaria():
    return render_template('/secundaria.html')

if __name__ == '__main__':
    app.run(port=5000, debug=True)