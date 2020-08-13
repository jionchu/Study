# json

```python
json = []
json.append({'start':0,'end':2})
json.append({'start':3,'end':6})
```
dictionary 형식으로 json object를 생성한다.
```python
json = json.dumps(json, indent=4)
json
```
```
[
    {
        'start': 0,
        'end': 2
    },
    {
        'start': 3,
        'end': 6
    }
]
```