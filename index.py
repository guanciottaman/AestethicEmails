from flask import Flask, render_template, request

app = Flask(__name__)
app.config['SECRET_KEY'] = b'+\xa7\x87\xf3\x83Qbs8W\xef\xf7p\x92Q\x8b'

@app.route('/', methods=['GET'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
