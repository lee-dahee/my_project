from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.daldang  # 'dbsparta'라는 이름의 db를 만듭니다.


## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/memu/<category>')
def memu(category):
    print(category)
    if category == 'cake':
        return render_template('cake.html')
    elif category == 'macaron':
        return render_template('macaron.html')
    else:
        return render_template('doughnut.html')


# @app.route('/menu', methods=['GET'])
# def memu():
#     category_receive = request.args.get('category_give')
#     print(category_receive)
#     return render_template('menu.html', category=category_receive)


@app.route('/store', methods=['GET'])
def store():
    category_receive = request.args.get('category_give')
    print(category_receive)
    store_list = list(db.store.find({'category': category_receive}, {'_id': False}))
    return jsonify({'result': 'success', 'store': store_list})


if __name__ == '__macaron__':
    app.run('0.0.0.0', port=5000, debug=True)

# ## API 역할을 하는 부분
# @app.route('/review', methods=['POST'])
# def write_review():
#     # title_receive로 클라이언트가 준 title 가져오기
#     title_receive = request.form['title_give']
#     # author_receive로 클라이언트가 준 author 가져오기
#     author_receive = request.form['author_give']
#     # review_receive로 클라이언트가 준 review 가져오기
#     review_receive = request.form['review_give']
#
#     # DB에 삽입할 review 만들기
#     review = {
#         'title': title_receive,
#         'author': author_receive,
#         'review': review_receive
#     }
#     # reviews에 review 저장하기
#     db.reviews.insert_one(review)
#     # 성공 여부 & 성공 메시지 반환
#     return jsonify({'result': 'success', 'msg': '리뷰가 성공적으로 작성되었습니다.'})
#
#
# @app.route('/review', methods=['GET'])
# def read_reviews():
#     # 1. DB에서 리뷰 정보 모두 가져오기
#     reviews = list(db.reviews.find({}, {'_id': 0}))
#     # 2. 성공 여부 & 리뷰 목록 반환하기
#     return jsonify({'result': 'success', 'reviews': reviews})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
