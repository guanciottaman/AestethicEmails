from flask import Flask, render_template, request
import imaplib
import sqlite3

db = sqlite3.connect('db.sqlite3')
c = db.cursor()
c.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)')
db.commit()
db.close()

imap_host = 'imap.gmail.com'
imap = imaplib.IMAP4_SSL(imap_host)

app = Flask(__name__)
app.config['SECRET_KEY'] = b'+\xa7\x87\xf3\x83Qbs8W\xef\xf7p\x92Q\x8b'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        db = sqlite3.connect('db.sqlite3')
        c = db.cursor()
        c.execute('')
        return render_template('index.html', username=username, password=password)

if __name__ == '__main__':
    app.run(debug=True)
