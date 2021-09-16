from .maths import *
from .ERRORS import *
from .timeout import timeout

functionList = [
    "tan(", "cos(", "sin(", "log(", "ln(", "sqrt(", "sinh(", "cosh(", "tanh(", "asin(", "acos(", "atan(", "power("
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

    def __init__(self,
                 skipError: bool = True,
                 useEval: bool = True,
                 showEquation: bool = False
                 ):
        """
        :param skipError:
        :param useEval:
        """
        self.ans = 0
        self.equation = ""
        self.equationList = []
        self.ERROR = None
        self.skipError = skipError
        self.useEval = useEval
        self.showEquation = showEquation

    def getList(self):
        lastNumber, tryAdd = "", ""
        self.equationList.clear()
        for symbol in self.equation:
            if symbol.isnumeric() or symbol == ".":
                lastNumber += symbol
                if tryAdd != "" and tryAdd not in symbolList:
                    return f"ERROR: '{tryAdd + symbol}'"
                tryAdd = ""
            elif symbol.isalpha() or tryAdd + symbol in functionList:
                tryAdd += symbol
                if lastNumber != "":
                    self.equationList.append(lastNumber)
                lastNumber = ""
            else:
                if lastNumber != "":
                    self.equationList.append(lastNumber)
                self.equationList.append(symbol)
                lastNumber, tryAdd = "", ""
            if tryAdd in symbolList:
                self.equationList.append(tryAdd)
                tryAdd = ""
        if lastNumber != "":
            self.equationList.append(lastNumber)

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

    def calculate(self):

        def lookup():
            pass

        leftBrackets = self.equation.count("(")
        rightBrackets = self.equation.count(")")
        if leftBrackets > rightBrackets:
            addBrackets = leftBrackets - rightBrackets
            self.equation += ")" * addBrackets
        elif leftBrackets < rightBrackets:
            return "ERROR: BracketsError (rightBrackets < leftBrackets)"
        for x in replaceList:
            self.equation = self.equation.replace(x, replaceList[x])
        lastNum, lastSym, equationList = "", "", []
        for symbol in self.equation:
            if symbol.isalpha() or lastSym+symbol in symbolList:
                if lastSym+symbol in symbolList:
                    equationList.append(lastSym+symbol)
                    lastSym = ""
                    symbol = None
                if lastNum != "":
                    equationList.append(lastNum)
                    lastNum = ""
                if symbol is not None:
                    lastSym += symbol
            elif symbol in "(+-*/)":
                if lastSym != "":
                    if lastSym in symbolList:
                        equationList.append(lastSym)
                        lastSym = ""
                    else:
                        return f"ERROR: Unknown function/equation: '{lastSym + symbol}'"
                if lastNum != "":
                    equationList.append(lastNum)
                    lastNum = ""
                equationList.append(symbol)
            elif symbol.isnumeric() or symbol in ".":
                if lastSym != "":
                    if lastSym in symbolList:
                        equationList.append(lastSym)
                        lastSym = ""
                    else:
                        return f"ERROR: Unknown function/equation: '{lastSym + symbol}'"
                lastNum += symbol
        if lastSym != "":
            if lastSym in symbolList:
                equationList.append(lastSym)
            else:
                return f"ERROR: Unknown function/equation: '{lastSym}'"
        if lastNum != "":
            equationList.append(lastNum)
        for count, sym in enumerate(equationList):
            if count + 1 != len(equationList):
                if sym not in "(+-*/" and "(" not in sym:
                    if equationList[count + 1] not in "+-*/)":
                        equationList.insert(count + 1, "*")
        if self.showEquation:
            print("".join(equationList))
        if self.useEval:
            Ans = self.ans
            if self.skipError:
                try:
                    ans = eval("".join(equationList))
                except Exception as error:
                    return f"Error: {error}"
                else:
                    return ans
            else:
                return eval("".join(equationList))
        else:
            def run(toCalculateFunc, symFunc, countFunc):
                if symFunc == "*":
                    if "**" not in "".join(toCalculateFunc):
                        toCalculateFunc[countFunc] = str(
                            int(toCalculateFunc[countFunc - 1]) * int(toCalculateFunc[countFunc + 1]))
                        toCalculateFunc.pop(countFunc + 1)
                        toCalculateFunc.pop(countFunc - 1)
                    else:
                        pass
                elif symFunc == "/":
                    toCalculateFunc[countFunc] = str(
                        int(toCalculateFunc[countFunc - 1]) / int(toCalculateFunc[countFunc + 1]))
                    toCalculateFunc.pop(countFunc + 1)
                    toCalculateFunc.pop(countFunc - 1)
                elif symFunc == "-":
                    toCalculateFunc[countFunc] = str(
                        int(toCalculateFunc[countFunc - 1]) - int(toCalculateFunc[countFunc + 1]))
                    toCalculateFunc.pop(countFunc + 1)
                    toCalculateFunc.pop(countFunc - 1)
                elif symFunc == "+":
                    toCalculateFunc[countFunc] = str(
                        int(toCalculateFunc[countFunc - 1]) + int(toCalculateFunc[countFunc + 1]))
                    toCalculateFunc.pop(countFunc + 1)
                    toCalculateFunc.pop(countFunc - 1)
                return toCalculateFunc, symFunc, countFunc

            while len(equationList) != 1:
                while "(" in equationList:
                    lastOpen, firstClose = None, None
                    for count, sym in enumerate(equationList):
                        if sym == "(" and firstClose is None:
                            lastOpen = count
                        if firstClose is None and sym == ")":
                            firstClose = count
                    toCalculate = equationList[(lastOpen + 1):firstClose]
                    print(toCalculate)
                    lastSym = None
                    while len(toCalculate) != 1:
                        for count, sym in enumerate(toCalculate):
                            toCalculate, sym, count = run(toCalculate, sym, count)
                else:
                    while len(equationList) != 1:
                        for count, sym in enumerate(equationList):
                            equationList, sym, count = run(equationList, sym, count)
            return "".join(equationList)

    def run(self, equation: [str, bytes]):
        self.equation = equation.replace(" ", "")
        with timeout(seconds=10):
            res = self.calculate()
        if "ERROR:" in str(res):
            return res
        else:
            self.ans = res
            if isinstance(self.ans, float):
                if self.ans.is_integer():
                    self.ans = int(self.ans)
            return self.ans
