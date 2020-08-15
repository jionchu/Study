# git config

global로 선언해주면 전체에 적용됨
- git config --global user.name "user.name"
- git config --global user.email <user.email>


프로젝트마다 다른 사용자로 설정하고 싶은 경우 global을 빼면 됨  
따로 범위 설정 하지 않으면 기본적으로 --local 옵션 적용됨  
- git config user.name "user.name"
- git config user.email <user.email>

CRLF will be replaced by LF 오류 해결법
- git config --global core.autocrlf true