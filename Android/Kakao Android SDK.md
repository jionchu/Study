# Kakao Android SDK

## 1. 카카오톡 채널
app/build.gradle에 다음을 추가한다.
```java
implementation 'com.kakao.sdk:plusfriend:1.21.0'
```

### 1) 카카오톡 채널 추가하기
```java
try {
    PlusFriendService.getInstance().addFriend(PlusFriendActivity.this, "_xcLqmC");
} catch (KakaoException e) {
    // 에러 처리 (앱키 미설정 등등)
    Toast.makeText(getApplicationContext(), e.getMessage(), Toast.LENGTH_LONG).show();
}
```

### 2) 카카오톡 채널 채팅
```java
try {
    PlusFriendService.getInstance().chat(PlusFriendActivity.this, "_xcLqmC");
} catch (KakaoException e) {
    // 에러 처리 (앱키 미설정 등등)
    Toast.makeText(getApplicationContext(), e.getMessage(), Toast.LENGTH_LONG).show();
}
```

## ClassNotFoundException
처음 채널 연동을 시도했을 때 다음과 같은 오류가 발생함
```java
Caused by: java.lang.ClassNotFoundException: Didn’t find class “com.kakao.util.IConfiguration$Factory”
```
검색 결과 기존에 사용하던 카카오 sdk 모듈(usermgmt를 사용중이었음)과 version이 달라서 발생하는 문제였다. 공통으로 사용하는 모듈들이 있어 버전을 최대한 맞춰줘야 충돌이 발생하지 않는다고 한다.

참고: https://devtalk.kakao.com/t/topic/75850
