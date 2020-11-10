from pymongo import MongoClient


client = MongoClient('localhost', 27017)
db = client.dbsparta

store_list = [
    {'name': 'store1', 'desc': 'desc1', 'image': 'http://naver.com/image1'},
    {'name': 'store2', 'desc': 'desc2', 'image': 'http://naver.com/image2'},
    {'name': 'store3', 'desc': 'desc3', 'image': 'http://naver.com/image3'},
    {'name': 'store3', 'desc': 'desc3', 'image': 'http://naver.com/image3'},
    {'name': 'store3', 'desc': 'desc3', 'image': 'http://naver.com/image3'},
    {'name': 'store3', 'desc': 'desc3', 'image': 'http://naver.com/image3'},
]

for store in store_list:
    db.store.insert_one(store)
