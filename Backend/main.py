
from flask import Flask, request, jsonify, json

app = Flask(__name__)




@app.route('/')
def hello_world():
    return 'Hello World'
 
@app.route('/sendInformationToController', methods=['POST'])
def send_Information_To_Controller():
    data = request.get_json()

if __name__ == '__main__':
    app.run()
