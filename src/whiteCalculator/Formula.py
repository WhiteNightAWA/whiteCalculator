from .calculator import Calculator


class Formula:

    def __init__(self):

        """
        Formulas

        f1 = QuadraticEquation = Quadratic Equation\n
        f2 = Law of Cosines = CosineTheorem\n
        f3 = Heron's Formula = HeronFormula\n

        """

        self.calculator = Calculator()
        self.f1 = self.QuadraticEquation
        self.f2 = self.CosineTheorem
        self.f3 = self.HeronFormula

    def QuadraticEquation(self, a: float, b: float, c: float):

        """
        Quadratic Equation\n
        Example: QuadraticEquation(1, -2, 1) => return (1, 1)

        :param a: value of a
        :param b: value of a
        :param c: value of a
        :return: (positive result, negative result)
        """

        x1 = self.calculator.run(f"(-({b})+sqrt((({b})^(2))-4*({a})*({c})))/(2*({a}))")
        x2 = self.calculator.run(f"(-({b})-sqrt((({b})^(2))-4*({a})*({c})))/(2*({a}))")
        return x1, x2

    def CosineTheorem(self, b: float, c: float, Ø: float):

        """
        Law of Cosines

        Example: CosineTheorem(6, 6, 60) => return 6

        :param b: sides b
        :param c: sides c
        :param Ø: angle Ø
        :return: sides a
        """

        a = self.calculator.run(f"sqrt({c}^2+{b}^2-2*{b}*{c}*cos({Ø}))")
        return a

    def HeronFormula(self, a: float, b: float, c: float):

        """
        Heron's Formula

        Example: HeronFormula(4, 13, 15) => return 24

        :param a: sides a
        :param b: sides b
        :param c: sides c
        :return: Area
        """

        A = self.calculator.run(f"0.25*sqrt(({a}+{b}+{c})*(-{a}+{b}+{c})*({a}-{b}+{c})*({a}+{b}-{c}))")
        return A
