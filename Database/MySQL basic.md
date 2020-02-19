# MySQL basic

## 1. Install MySQL
mysql 설치
```
> npm install mysql
```

## 2. Create user
mysql 실행
```
> sudo service mysql start
```
root로 접근
```
> mysql –u root
```
user 생성
```
mysql> CREATE USER ‘username’@’localhost’ IDENTIFIED BY ‘user_password’;
```

## 3. Create database
database 생성하기
```
mysql> CREATE DATABASE my_db;
```
존재하는 database 확인하기
```
mysql> SHOW DATABASES;
```
```
+--------------------+
| Database           |
+--------------------+
| information_schema |
| my_db              |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
5 rows in set (0.00 sec)
```
사용자에게 데이터베이스 접근 권한 주기
```
mysql> GRANT ALL PRIVILEGES ON *.* TO 'username'@'localhost' IDENTIFIED BY 'user_password';
```
root가 아닌 user로 로그인하여 작업하기
```
mysql> \q
> mysql –u username –p
Enter password: ******
```
