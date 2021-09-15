> # Calculator Module for Python
> By White Night
## Install
```shell
# Linux/macOS
python3 -m pip install -U whiteCalculator

# Windows
py -3 -m pip install -U whiteCalculator
```


# QuickStart
### Calculator
```python
>>> from whiteCalculator import Calculator
>>> c = Calculator()
>>> print(c.run("1+8(5^2)"))
201
>>> print(c.run("9Ans"))
1809
```
### Formula
```python
>>> from whiteCalculator import Formula
>>> f = Formula()
>>> print(f.f2(6, 6, 60))
6
>>> print(f.QuadraticEquation(1, -2, 1))
(1, 1)
```


## Errors
```python
>>> from whiteCalculator import Calculator

>>> c2 = Calculator() # Default is True
>>> c2.run("9/0")
Error: division by zero

>>> c1 = Calculator(skipError=False)
>>> c1.run("9/0")
Traceback (most recent call last):
    ...
ZeroDivisionError: division by zero
```

## Links
> [GitHub](https://github.com/WhiteNightAWA/whiteCalculator/)
> [Pypi](https://pypi.org/project/whiteCalculator/)

## You can use:
- sin / asin / sinh
- cos / acos / cosh
- tan / atan / tanh
- ln / log
- × / •
- ^ / ** / power
- √ / sqrt
- π / pi
- %
- ÷
- Ans