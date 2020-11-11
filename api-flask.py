from flask import Flask, jsonify

app = Flask(__name__)

tasks= [
	{'id':1,'name':'one'},
	{'id':2,'name':'two'}
]

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

if __name__ == '__main__':
    app.run(debug=True)