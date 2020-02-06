## 1. HTML vs JS
### <script>
html 코드 안에 javascript 코드가 시작된다는 것을 알려주는 태그
```html
<!-- javascript -->
<script>
    document.write('hello world');
</script>
```
```html
<!-- html -->
hello world
```
문자열 출력시 결과는 동일

### javascript는 동적으로 동작
ex) javascript는 1+1을 계산해서 2를 출력하고 javascript 코드가 아닌 html 코드는 1+1을 출력한다.
```html
<!-- javascript -->
<script>
    document.write(1+1);
</script>
```
```html
<!-- html -->
1+1
```

### Event
- javascript가 사용자와 상호작용 하는데 핵심적 역할, 웹브라우저 위에서 일어나는 사건
- 태그 속성값을 웹브라우저가 기억하고 있다가 이벤트 발생 시 웹브라우저가 javascript 코드를 해석하여 동작함
- ex) onclick, onchange, onkeydown(키보드 눌렀을 때)

### 콘솔(console)
- 웹 브라우저에서 F12를 누르면 나옴
- javascript 파일을 따로 만들지 않고 즉석으로 코드를 실행할 수 있음
- 현재 켜져 있는 해당 웹브라우저를 대상으로 javascript 코드가 실행됨
