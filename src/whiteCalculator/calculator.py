import asyncio
from .maths import *
from .timeout import timeout


functionList = [
    "tan", "cos", "sin", "log", "ln", "sqrt", "sinh", "cosh", "tanh", "asin", "acos", "atan", "power"
]
symbolList = ["pi", "**", "Ans"] + functionList

replaceList = {
    "^": "**",
    "π": "pi",
    "√": "sqrt",
    "%": "/100",
    "×": "*",
    "•": "*",
    "÷": "/"
}


class Calculator:

    def __init__(self, skipError=True):
        self.ans = 0
        self.equation = ""
        self.equationList = []
        self.ERROR = None
        self.skipError = skipError

    def checkBrackets(self):
        leftBrackets = self.equation.count("(")
        rightBrackets = self.equation.count(")")
        if leftBrackets > rightBrackets:
            addBrackets = leftBrackets - rightBrackets
            self.equation += ")" * addBrackets

    def getList(self):
        last, tryAdd = "", ""
        self.equationList.clear()
        for symbol in self.equation:
            if symbol.isnumeric() or symbol == ".":
                last += symbol
                tryAdd = ""
            elif symbol.isalpha():
                tryAdd += symbol
                if last != "":
                    self.equationList.append(last)
                last = ""
            else:
                if last != "":
                    self.equationList.append(last)

                self.equationList.append(symbol)
                last, tryAdd = "", ""
            if tryAdd in symbolList:
                self.equationList.append(tryAdd)
                tryAdd = ""
        if last != "":
            self.equationList.append(last)

    def fixList(self):
        last = "+"
        pointer = 0
        added = 0
        newEquationList = self.equationList.copy()
        for symbol in self.equationList:
            if symbol not in [")", "+", "-", "*", "/"]:
                if last not in ["+", "-", "*", "/", "("] + functionList:
                    newEquationList.insert(pointer + added, "*")
                    added += 1
            last = symbol
            pointer += 1
        self.equationList = newEquationList

    def fix(self):
        last, curr = '+', ''
        result = ''
        for i, char in enumerate(self.equation):
            if char.isnumeric() or char in "(+-*/)":
                if char.isnumeric():
                    if last == ')' or (curr and curr not in functionList):
                        result += '*'
                elif char == '(':
                    if (curr not in functionList) if curr else i and last not in "(+-*/":
                        result += '*'
                curr = ''
            elif char.isalpha():
                if last == ')' or last.isnumeric():
                    result += '*'
                curr += char
            else:
                raise ValueError()
            last = char
            result += char
        self.equation = result

    def getAns(self):
        self.ERROR = None
        Ans = self.ans
        try:
            self.ans = eval(self.equation)
        except Exception as error:
            if self.skipError:
                self.ERROR = error
            else:
                raise error

    def replaces(self):
        for x in replaceList:
            self.equation = self.equation.replace(x, replaceList[x])

    def run(self, equation: str):
        self.equation = equation.replace(" ", "")
        self.checkBrackets()
        self.replaces()
        self.getList()
        self.fixList()
        print(self.equationList)
        self.equation = "".join(self.equationList)
        oldAns, count = self.ans, 0
        with timeout(seconds=10):
            self.getAns()
        if isinstance(self.ans, float):
            if self.ans.is_integer():
                self.ans = int(self.ans)
        if self.ERROR is None:
            return self.ans
        else:
            return "Error: " + str(self.ERROR)
