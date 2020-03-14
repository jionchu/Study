# Calendar Provider API

사용자의 캘린더에 대해 쿼리, 삽입, 업데이트 및 삭제 등을 할 수 있다.  
어플리케이션과 동기화 어댑터는 Calendar Provider API를 통해 사용자의 캘린더 데이터를 보관하고 있는 데이터베이스 테이블에 대한 읽기/쓰기 권한을 얻을 수 있다.

한 사용자가 여러 개의 캘린더를 가질 수 있고, 각 캘린더는 각각 다른 계정과 연결될 수 있다.  

Calendar Provider API는 유연하고 효과적이도록 설계되었다.

## 1. 사용자 권한
Manifest에 사용자 권한을 추가한다.  
- **READ_CALENDAR**: 캘린더 데이터를 읽기 위한 권한
- **WRITE_CALENDAR**: 캘린더 데이터를 삭제, 삽입, 업데이트 하기 위한 권한
```
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"...>
    <uses-sdk android:minSdkVersion="14" />
    <uses-permission android:name="android.permission.READ_CALENDAR" />
    <uses-permission android:name="android.permission.WRITE_CALENDAR" />
    ...
</manifest>
```
권한이 없어도 인텐트를 이용하면 캘린더 앱으로 이동하여 보기, 수정을 한 후 원래 어플리케이션으로 돌아올 수 있다. 따로 권한 허가를 요청하거나 사용자 인터페이스를 제공하지 않아도 된다.  
