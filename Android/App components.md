# App components
Android 앱의 필수적인 기본 구성 요소. 각 component는 시스템이나 사용자가 앱에 들어올 수 있는 진입점이다. 다른 component에 종속되는 component도 있다.
- Activities
- Services
- Broadcast receivers
- Content providers

## 1. Activity
사용자와 상호작용하기 위한 진입점. 사용자 인터페이스를 포함한 화면 하나를 나타냄

## 2. Service
여러 가지 이유로 백그라운드에서 앱을 계속 실행하기 위한 다목적 진입점. 백그라운드에서 실행되는 component로, 오랫동안 실행되는 작업을 수행하거나 원격 프로세스를 위한 작업을 수행한다. 사용자 인터페이스는 제공하지 않는다.

## 3. Broadcast Receiver
시스템이 정기적인 사용자 플로우 밖에서 이벤트를 앱에 전달하도록 지원하는 component로, 앱이 시스템 전체의 브로드캐스트 알림에 응답할 수 있게 한다. 현재 실행되지 않은 앱에도 시스템이 브로드캐스트를 전달할 수 있다.

## 4. Content provider
파일 시스템, SQLite 데이터베이스, 웹상이나 앱이 접근할 수 있는 다른 모든 영구 저장 위치에 저장 가능한 앱 데이터의 공유형 집합을 관리한다.