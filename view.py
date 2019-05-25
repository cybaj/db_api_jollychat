from flask import Flask
from shutil import copyfile

app = Flask(__name__, static_folder='view')

@app.route('/')
def static_proxy():
    copyfile('db.json', 'view/sample.json')
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(port=7000)
