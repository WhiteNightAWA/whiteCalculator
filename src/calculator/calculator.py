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

    def checkBrackets(self):
        leftBrackets = self.equation.count("(")
        rightBrackets = self.equation.count(")")
        if leftBrackets > rightBrackets:
            addBrackets = leftBrackets - rightBrackets
            self.equation += ")" * addBrackets
        if leftBrackets < rightBrackets:
            self.ERROR = SyntaxError

    def getList(self):
        last, tryAdd = "", ""
        self.equationList.clear()
        for symbol in self.equation:
            if symbol.isnumeric() or symbol == ".":
                last += symbol
                if tryAdd in symbolList:
                    self.equationList.append(tryAdd)
                tryAdd = ""
            elif symbol.isalpha():
                tryAdd += symbol
                if last != "":
                    self.equationList.append(last)
                last = ""
            else:
                if last != "":
                    self.equationList.append(last)
                if tryAdd in symbolList:
                    self.equationList.append(tryAdd)

                self.equationList.append(symbol)
                last, tryAdd = "", ""
        if last != "":
            self.equationList.append(last)
        if tryAdd in symbolList:
            self.equationList.append(tryAdd)

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

    def getAns(self):
        Ans = self.ans
        self.ans = eval(self.equation)
        return self.ans

    def replaces(self):
        for x in replaceList:
            self.equation = self.equation.replace(x, replaceList[x])

    def run(self, equation: str):
        self.equation = equation.replace(" ", "")
        self.checkBrackets()
        self.replaces()
        self.getList()
        self.fixList()
        self.equation = "".join(self.equationList)
        self.getAns()
        if isinstance(self.ans, float):
            if self.ans.is_integer():
                self.ans = int(self.ans)
        if self.ERROR is None:
            return self.ans
        else:
            return self.ERROR
