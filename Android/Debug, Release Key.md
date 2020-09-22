# debug, release key

소셜 로그인(카카오, 구글 등)을 사용하는 경우 **debug ke**와 **release key**를 모두 등록해야 한다. debug 버전으로 개발만 하는 경우에는 debug 키해시만 등록해도 문제가 발생하지 않지만 release 버전으로 배포를 하는 경우 release 키해시를 등록하지 않으면 로그인이 되지 않는 문제가 발생한다.

## 1. 카카오 로그인
[카카오 개발자 페이지](https://developers.kakao.com/)에서 `내 애플리케이션 > 앱 설정 > 플랫폼 > Android > 키 해시`에 debug keyhash와 release keyhash를 모두 등록한다.

키 해시를 얻는 방법은 다음과 같다.
### 1) debug keyhash
```
keytool -exportcert -alias androiddebugkey -keystore <keystore location> | openssl sha1 -binary | openssl base64
```

### 2) release keyhash
jks 파일이 있는 디렉토리로 이동하여 명령어를 입력한다.
```
keytool -exportcert -alias <alias> -keystore <jks location> | openssl sha1 -binary | openssl base64
```
openssl이 환경변수로 설정되어 있지 않은 경우 `'openssl'은(는) 내부 또는 외부 명령, 실행할 수 있는 프로그램, 또는 배치 파일이 아닙니다.`라는 오류가 발생한다. [여기](https://code.google.com/archive/p/openssl-for-windows/downloads)에서 openssl 파일을 다운받은 후 다음과 같이 openssl 응용 프로그램의 위치를 직접 입력하면 된다.
```
keytool -exportcert -alias <alias> -keystore <jks location> | C:\Users\user\Desktop\openssl-0.9.8e_X64\bin\openssl.exe sha1 -binary | C:\Users\user\Desktop\openssl-0.9.8e_X64\bin\openssl.exe base64
```
명령어를 실행한 후 키 저장소 비밀번호를 입력하면 keyhash가 나타난다.

## 2. 구글 로그인
구글 로그인의 경우 keyhash가 아닌 SHA1 값을 입력해야 한다.
### 1) debug key
안드로이드 스튜디오 우측 `Gradle > Tasks > android > signingReport`에서 간단하게 얻을 수 있다.

### 2) release key
키 해시를 구할 때와 마찬가지로 jks 파일이 있는 디렉토리로 이동하여 명령어를 실행한다.
```
keytool -list -v -keystore <jks location>
```
명령어를 실행한 후 키 저장소 비밀번호를 입력하면 SHA1 값을 포함한 키 저장소에 대한 정보들이 나타난다.