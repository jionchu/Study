```python
Old: print "The answer is", 2*2
New: print("The answer is", 2*2)
```
```python
Old: print x, # Trailing comma suppresses newline
New: print(x, end=" ") # Appends a space instead of a newline
```
```python
Old: print # Prints a newline
New: print() # You must call the function!
```
```python
Old: print(x,y) # prints repr((x,y))
New: print((x,y)) # Not the same as print(x,y)!
```
