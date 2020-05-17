# Sound Event Detection
## 1. Sound Event Detection이란?
- 실생활에서 녹음된 음에서 발생되는 다양한 이벤트 검출
- 녹음 파일에서 아무 소리도 없는 silence 구간과 여러 가지 event 구간의 발생 구간과 발생 시간 등을 찾아냄
- audio recording에서 event를 얼마나 잘 인식하느냐가 바로 SED model의 성능  

![sound event detection](https://github.com/jionchu/TIL/blob/master/Speech%20Recognition/images/sound_event_detection.png)  
- ASC란 Audio Scene Classification. 음향 event들이 무엇인지 분류하는 것
- 녹음 파일에서 어떠한 event 소리가 어떤 클레스 인지 주파수의 특징을 딥러닝 모델을 사용해서 찾고 어떤 class인지 분류하는 것

https://blog.naver.com/seongcheol02/221728238204

## 2. 음성 신호를 학습 데이터로 만드는 방법
### 1) Mel Frequency Cepstral Coefficient (MFCC)
- 소리의 고유한 특징을 나타내는 수치
- 언어 콘텐츠를 식별하고 다른 것들(background noise 등) 제거
- 자동 음성 인식, 화자 인식에도 널리 쓰이는 feature
- Mel Spectrum에서 Cepstral 분석을 통해 추출된 값

#### ㄱ. MFCC 추출과정
![mfcc](https://github.com/jionchu/TIL/blob/master/Speech%20Recognition/images/mfcc.png)  
1. 오디오 신호를 프레임별(보통 20ms - 40ms)로 나누어 FFT를 적용해 Spectrum을 구한다.
2. Spectrum에 Mel Filter Bank를 적용해 Mel Spectrum을 구한다.
3. Mel Spectrum에 Cepstral 분석을 적용해 MFCC를 구한다.

#### ㄴ. FFT(Fast Fourier Transform: 고속 푸리에 변환)
신호를 주파수 성분으로 변환하는 알고리즘으로, 기존의 이산 푸리에 변환(DFT)을 더욱 빠르게 수행할 수 있도록 최적화한 알고리즘.

#### ㄷ. MFCC 추출과정 (좀 더 자세)
1. Frame the signal into short frames.

2. For each frame calculate the periodogram estimate of the power spectrum.
하지만 periodogram spectral estimate는 여전히 ASR에 필요하지 않은 많은 정보를 담고 있음. 특히 cochlea는 두 개의 가까운 주파수를 구별하지 못함

3. Apply the mel filterbank to the power spectra, sum the energy in each filter.  
periodogram 뭉치를 모아서 더함

4. Take the logarithm of all filterbank energies.  
- 인간은 선형 스케일로 소리의 강도를 듣지 않기 때문  
- 일반적으로 감지된 소리의 볼륨을 2배로 얻기 위해서는 소리의 에너지의 8배가 필요함  
- log를 적용시킴으로써 feature를 인간이 실제 듣는 것에 가깝게 매치시킴  
- 세제곱이 아닌 로그인 이유: 로그는 ceptstral mean subtraction이라는 channel normalization 기술을 쓸 수 있게 해줌

5. Take the DCT of the log filterbank energies.
filterbank가 모두 겹치기 때문에 filterbank 에너지들끼리 상관관계가 있음

6. Keep DCT coefficients 2-13, discard the rest.
DCT coefficients가 많을수록 filterbank 에너지의 빠른 변화를 나타내고 ASR 성능을 하락시킴

#### ㄹ. Mel scale
인간은 높은 주파수보다 낮은 주파수의 소리 변화를 더 잘 구별함  
Mel scale로 변환함으로써 feature를 인간의 청각과 비슷하게 매치시킴

- 주파수에서 Mel scale로 변환하는 공식
M(f) = 1125 ln(1+f/700)

- Mel scale에서 주파수로 변환하는 공식
M^(-1)(m) = 700(exp(m/1125)-1)

http://soyoon.github.io/asr/2017/05/04/Voice-Signal-Processing.html