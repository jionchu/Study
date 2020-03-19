# Node.js로 번역기 만들기

### 모듈 설치
```
npm install --save google-translate-api
```

### 코드 작성
```javascript
const translate = require('google-translate-api);

translate('안녕하세요!',{from:'ko',to:'en'}).then(res => {
    console.log(res.text);
}).catch(err => {
    console.error(err);
})
```
실행하면 다음과 같은 결과가 나온다.
```
Hello!
```

참고: https://brunch.co.kr/@skykamja24/130