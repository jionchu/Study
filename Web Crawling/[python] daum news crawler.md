# [python] daum news crawler
[daum 뉴스](https://media.daum.net/)에서 뉴스 타이틀 크롤링하기
```python
import requests
from bs4 import BeautifulSoup
 
res = requests.get('https://media.daum.net/') 
soup = BeautifulSoup(res.content, 'html.parser')
 
mytitle = soup.select('#mArticle > div.box_headline > ul > li > strong > a')
for top in mytitle:
    print(top.text.strip())
```

```
'격리' 어기면 최대 1년 징역..'코로나 3법'으로 달라지는 ...
한인 자가 격리 뒤 '현관문 봉인'..中 "배은망덕 아냐"
"가장 큰 원인은 중국서 온 한국인" 박능후 발언 논란
그리스서도 코로나19 첫 감염자 발생.."이탈리아 북부 여행자"
일, 곧바로 '한국발 입국 제한'..정작 국내 검사는 1천여건뿐
민생당, '사무총장 바른미래·대통령 회동 유성엽 참석' 합의
민생당, '사무총장 바른미래·대통령 회동 유성엽 참석' 합의
민생당, '사무총장 바른미래·대통령 회동 유성엽 참석' 합의
우체국 · 농협에서도 마스크 판매한다..1인 5장 제한
코로나19 방역, 선방하는 줄 알았는데 왜 무너졌나
"일단 닫자"..줄줄이 사옥 폐쇄에 재택근무
이란 '보건부 차관'까지 감염..유럽도 확산 비상
```