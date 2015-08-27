import random

from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def root():
    return jsonify({"an": "api"})

@app.route('/posts', methods=['POST'])
def posts():
    return jsonify({"yeah": "i got it"})

@app.route('/mightfail')
def mightfail():
    if random.randint(0, 1) == 0:
        return jsonify({"msg": "failed!"}), 404
    return jsonify({"msg": "didn't fail!"})

@app.route('/posts/<id>')
def get_post(id):
    return jsonify({"id": id})

if __name__ == '__main__':
    app.run(debug=True)
