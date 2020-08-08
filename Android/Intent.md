# Intent

## 1. Intent Flag
### 최상위 activity만 남기기
- FLAG_ACTIVITY_CLEAR_TASK
- FLAG_ACTIVITY_NEW_TASK

## 2. PendingIntent
- 기본 목적: 외부 애플리케이션에 권한을 허가하여 안에 들어있는 intent를 본인 앱의 자체 프로세스에서 실행하는 것처럼 사용하게 함  
### Example
- 사용자가 **알림**으로 어떤 작업을 수행할 때 intent가 실행되도록 선언(Android system의 **NotificationManager**가 intent를 실행)
- **앱 위젯**으로 어떤 작업을 수행할 때 intent가 실행되도록 선언(메인 화면 앱이 intent를 실행)
- 지정된 시간에 intent가 실행되도록 선언(Android system의 **AlarmManager**가 intent를 실행)