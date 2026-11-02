from flask import Flask, request, jsonify, send_from_directory
import random

app = Flask(__name__, static_folder='.')

# 投稿された猫のつぶやきをメモリ上に保持するリスト
cats_db = []

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/api/cats', methods=['GET'])
def get_cats():
    return jsonify(cats_db)

@app.route('/api/cats', methods=['POST'])
def add_cat():
    data = request.get_json()
    if data and 'text' in data:
        cat = {
            'text': data['text'],
            'x': random.randint(5, 80),
            'y': random.randint(5, 80)
        }
        cats_db.append(cat)
        # 最大20個まで保持
        if len(cats_db) > 20:
            cats_db.pop(0)
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)