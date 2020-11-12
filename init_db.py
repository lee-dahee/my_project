from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.daldang

data = [
    {
        'name': '로타리과자',
        'desc': '망원동에 위치한 과자점 입니다.',
        'address': '서울 마포구 망원로6길 65',
        'naver_url': 'https://www.instagram.com/nabang.official/',
        'insta_url': 'https://map.naver.com/v5/entry/place/1463632135?c=14126910.6118331,4516631.9068985,13,0,0,0,dh&placePath=%2Fhome%3Fentry=plt',
        'category': 'cake',
        'img': "https://user-images.githubusercontent.com/70143301/98931442-5ed38100-2521-11eb-9938-87d6e4726ab3.png"
    },
    {
        'name': '바나나하루키',
        'desc': ':YOUR CAKE',
        'address': '서울 마포구 상수동 72-43',
        'naver_url': 'https://map.naver.com/v5/entry/place/37468319?c=14129273.4125530,4515851.7929668,15,0,0,0,dh&placePath=%3Fentry=plt',
        'insta_url': 'https://www.instagram.com/banana_haruki/',
        'category': 'cake',
        'img': "https://user-images.githubusercontent.com/70143301/98931452-61ce7180-2521-11eb-8b6a-c8b8a3f939df.png"
    },
    {
        'name': '불나방',
        'desc': '센스있는 디저트 작업실 불나방',
        'address': '역촌동 34-19번지 부동산옆',
        'naver_url': 'https://map.naver.com/v5/search/%EB%B6%88%EB%82%98%EB%B0%A9/place/1445926280?placeSearchOption=fromNxList=true%26noredirect=1%26entry=pll&c=14128325.493693072,4523451.516910225,13,0,0,0,dh&placePath=%2Fhome%3Fentry=pll',
        'insta_url': 'https://www.instagram.com/nabang.official/',
        'category': 'cake',
        'img': "https://user-images.githubusercontent.com/70143301/98931454-62ff9e80-2521-11eb-8e4a-ce27f456a94b.png"
    },
    {
        'name': '스위츠마인',
        'desc': '나카무라아카데미 전문가과정 수료',
        'address': '서울 은평구 역촌동 83-30 102호',
        'naver_url': 'https://map.naver.com/v5/entry/place/1344773660?c=14128132.61041138,4523222.630864622,13,0,0,0,dh&placePath=%2Fhome%3Fentry=plt',
        'insta_url': 'https://www.instagram.com/sweets.mine/?igshid=ef1nwyqypnip',
        'category': 'cake',
        'img': "https://user-images.githubusercontent.com/70143301/98931455-63983500-2521-11eb-82b6-34d56b7ecd94.png"
    },
    {
        'name': '쭈롱베이커리',
        'desc': '계절과 건강을 디저트로',
        'address': '경북 김천시 부곡중앙길 4 1층',
        'naver_url': 'https://map.naver.com/v5/search/%EC%AD%88%EB%A1%B1%EB%B2%A0%EC%9D%B4%EC%BB%A4%EB%A6%AC/place/1272412252?c=14259865.0744547,4317813.0722872,15,0,0,0,dh',
        'insta_url': 'https://www.instagram.com/jjurong_bake/',
        'category': 'cake',
        'img': "https://user-images.githubusercontent.com/70143301/98931456-63983500-2521-11eb-863b-0f97a1a3c433.png"
    },
    {
        'name': 'happy puppy house',
        'desc': 'happy puppy',
        'address': '경리단길',
        'insta_url': 'https://www.instagram.com/happypuppyhouse_/',
        'category': 'cake',
        'img': "https://user-images.githubusercontent.com/70143301/98931457-6430cb80-2521-11eb-85b9-c92a6ac14b15.png"
    },
    {
        'name': '플러피도넛',
        'desc': 'crispy yummy fluffy!',
        'address': '서울 마포구 성미산로 163',
        'naver_url': 'https://map.naver.com/v5/entry/place/1293352409?c=14129146.8088962,4518143.5071791,15,0,0,0,dh&placePath=%3Fentry=plt',
        'insta_url': 'https://www.instagram.com/fluffy.doughnut/',
        'category': 'doughnut',
        'img': "https://user-images.githubusercontent.com/70143301/98931578-8cb8c580-2521-11eb-8126-4cc8d6e1707b.png"
    },
    {
        'name': '올드페리도넛',
        'desc': '직접 로스팅 한 커피와 도넛을 판매합니다.',
        'address': '서울 용산구 한남대로27길 66',
        'naver_url': 'https://map.naver.com/v5/search/%EC%98%AC%EB%93%9C%ED%8E%98%EB%A6%AC%EB%8F%84%EB%84%9B/place/1029619861?c=14136954.3329722,4514688.5819213,15,0,0,0,dh&placePath=%3F%2526',
        'insta_url': 'https://www.instagram.com/oldferrydonut/',
        'category': 'doughnut',
        'img': "https://user-images.githubusercontent.com/70143301/98931580-8de9f280-2521-11eb-9329-674b7b626f44.png"
    },
    {
        'name': '파파도나스',
        'desc': '🍩1-2일전 예약은 센스😘',
        'address': '서울 용산구 신흥로 7',
        'naver_url': 'http://papadonas.com/',
        'insta_url': 'https://www.instagram.com/papadonas_hbc/',
        'category': 'doughnut',
        'img': "https://user-images.githubusercontent.com/70143301/98931584-8e828900-2521-11eb-856f-de7a197f6099.png"
    },
    {
        'name': '랜디스도넛',
        'desc': '수제 도넛 브랜드',
        'address': '🍊제주애월점 🍩서울연남점',
        'naver_url': 'http://randysdonuts.co.kr/',
        'insta_url': 'https://www.instagram.com/randysdonutskr1962/',
        'category': 'doughnut',
        'img': "https://user-images.githubusercontent.com/70143301/98931589-8fb3b600-2521-11eb-8629-f8154e9f910e.png"
    },
    {
        'name': '노티드도넛',
        'desc': '🐻Knotted X Sugarbear🐻',
        'address': '서울 용산구 대사관로5길 12 2층',
        'naver_url': 'https://map.naver.com/v5/search/%EB%85%B8%ED%8B%B0%EB%93%9C%EB%8F%84%EB%84%9B/place/1097972836?c=14133865.7992980,4514256.2349801,13,0,0,0,dh&placePath=%3Fentry%253Dpll%2526',
        'insta_url': 'https://www.instagram.com/cafeknotted/',
        'category': 'doughnut',
        'img': "https://user-images.githubusercontent.com/70143301/98931571-8aef0200-2521-11eb-9c04-05f0c12519b8.png"
    },
    {
        'name': '엣모스피어',
        'desc': 'Dessert&cafe 수제케이크와 마카롱',
        'address': '서울 마포구 망원로 54-1',
        'naver_url': 'https://map.naver.com/v5/search/%EC%97%A3%EB%AA%A8%EC%8A%A4%ED%94%BC%EC%96%B4/place/36883540?c=14122963.9681388,4517342.3799971,13,0,0,0,dh&placePath=%3Fentry%253Dpll%2526',
        'insta_url': 'https://www.instagram.com/atmosphere.cafe/',
        'category': 'macaron',
        'img': "https://user-images.githubusercontent.com/70143301/98931666-aa862a80-2521-11eb-8697-bad25d203ec3.png"
    },
    {
        'name': '아비오',
        'desc': '유기농 커피 전문 로스터리 카페입니다.',
        'address': '마포구 성미산로 82 명주빌딩 1층',
        'naver_url': 'https://map.naver.com/v5/search/%EC%B9%B4%ED%8E%98%20%EC%95%84%EB%B9%84%EC%98%A4/place/38522226?placeSearchOption=fromNxList=true%26noredirect=1%26entry=pll&c=14124540.4818472,4517863.1072523,13,0,0,0,dh&placePath=%2Fhome%3Fentry=pll',
        'insta_url': '',
        'category': 'macaron',
        'img': "https://user-images.githubusercontent.com/70143301/98931688-b07c0b80-2521-11eb-8238-e69334973ea3.png"
    },
    {
        'name': '디저트콩콩',
        'desc': '수제 마카롱 가득한 맛있는 디저트 맛집',
        'address': '서울 은평구 역촌동 78-1',
        'naver_url': 'https://map.naver.com/v5/search/%EB%94%94%EC%A0%80%ED%8A%B8%EC%BD%A9%EC%BD%A9/place/1235128808?placeSearchOption=fromNxList=true%26noredirect=1%26entry=pll&c=14123776.1115644,4523715.3172304,13,0,0,0,dh&placePath=%2Fhome%3Fentry=pll',
        'insta_url': 'https://www.instagram.com/dessert_kongkong/',
        'category': 'macaron',
        'img': "https://user-images.githubusercontent.com/70143301/98931692-b114a200-2521-11eb-90e5-c5cba7d8d4f6.png"
    },
    {
        'name': '하루쿠키',
        'desc': 'macaron & cake',
        'address': '전북 군산시 서수송1길 14-5',
        'naver_url': 'https://map.naver.com/v5/entry/place/36282923?c=14105186.4684895,4295786.9225496,15,0,0,0,dh&placePath=%3Fentry=plt',
        'insta_url': 'https://www.instagram.com/haroo.cookie/',
        'category': 'macaron',
        'img': "https://user-images.githubusercontent.com/70143301/98931695-b245cf00-2521-11eb-9314-b38f594b4560.png"
    },
    {
        'name': '미완성식탁',
        'desc': '망원동 말이 필요없는 마카롱 맛집',
        'address': '서울 마포구 망원로6길 37',
        'naver_url': 'https://map.naver.com/v5/entry/place/1837274244?c=14126867.0191205,4516790.9444420,15,0,0,0,dh&placePath=%3Fentry=plt',
        'insta_url': 'https://www.instagram.com/incompletetable/',
        'category': 'macaron',
        'img': "https://user-images.githubusercontent.com/70143301/98931698-b2de6580-2521-11eb-9788-9fd60a8a6f56.jpeg"
    },
    {
        'name': 'Of you',
        'desc': '카페 오브유[of you]',
        'address': '구미시 문장로 88, 2층',
        'naver_url': 'https://map.naver.com/v5/search/%EA%B5%AC%EB%AF%B8%20%EC%98%A4%EB%B8%8C%EC%9C%A0/place/1095240517?placeSearchOption=fromNxList=true%26noredirect=1%26entry=pll&c=14282096.3064000,4320407.1539346,13,0,0,0,dh&placePath=%2Fhome%3Fentry=pll%E2%80%8B',
        'insta_url': 'https://www.instagram.com/o.f.y.o.u/?igshid=xygco9t1p3vw',
        'category': 'macaron',
        'img': "https://user-images.githubusercontent.com/70143301/98936149-ee7c2e00-2527-11eb-851e-27ba71251a80.jpeg"
    }]


for store in data:
    db.store.insert(store)
    print(store)
