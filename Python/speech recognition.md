# Speech Recognition

```python
!pip install SpeechRecognition
import speech_recognition as sr
```
```python
r = sr.Recognizer()
audio = sr.AudioFile('sample.wav')
with audio as source:
    audio = r.record(source)

r.recognize_google(audio_date = audio, language = "ko-KR")
```