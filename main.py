from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'The sole purpose is to host some files on GH'


app.run(host='0.0.0.0', port=81)
