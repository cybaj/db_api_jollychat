from flask import Flask, render_template, request
from dbm import DatabaseManager
import json

app = Flask(__name__)

dbm = DatabaseManager()

def initDB():
    global dbm
    if dbm == None :
        dbm = DatabaseManager()
    dbm.loadDatabase()
def closeDB():
    dbm = None

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/hello/<username>/<int:id>')
def hello_user(username, id):
    print(id)
    return 'User %s' % username

@app.route('/graph/')
def hello_graph():
    return 'this is graph api'

@app.route('/graph/get/')
def hello_get():
    return 'you need to specity options, /node/node_id or'

@app.route('/graph/get/node/<string:nodename>', methods=['GET', 'POST'])
def getNode(nodename):
    if request.method == 'GET':
        options = {'name': nodename} 
        initDB()
        node = dbm.findNode(options)
        closeDB()
        serialized = json.dumps(node)
        return serialized
    else: 
        return 'NO POST, GET IT'

@app.route('/graph/get/edge/<int:edgeId>', methods=['GET', 'POST'])
def getEdge(edgeId):
    if request.method == 'GET':
        return "getting %d edge" % edgeId
    else: 
        return 'NO POST, GET IT'

@app.route('/graph/insert/')
def hello_insert():
    return 'you need to specify options, /node/nodname or '

@app.route('/graph/insert/node/<string:nodename>', methods=['GET', 'POST'])
def insertNode(nodename):
    print("nodename: ", nodename)
    if request.method == 'POST':
        options = {'name': nodename}
        initDB()
        node = dbm.addNode(options)
        closeDB()
        serialized = json.dumps(node)
        return serialized
    else:
        return 'NO GET, POST IT'

@app.route('/graph/insert/edge/<string:firstNodeName>/<string:secondNodeName>', methods=['GET', 'POST'])
def insertEdge(firstNodeName, secondNodeName):
    if request.method == 'POST':
        options = {
                     'uv_nodes': (firstNodeName, secondNodeName), 
                     'weight': 1, 
                     'capacity': 1, 
                     'length': 1
                  }
        initDB()
        is_success =  dbm.addEdge(options)
        closeDB()
        return is_success 
    else:
        return 'NO GET, POST IT'
   
@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

if __name__ == '__main__':
    app.debug = True
    app.run(port=5000)
