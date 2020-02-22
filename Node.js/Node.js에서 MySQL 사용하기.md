# Node.js에서 MySQL 사용하기

## 1. Simple Example
```javascript
// main.js
var mysql = require('mysql'); // mysql 모듈 불러오기
var connection = mysql.createConnection({
    host: 'localhost', // 호스트 주소
    user: 'me', // mysql user
    password: 'secret', // mysql password
    database: 'my_db' // mysql 데이터베이스
}); // 연결할 때 사용되는 정보를 담고 있음

connection.connect(); // mysql에 연결

// query를 통해 실제 데이터베이스의 값을 다룸
connection.query('SELECT 1 + 1 AS solution',
function (error, results, fields){
    if(error) throw error;

    // results는 query문을 실행한 결과를 return
    // 값의 타입이 배열로 들어가고, column은 JSON 방식
    console.log(results);
    // RowDataPacket ??
    console.log('The solution is: ', results[0].solution);
});

connection.end(); // mysql 연결 끊기
```
```
> node main.js
```
```
[ RowDataPacket { solution: 2 } ]
The solution is: 2
```
