from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__, static_folder='.')

# 投稿された猫のつぶやきをメモリ上に保持するリスト
cats_db = []

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

# index.html がデータを取得するために読みに行く場所
@app.route('/data.json')
def get_data_json():
    return jsonify(cats_db)

# index.html が投稿や「いいね」をしたときに保存しにくる場所
@app.route('/save', methods=['POST'])
def save_data():
    global cats_db
    data = request.get_json()
    if data is not None:
        cats_db = data
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
