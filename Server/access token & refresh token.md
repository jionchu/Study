# Access Token & Refresh Token

access token(jwt)를 이용하여 인증할 때
1. token의 유효기간이 짧은 경우 사용자가 새로운 token을 자주 발급받아야 하므로 불편함
2. token의 유효기간이 긴 경우 토큰이 제 3자에게 탈취당했을 때 보안에 취약함

⇒ **Refresh token**을 이용하자!

## Refresh Token
- access token과 동일한 형태의 jwt
- 처음 로그인 할 때 access token과 함께 발급됨
- access token보다 유효기간이 길기 때문에 access token이 만료되었을 때 refresh token을 이용해서 access token을 갱신함
