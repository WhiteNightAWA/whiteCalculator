> # Calculator API for Python
> By White Night
## Install
```shell
# Linux/macOS
python3 -m pip install -U white_calculator

# Windows
py -3 -m pip install -U white_calculator
```


# QuickStart
```python
>>> from white_calculator import Calculator
>>> c = Calculator()
>>> print(c.run("1+8(5^2)"))
201
>>> print(c.run("9Ans"))
1809
```

## Errors
```python
>>> from white_calculator import Calculator

>>> c2 = Calculator() # Default is True
>>> c2.run("9/0")
Error: division by zero

>>> c1 = Calculator(skipError=False)
>>> c1.run("9/0")
Traceback (most recent call last):
    ...
ZeroDivisionError: division by zero
```

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