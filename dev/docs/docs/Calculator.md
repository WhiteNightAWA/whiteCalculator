---
prev: ../
next: 
  text: Formula
  link: ./Formula/
icon: calculate
title: Calculator
---
# Calculator
> _class_ Calculator(skipError, useEval, showEquation)
- [Attributes](#attributes)
  - [ans](#ans)
  - [equation](#equation)
  - [ERROR](#error)
  - [skipError](#skiperror)
  - [useEval](#useeval)
  - [showEquation](#showequation)
- Methods
  - [`async` calculate](#await-calculate-equation)
  - [`def` calculateEquation](#calculateequation)
  - [`def` run](#runequation)
  - [`def` getAns](#getans)
  - [`def` getList](#getlist)
  - [`def` fix](#fix)
  - [`def` fixList](#fixlist)

Represents a Calculator.
***
## Attributes
> ### **.ans** 
> The prev answer of this calculator.
- **Type**
  - [int](https://docs.python.org/3/library/functions.html#int) **or** [float](https://docs.python.org/3/library/functions.html#float)
***
> ### **.equation**
> The prev equation of this calculator.
- **Type**
  - [str](https://docs.python.org/3/library/functions.html#str)
***
> ### **.skipError**
> Decide should this calculator use Exception to traceback error.
- **Type**
  - [bool](https://docs.python.org/3/library/functions.html#bool)
- **Default**
  - `true`
- **Example**

<CodeGroup>
  <CodeGroupItem title="True">

```python
>>> Calculator(skipError=True).run("1/0")
# Output: "Error: division by zero"
```

  </CodeGroupItem>

  <CodeGroupItem title="False">

```python
>>> Calculator(skipError=False).run("1/0")
# Outputs:
# Traceback (most recent call last):
#     ...
# ZeroDivisionError: division by zero
```

  </CodeGroupItem>
</CodeGroup>

***
> ### **.useEval**
> Decide should this calculator use [eval](https://docs.python.org/3/library/functions.html#eval) to calculate. 
- **Type**
  - [bool](https://docs.python.org/3/library/functions.html#bool)
- **Default**
  - `false`
- **P.S.**
  - `false`: Faster
  - `true`: Safer
***
> ### **.showEquation**
> Decide should this calculator print equation when calculated. 
- **Type**
  - [bool](https://docs.python.org/3/library/functions.html#bool)
- **Default**
  - `false`
- **Example**

<CodeGroup>
  <CodeGroupItem title="True">

```python
>>> Calculator(showEquation=True).run("90(64(9")
# Output:
# 90*(64*(9))
# 51840
```

  </CodeGroupItem>

  <CodeGroupItem title="False">

```python
>>> Calculator(showEquation=False).run("90(64")
# Output: 51840
```

  </CodeGroupItem>
</CodeGroup>

***
## Methods
> ### _await_ **calculate(equation)**
> calculate the `equation` (same as [`def` run()](#runequation))
- **Parameters**
  - **equation** ([str](https://docs.python.org/3/library/functions.html#str)) - the equation you want to calculate. <br>(You can use [these](/docs/Others/#all-symbols-and-functions-you-can-use-in-calculator) symbol)
- **Returns**
  - answer or error of the equation
- **Return type**
  - [.ans](#ans) **or** [str(errors)](https://docs.python.org/3/library/functions.html#str)
***
> ### **calculateEquation()**
> old codes
***
> ### **run(equation)**
> calculate the `equation`
- **Parameters**
  - **equation** ([str](https://docs.python.org/3/library/functions.html#str)) - the equation you want to calculate.<br>(You can use [these](/docs/Others/#all-symbols-and-functions-you-can-use-in-calculator) symbol)
- **Return**
  - [.ans](#ans) - answer of the equation
- **Return type**
  - [.ans](#ans) **or** [str](https://docs.python.org/3/library/functions.html#str)(errors)
***
> ### **getAns()**
> old codes
***
> ### **getList()**
> old codes
***
> ### **fix()**
> old codes
***
> ### **fixList()**
> old codes
***
  

