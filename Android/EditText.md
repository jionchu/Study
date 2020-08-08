# EditText

## nextFocus
키보드의 다음 키를 눌렀을 때 넘어갈 곳을 설정할 수 있다.  
- nextFocusDown
- nextFocusRight
- nextFocusLeft
- nextFocusUp

여러 가지 nextFocus 속성이 있지만 실제로 실행했을 때 nextFocusDown만 제대로 동작함

```java
android:nextFocusDown="@id/nextEditText"
```

## imeOptions
### 1) actionDone
키보드의 완료 키를 눌렀을 때 키보드를 숨긴다.
```java
android:imeOptions="actionDone"
```