---
icon: function

---


# Formula
> _class_ Formula(**options)
- [Attributes(Optional)](#attributes)
  - [skipError](#skiperror)
  - [useEval](#useeval)
  - [showEquation](#showequation)
- [Class(Formulas)](#class-formulas)
  - [`class` PythagorasTheorem](#pythagorastheorem)
    - [`def` getA](#geta-b-c)
    - [`def` getB](#getb-a-c)
    - [`def` getC](#getc-a-b)
  - [`class` LensFormula](#lensformula)
    - [`def` getU](#getu-v-f)
    - [`def` getV](#getv-u-f)
    - [`def` getF](#getf-u-v)
  - [`class` LinearMagnificationFormula](#linearmagnificationformula)
    - [`class` getM](#classs-getm)
      - [`def` byHeight](#byheight-i-h)
      - [`def` byDistance](#bydistance-v-u)
    - [`def` getO](#geto-m-i)
    - [`def` getI](#geti-m-o)
    - [`def` getV](#getv-m-u)
    - [`def` getU](#getu-m-v)


## How to use?
```python
from whiteCalculator import Formula
Formula.{Formula}.{function}(args)
```
### Example
```python
>>> from whiteCalculator import Formula
>>> Formula.PythagorasTheorem.getC(a=3, b=4)
5
```

## Attributes
> ### **.skipError**
> Decide should this calculator use Exception to traceback error.
> Same and see more at [Calculator().skipError](Calculator.md#skiperror)
> ### **.useEval**
> Decide should this calculator use [eval](https://docs.python.org/3/library/functions.html#eval) to calculate. 
> Same and see more at [Calculator().useEval](Calculator.md#useeval)
> ### **.showEquation**
> Decide should this calculator print equation when calculated. 
> Same and see more at [Calculator().showEquation](Calculator.md#showEquation)

## Class(Formulas)

> ### PythagorasTheorem
> $$
> a^2 + b^2 = c^2
> $$
- #### **getA** (b, c)
  - **Parameters**
    - **b** (int **or** float **or** str(equation)) - length of perpendicular
    - **c** (int **or** float **or** str(equation)) - length of hypotenuse
  - **Returns**
    - length of base
  - **Return Type**
    - [.ans](Calculator.md#ans) **or** [str](https://docs.python.org/3/library/functions.html#str)(errors)

- #### **getB** (a, c)
  - **Parameters**
    - **a** (int **or** float **or** str(equation)) - length of base
    - **c** (int **or** float **or** str(equation)) - length of hypotenuse
  - **Returns**
    - length of perpendicular
  - **Return Type**
    - [.ans](Calculator.md#ans) **or** [str](https://docs.python.org/3/library/functions.html#str)(errors)

- #### **getC** (a, b)
  - **Parameters**
    - **a** (int **or** float **or** str(equation)) - length of base
    - **b** (int **or** float **or** str(equation)) - length of perpendicular
  - **Returns**
    - length of hypotenuse
  - **Return Type**
    - [.ans](Calculator.md#ans) **or** [str](https://docs.python.org/3/library/functions.html#str)(errors)

> ### LensFormula
> $$
> \frac{1}{u} + \frac{1}{v} = \frac{1}{f}
> $$
- #### **getU** (v, f)
  - **Parameters**
    - **v** (int **or** float **or** str(equation)) - images distance
    - **f** (int **or** float **or** str(equation)) - focus length
  - **Returns**
    - object distance
  - **Return Type**
    - [.ans](Calculator.md#ans) **or** [str](https://docs.python.org/3/library/functions.html#str)(errors)

- #### **getV** (u, f)
  - **Parameters**
    - **u** (int **or** float **or** str(equation)) - object distance
    - **f** (int **or** float **or** str(equation)) - focus length
  - **Returns**
    - images distance
  - **Return Type**
    - [.ans](Calculator.md#ans) **or** [str](https://docs.python.org/3/library/functions.html#str)(errors)

- #### **getF** (u, v)
  - **Parameters**
    - **u** (int **or** float **or** str(equation)) - object distance
    - **v** (int **or** float **or** str(equation)) - images distance
  - **Returns**
    - focus length
  - **Return Type**
    - [.ans](Calculator.md#ans) **or** [str](https://docs.python.org/3/library/functions.html#str)(errors)

> ### LinearMagnificationFormula
> $$
> m = \frac{h_{i}}{h_{o}} = \frac{v}{u}
> $$
- #### **getM**
  - ##### **byHeight** (i, o)
    - **Parameters**
      - **i** (int **or** float **or** str(equation)) - height of images
      - **o** (int **or** float **or** str(equation)) - height of object
    - **Returns**
      - Magnification of lens
    - **Return Type**
      - [.ans](Calculator.md#ans) **or** [str](https://docs.python.org/3/library/functions.html#str)(errors)

  - ##### **byDistance** (v, u)
    - **Parameters**
      - **v** (int **or** float **or** str(equation)) - images distance
      - **u** (int **or** float **or** str(equation)) - object distance
    - **Returns**
      - Magnification of lens
    - **Return Type**
      - [.ans](Calculator.md#ans) **or** [str](https://docs.python.org/3/library/functions.html#str)(errors)

- #### **getO** (m, i)
    - **Parameters**
      - **m** (int **or** float **or** str(equation)) - Magnification of lens
      - **i** (int **or** float **or** str(equation)) - height of images
    - **Returns**
      - height of object
    - **Return Type**
      - [.ans](Calculator.md#ans) **or** [str](https://docs.python.org/3/library/functions.html#str)(errors)

- #### **getI** (m, o)
    - **Parameters**
      - **m** (int **or** float **or** str(equation)) - Magnification of lens
      - **o** (int **or** float **or** str(equation)) - height of object
    - **Returns**
      - height of images
    - **Return Type**
      - [.ans](Calculator.md#ans) **or** [str](https://docs.python.org/3/library/functions.html#str)(errors)

- #### **getV** (m, u)
    - **Parameters**
      - **m** (int **or** float **or** str(equation)) - Magnification of lens
      - **u** (int **or** float **or** str(equation)) - object distance
    - **Returns**
      - images distance
    - **Return Type**
      - [.ans](Calculator.md#ans) **or** [str](https://docs.python.org/3/library/functions.html#str)(errors)

- #### **getU** (m, v)
    - **Parameters**
      - **m** (int **or** float **or** str(equation)) - Magnification of lens
      - **v** (int **or** float **or** str(equation)) - images distance
    - **Returns**
      - object distance
    - **Return Type**
      - [.ans](Calculator.md#ans) **or** [str](https://docs.python.org/3/library/functions.html#str)(errors)









