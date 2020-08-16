# Manifest

모든 앱 프로젝트는 프로젝트 소스의 루트에 AndroidManifest.xml 파일이 있어야 한다. Manifest 파일은 Android 빌드 도구, Android 운영체제 및 Google Play에 앱에 관한 필수 정보를 설명한다.

매니페스트 파일은 특히 다음과 같은 내용을 선언해야 한다.
- 앱의 패키지 이름: 시스템과 Google Play에서 고유한 앱 식별자로 사용된다.
- 앱의 구성 요소(모든 액티비티, 서비스, Broadcast Receiver, Content Provider 포함)
- 앱이 시스템 또는 다른 앱의 보호된 부분에 접근하기 위해 필요한 권한