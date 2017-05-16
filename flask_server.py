from flask import Flask, render_template
from prometheus_metrics import setup_metrics

app = Flask(__name__)
setup_metrics(app)

@app.route('/')
def mainRoute():
    return render_template('index.html')

@app.route('/cats')
def cats():
    return render_template('cats.html')

@app.route('/dogs')
def dogs():
    return render_template('dogs.html')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')

