# SurfaceView vs TextureView

draw를 실행할 때 기존 View의 문제
1. UI 스레드에서만 그릴 수 있다.
2. View의 계층 구조를 타고 올라가야 한다.
3. 실시간으로 그리기 어렵다.

대안으로 SurfaceView가 등장

## 1. SurfaceView
일반 View는 onDraw 메소드를 시스템에서 자동으로 호출함으로써 화면을 그리기 때문에 늦게 그려질 수도 있다. 반면 SurfaceView는 시스템에 맡기는 것이 아니라 스레드를 이용하여 강제로 화면에 그리기 때문에 원하는 시점에 바로 화면에 그릴 수 있다.  

그래서 SurfaceView는 애니메이션이나 동영상과 같이 연산처리가 많이 필요한 뷰를 위해 사용된다.  

### 더블 버퍼링
**SurfaceHolder**라는 콜백 함수가 **Surface**라는 버퍼에 그린 후에 Surface가 **SurfaceView**에 반영된다.  
처리속도가 느린 View에 직접 그리는 것이 아니라 처리속도가 빠른 메모리에서 직접 처리한 다음 View로 고속 전송하는 방식  

SurfaceView는 Window의 일부를 뚫어서(punch) 자신이 보이게 하고 Window와 View가 블렌딩되어 화면에 보여진다.  
![surface view](https://github.com/jionchu/TIL/blob/master/Android/images/surfaceview.png) 

### override method
- public void onDraw (Canvas canvas): 화면을 그린다.
- public void surfaceChanged(): 뷰가 변경될 때 호출
- public void surfaceCreated(): 뷰가 생성될 때 호출
- public void surfaceDestroyed(): 뷰가 종료될 때 호출

#### 확대, 축소, 비트맵 캡쳐 불가
대안으로 TextureView이 등장한다.

## 2. TextureView
SurfaceTexture, TextureView, SurfaceTextureListner가 한 set로 작동한다.  
이 중 SurfaceTexture는 framework가 관리하고 TextureView는 일반 View처럼 사용한다.  
Listener만 잘 override하여 구현하면 사용이 간편함  

카메라를 이용한 어떠한 기능을 만들어 낼 때 주로 사용한다.
- 스트리밍 서비스
- 실시간 얼굴 인식

참고: https://javaexpert.tistory.com/170  
https://aroundck.tistory.com/2075  
https://verybutter.tistory.com/24