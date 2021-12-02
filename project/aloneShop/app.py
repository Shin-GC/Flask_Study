from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('localhost', 27017)
db = client.alone_shop

# HTML 화면 보여주기
@app.route('/')
def homework():
    return render_template('index.html')


# 주문하기(POST) API
@app.route('/order', methods=['POST'])
def save_order():
    name = request.form['name']
    address = request.form['address']
    phone = request.form['phone']
    count = request.form['count']

    doc = {
        'name': name,
        'address': address,
        'phone': phone,
        'count': count,
    }

    db.alone_shop.insert_one(doc)

    return jsonify({'msg': '저장 완료!'})


# 주문 목록보기(Read) API
@app.route('/order', methods=['GET'])
def view_orders():
    orders = list(db.alone_shop.find({}, {'_id': False}))

    return jsonify({'all_orders': orders})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
