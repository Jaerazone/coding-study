const express = require('express');
const app = express();

app.use(express.urlencoded({extended: true})) 

app.listen(8080, function() {
    console.log('listening on 8080')
})
// 누군가가 /pet으로 방문하면..
// pet관련된 안내문을 띄워주자

app.get('/pet', function(요청, 응답) {
    응답.send('펫용품 쇼핑할 수 있는 페이지입니다')
})

app.get('/beauty', function(요청,응답) {
    응답.send('뷰티용품 쇼핑 페이지임')
})

app.get('/', function(요청,응답) {
    응답.sendFile(__dirname + '/index.html')
})

app.get('/write', function(요청,응답) {
    응답.sendFile(__dirname + '/write.html')
})

// 어떤사람이 /add경로로 POST 요청을 하면..
// ?? 를 해주세요~

app.post('/add', function(요청,응답) {
    응답.send('전송완료');
    console.log(요청.body);
    console.log(요청.body.title);
    console.log(요청.body.date);
}) // 이때 우리가 input에 적은 작성한 할일, 날짜는 '요청' 안에 저장되어있다
    // '요청'에 저장된정보를 쉽게 꺼내쓰려면 라이브러리 필요함
    // body-parser라이브러리가 이미 express에 기본 포함이라서
    // npm으로 따로 설치할 필요가 없다 
    // app.use(express.urlencoded({extended: true})) 
    // 이거만 맨위에 적어주면된다
    // body-parser은 html의 body안에 있는 데이터 (input같은놈들) 해석할수있게 도와준다

    //post요청으로 서버에 데이터를 전송하고싶으면
    // 1) app.use(express.urlencoded({extended: true})) 
    // 2) form데이터의 경우 input들에 name="" 쓰기  (input이 많을경우를 대비해 각자이름을새김)
    // 3) console.log(요청.body.~~) 콘솔로 확인하기
    // 4) 이제 이 데이터들을 영구적으로 저장해보자! DB에 저장해주세요~