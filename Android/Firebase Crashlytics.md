# Firebase Crashlytics

## 1. Crashlytics란?
- 가벼운 실시간 오류 보고 도구
- 비정상 종료를 그룹화하고 비정상 종료를 유발하는 상황을 보여줌

## 2. 적용 방법
### 1) build.gradle (project)
```
buildscript {
    repositories {
        // Check that you have Google's Maven repository (if not, add it).
        google()
    }

    dependencies {
        // ...

        // Check that you have the Google Services Gradle plugin v4.3.2 or later
        // (if not, add it).
        classpath 'com.google.gms:google-services:4.3.3'

        // Add the Crashlytics Gradle plugin.
        classpath 'com.google.firebase:firebase-crashlytics-gradle:2.2.0'
    }
}

allprojects {
    repositories {
        // Check that you have Google's Maven repository (if not, add it).
        google()
    }
}
```

### 2) build.gradle (app)
```
// Apply the Crashlytics Gradle plugin
apply plugin: 'com.google.firebase.crashlytics'

dependencies {
    // Recommended: Add the Firebase SDK for Google Analytics.
    implementation 'com.google.firebase:firebase-analytics:17.5.0'

    // Add the Firebase Crashlytics SDK.
    implementation 'com.google.firebase:firebase-crashlytics:17.2.1'
}

```
기존의 fabric 라이브러리는 2020년 4월부터 중단되었다. 새로운 crashlytics는 별도의 초기화 코드가 필요하지 않음

참고: https://firebase.google.com/docs/crashlytics/get-started?hl=en&platform=android