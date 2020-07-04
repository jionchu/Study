# SharedPreferences

## apply vs commit
- **apply**
  - 메모리 내 SharedPreferences 객체를 즉시 변경
  - 업데이트를 디스크에 *비동기적*으로 씀
- **commit**
  - 데이터를 디스크에 *동기적*으로 씀
  - 동기적이므로 기본 스레드에서 호출하는 것은 피해야 함 (UI 렌더링이 일시중지될 수 있음)