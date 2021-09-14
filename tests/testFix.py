functionList = [
    "tan", "cos", "sin", "log", "ln", "sqrt", "sinh", "cosh", "tanh", "asin", "acos", "atan", "power"
]
symbolList = ["pi", "**", "Ans"] + functionList

from src.whiteCalculator.maths import *



i = None
while i != "q":
    try:
        i = fix(input("Input: "))
    except Exception as error:
        i = error
    print("Output: "+str(i))
