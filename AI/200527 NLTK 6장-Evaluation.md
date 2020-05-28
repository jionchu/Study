# Evaluation

## 1. Precision & Recall
- **Precision**: which indicates how many of the items that we idnentified were relevant, is **TP/(TP+FP)**
- **Recall**: which indicates how many of the relevant items that we identified, is **TP/(TP+FN)**
- **F-Measure** (or F-Score): which combines the precision and recall to give a single score, is defined to be the harmonic mean of the precision and recall **(2 X Precision X Recall)/(Precision+Recall)**

![precision & recall](https://github.com/jionchu/TIL/blob/master/AI/images/precision_recall.PNG)  

## 2. Decision Trees

### 1) Entropy
- If most input values have the same label, then entropy is **low**

질문을 가장 적게 할 수 있도록 (entropy가 가장 작도록) decision tree를 만들어야 함