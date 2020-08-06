# Permission

### fragment에서 requestPermission() 요청하기
```java
if (ContextCompat.checkSelfPermission(getActivity(), permission.READ_EXTERNAL_STORAGE)
          != PackageManager.PERMISSION_GRANTED) {
    requestPermissions(new String[] {permission.READ_EXTERNAL_STORAGE},
    RequestCode.READ_EXTERNAL_STORAGE_PERMISSION);
}
```