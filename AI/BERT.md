# BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding

## Abstract
- BERT:Bidirectional Encoder Representations from Transformer
  - Transformer 구조를 활용한 Language Representation
- 기본적으로 wiki나 book data와 같은 대용량 **unlabeled data**로 모델을 미리 학습시킨 후 특정 task를 가지고 있는 labeled data로 **transfer learning**을 하는 모델
- BERT 이전에 이러한 접근 방법을 가지는 모델들이 있지만 shallow bidirectional 또는 unidirectional 하므로 language representation이 부족함
- BERT는 특정 task를 처리하기 위해 새로운 network를 붙일 필요 없이 BERT 모델 자체의 fine-tuning을 통해 해당 task의 state-of-the-art를 달성했음

## 1. Introduction
### 1.1 기존 모델
- pre-trained language representation을 적용하는 방식은 크게 2가지가 있음
  - **feature-based approach** : 특정 task를 수행하는 network에 pre-trained language representation을 추가적인 feature로 제공 → 두 개의 network를 붙여서 사용한다고 보면 됨 (ex. ELMo)
  - **fine-tuning approach** : task-specific한 parameter를 최대한 줄이고, pre-trained된 parameter들을 downstream task 학습을 통해 조금만 바꿔주는 (fine-tuning) 방식 (ex. OpenAI GPT)
- 기존의 pre-trained 모델들은 pre-training 시에 동일한 objective function으로 학습을 수행했지만, **BERT**는 새로운 방식으로 **pre-trained Language Representation**을 학습함

### 1.2 BERT
- BERT pre-training의 새로운 방법론은 크게 2가지로 나눌 수 있음
  - 기존 방법론 : 일반적인 language model : 앞의 n개의 단어를 가지고 뒤의 단어를 예측하는 모델을 만드는 것(n-gram). 하지만 이는 필연적으로 **unidirectional**할 수 밖에 없음.
  - **Masked Language Model(MLM)** : input에서 무작위로 몇개의 token을 mask 시킴. 그리고 이를 Transformer 구조에 넣어서 주변 단어의 context만 보고 mask된 단어를 예측하는 모델. **OpenAI GPT**도 Transformer 구조를 사용하지만 앞의 단어들만 보고 뒷 단어를 예측하는 **Transformer decoder** 구조를 사용함. 이와 달리 **BERT**는 input 전체와 mask된 token을 한번에 **Transformer encoder**에 넣고 원래 token 값을 예측하므로 **deep bidirectional**하다고 할 수 있음
  - **next sentence prediction** : 두 문장을 pre-training 시에 같이 넣어줘서 두 문장이 이어지는 문장인지 아닌지 맞추는 것. pre-training 시에는 50:50 비율로 실제로 이어지는 두 문장과 랜덤하게 추출된 두 문장을 넣어줘서 BERT가 맞추게 시킴. 이러한 task는 실제 Natural Language Inference와 같은 task를 수행할 때 도움이 됨

## 2. BERT
- BERT는 **Attention is all you need**에서 소개된 **Transformer**를 사용하지만, pre-training과 fine-tuning시의 아키텍처를 다르게 하여 **Transfer Learning**을 용이하게 만드는 것이 핵심

### 2.1 Model Architecture
- transformer 중에서도 **encoder** 부분만 사용
- 모델의 크기에 따라 *base* 모델과 *large* 모델을 제공함
- **BERT_base** 모델의 경우, **OpenAI GPT** 모델과 hyper parameter가 동일함
