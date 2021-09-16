# QuickStart
### Calculator
```python
from whiteCalculator import Calculator
c = Calculator()
print(c.run("1+8(5^2)"))
# Output: 201
print(c.run("9Ans"))
# Output: 1809
```
### Formula
```python
from whiteCalculator import Formula
Formula.PythagorasTheorem.getA(b=4, c=5)
# Output: 3
Formula.PythagorasTheorem.getA(b="2^2", c="√(25)")
# Output: 3
```
#### Formula List
```python
PythagorasTheorem, LensFormula, LinearMagnificationFormula
```