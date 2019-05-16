from flask import Flask
from shutil import copyfile

copyfile('db.json', 'view/sample.json')

app = Flask(__name__, static_folder='view')

@app.route('/')
def static_proxy():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(port=8000)
