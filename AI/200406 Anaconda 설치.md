## Anaconda
- 버전 관리가 쉬움
- 여러 가지 환경을 만들어두고 사용할 수 있음
- 환경마다 다른 패키지 설치해서 사용

### Anaconda Prompt 명령어
environment list 출력
```
conda env list
```

새로운 environment 생성
```
conda create -n [env명]
```
환경 변경
```
conda activate [env명]
```
패키지 설치 (ex. nltk 설치)
```
conda install nltk
```
환경 비활성화
```
conda deactivate
```
