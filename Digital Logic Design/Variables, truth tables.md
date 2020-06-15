# Variables, truth tables

## 1. Truth table

### 1) AND
|x1|x2|L|
|---|---|---|
|0|0|0|
|0|1|0|
|1|0|0|
|1|1|1|

### 2) OR
|x1|x2|L|
|---|---|---|
|0|0|0|
|0|1|1|
|1|0|1|
|1|1|1|

### 3) NOT
|x|L|
|---|---|
|0|1|
|1|0|

### 4) XOR
|x1|x2|L|
|---|---|---|
|0|0|0|
|0|1|1|
|1|0|1|
|1|1|0|

## 2. Variable properties
### 1) Commutative
- x⋅y = y⋅x
- x+y = y+x

### 2) Associative
- x⋅(y⋅z) = (x⋅y)⋅z
- x+(y+z) = (x+y)+z

### 3) Distributive
- x⋅(y+z) = x⋅y + x⋅z
- x+y⋅z = (x+y) ⋅ (x+z)

### 4) Absorption
- x + x⋅y = x
- x⋅(x+y) = x

### 5) Combining
- x⋅y + x⋅y' = x
- (x+y) ⋅ (x+y') = x

### 6) DeMorgan's Theorem
- (x⋅y)' = x' + y'
- (x+y)' = x'⋅y'

### 7)
- x + x'⋅y = x+y
- x⋅(x'+y) = x⋅y