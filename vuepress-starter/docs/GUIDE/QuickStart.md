---
prev:
  text: Installation
  link: /GUIDE/Installation.md
next:
  text: Home
  link: /
---
# Quick Started
## Calculator
```python
from whiteCalculator import Calculator # import the Calculator
c = Calculator()
ans = c.run("1+1")
print(ans)  # Output: 2
```
#### You can use this as your calculator:
```python
print(c.run("50pi(99^6)"))  # Output: 147887356042940.12

print(c.run("Ans/4"))  # Output: 36971839010735.03
```
- [Config of Calculator]()
- [All Symbol you can use Calculator]()

## Formula
```python
from whiteCalculator import Formula # import the Formulas
ans = Formula.PythagorasTheorem.getC(a=3, b=4)
print(ans)  # Output: 5
```
#### You can even calculate it like this:
```python
ans = Formula.LF.getF(u="2^3", v="√(4)") # LF == LensFormula
print(ans)  # Output: 1.6
```
- [List of Formula]()
