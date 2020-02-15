manifest에 다음 코드 입력  
https://gun0912.tistory.com/80

java.net.SocketException: socket failed: EACCES (Permission denied) 오류  
다음을 추가  
```
<uses-permission android:name="android.permission.INTERNET" />
```

java.net.socketexception broken pipe  
Intent를 뒤늦게 시작하게 함  
https://lookingfor.tistory.com/entry/%EC%9E%90%EB%B0%94-ExceptionBroken-pipe-%EC%98%A4%EB%A5%98-%ED%95%B4%EA%B2%B0-%EB%B0%A9%EB%B2%95

Connection reset 오류 -> 서버에서 제한해둔 것보다 영상 파일 용량이 커서 생기는 문제였다. 용량을 줄여서 전송하니 정상적으로 보내졌다.