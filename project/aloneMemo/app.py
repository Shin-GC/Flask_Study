from flask import Flask, render_template, jsonify, request
import movie_crawling
from pymongo import MongoClient

app = Flask(__name__)


client = MongoClient('localhost', 27017)
db = client.dbsparta


# HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/memo', methods=['GET'])
def listing():
    articles = list(db.articles.find({}, {'_id': False}))
    return jsonify({'all_articles': articles})


# API 역할을 하는 부분
@app.route('/memo', methods=['POST'])
def saving():
    movie_name = request.form['movie_name']
    review = request.form['review']

    doc = movie_crawling.crawling_one(movie_name)
    doc['review'] = review

    db.articles.insert_one(doc)

    return jsonify({'msg': '저장 완료!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
