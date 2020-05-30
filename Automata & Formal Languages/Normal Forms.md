# Normal Forms

## 1. Chomsky Normal Form
변수가 terminal 혹은 두 개의 변수로 mapping 되는 것
- A → BC
- A → a

- Chomsky normal forms are good for parsing and proving theorems
- It is very easy to find the Chomsky normal form of any context-free grammar

## 2. Greibach Normal Form
왼쪽에 symbol이 나오고 오른쪽에 변수가 나오는 것 (변수 개수 상관 없음)
- A → aV1V2...Vk

제일 왼쪽 symbol 이외의 symbol들은 전부 변수로 대체  
일반화시키기 어려움

- very good for parsing
- It is hard to find the Greibach normal form of any context-free grammar

## 3. Membership Algorithm
문자열이 grammar로 유도될 수 있는지 찾는 알고리즘

### 1) CKY Algorithm 구현
```java
private static int ruleCount = 0;
private static HashMap<String, ArrayList<String>> ruleMap = new HashMap<>();
private static String w;	
```

#### ㄱ. production rule 입력
```java
Scanner sc = new Scanner(System.in);
System.out.print("규칙의 개수를 입력하세요=>");
ruleCount = sc.nextInt(); // production rule 개수 입력
sc.nextLine();

System.out.println(ruleCount + "개의 규칙을 입력하세요");

for (int i=0;i<ruleCount; i++) {
	String[] line = sc.nextLine().split(">");
	if (line.length == 2) {
		String key = line[1];
		ArrayList<String> vars = ruleMap.get(key.trim());
		if (vars == null) {
			vars = new ArrayList<String>();
			vars.add(line[0].trim());
			ruleMap.put(key, vars);
		} else {
			vars.add(line[0].trim());
		}
	} else {
		// wrong input
	}
}
```
우변을 key 값으로 설정하고 key에 해당하는 변수 리스트가 없는 경우 새로 생성하여 저장하고 해당하는 변수 리스트가 있는 경우 기존에 있던 변수 리스트에 변수를 추가한다.

#### ㄴ. key값 생성함수
```java
private static int makeKey(int i, int j, int len) {
	return (i * len) + j;
}
```

#### ㄷ. V(ij) 구하기
```java
HashMap<Integer, ArrayList<String>> parseVarMap = new HashMap<>();
System.out.println("멤버 확인이 필요한 문자열을 입력하세요.");
w = sc.nextLine().trim(); // 문자열 입력
int wlen = w.length(); // 문자열 길이
		
for (int len = 1; len <= wlen; len++) {
	for (int i = 1, j = len; j <= wlen; i++, j++) {
		int newKey = makeKey(i, j, wlen);
		ArrayList<String> newVars = new ArrayList<>();
		
		if (len == 1) {
			String findKey = w.substring(i-1,i); // 문자열의 i번째 symbol
			ArrayList<String> ruleVar = ruleMap.get(findKey); // symbol을 만들 수 있는 변수 집합
			if (ruleVar != null && !ruleVar.isEmpty()) {
				for (String var : ruleVar) {
					newVars.add(var);
				}
				parseVarMap.put(newKey, newVars); // V(ii) 저장
			}
		} else {
			for (int k=i; k<j; k++) {
				int key1 = makeKey(i, k, wlen); // V(i,k)의 key 값
				int key2 = makeKey(k+1, j, wlen); // V(k+1,j)의 key 값
				
				// 모든 V(i,k)V(K+1,j)에 대해 존재하는 rule 찾기
				for (String var1 : parseVarMap.get(key1)) {
					for (String var2 : parseVarMap.get(key2)) {
						String findKey = var1 + var2; // V(i,k)V(k+1,j)
						ArrayList<String> ruleVar = ruleMap.get(findKey);
						if (ruleVar != null && !ruleVar.isEmpty()) {
							for (String var : ruleVar) {
								if (!newVars.contains(var)) newVars.add(var);
							}
						}
					}
				}
				parseVarMap.put(newKey, newVars); // V(ij) 저장
			}
		}
	}
}
```
V(11)부터 최종 변수 집합까지 substring의 길이를 1씩 늘려가면서 V(ij)를 구한다.  
V(i,k)V(k+1,j)를 만드는 rule이 존재하는 경우 변수 리스트에 추가한다.  

#### ㄹ. 최종 결과 확인
```java
int lastKey = makeKey(1, wlen, wlen);
boolean isAccept = false;
for (String var : parseVarMap.get(lastKey)) {
	if (var.contains("S")) {
		isAccept = true;
		break;
	}
}

if (isAccept) System.out.println("Accept");
else System.out.println("Reject");
sc.close();
```
최종 변수 리스트에 S가 있는지 확인한다.  
- S가 포함된 경우 ACCEPT
- S가 포함되지 않은 경우 REJECT
