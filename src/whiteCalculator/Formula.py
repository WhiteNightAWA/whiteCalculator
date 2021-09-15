from .calculator import Calculator

mainCalculator = Calculator(
        skipError=True
)


class Formula:
    """
    A _ of formulas\n
    ----------\n
    FORMULAS:
        * Pythagoras Theorem
        * Lens Formula
    """
    # f1 = QuadraticEquation
    # f2 = CosineTheorem
    # f3 = HeronFormula

    # @classmethod
    # def QuadraticEquation(cls, a: [int, float, str], b: [int, float, str], c: [int, float, str]):
    #
    #     """
    #     Quadratic Equation\n
    #     Example: QuadraticEquation(1, -2, 1) => return (1, 1)
    #
    #     :param a: value of a
    #     :param b: value of a
    #     :param c: value of a
    #     :return: positive result, negative result
    #     """
    #
    #     x1 = cls.calculator.run(f"(-({b})+sqrt((({b})^(2))-4*({a})*({c})))/(2*({a}))")
    #     x2 = cls.calculator.run(f"(-({b})-sqrt((({b})^(2))-4*({a})*({c})))/(2*({a}))")
    #     return x1, x2
    #
    # @classmethod
    # def CosineTheorem(cls, b: [int, float, str], c: [int, float, str], Ø: [int, float, str]):
    #
    #     """
    #     Law of Cosines
    #
    #     Example: CosineTheorem(6, 6, 60) => return 6
    #
    #     :param b: sides b
    #     :param c: sides c
    #     :param Ø: angle Ø
    #     :return: sides a
    #     """
    #
    #     a = cls.calculator.run(f"sqrt({c}^2+{b}^2-2*{b}*{c}*cos({Ø}))")
    #     return a
    #
    # @classmethod
    # def HeronFormula(cls, a: [int, float, str], b: [int, float, str], c: [int, float, str]):
    #
    #     """
    #     Heron's Formula
    #
    #     Example: HeronFormula(4, 13, 15) => return 24
    #
    #     :param a: sides a
    #     :param b: sides b
    #     :param c: sides c
    #     :return: Area
    #     """
    #
    #     A = cls.calculator.run(f"0.25*sqrt(({a}+{b}+{c})*(-{a}+{b}+{c})*({a}-{b}+{c})*({a}+{b}-{c}))")
    #     return A

    class PythagorasTheorem:
        """
        Pythagoras Theorem
        ----------
        a² + b² = c²
        ----------
        ----------\n
        PARAMS:
            * a = length of base\n
            * b = length of perpendicular\n
            * c = length of hypotenuse\n
        ----------\n
        FUNCTIONS:
            * def getA(b, c):
                return the value of a
            * def getB(a, c):
                return the value of b
            * def getC(b, c):
                return the value of c
        """

        @classmethod
        def getA(cls, b, c):
            """
            :param b: length of perpendicular
            :param c: length of hypotenuse
            :return: a: length of base
            """
            a = mainCalculator.run(f"sqrt((({c})^2)-(({b})^2))")
            return a

        @classmethod
        def getB(cls, a, c):
            """
            :param a: length of base
            :param c: length of hypotenuse
            :return: b: length of perpendicular
            """
            b = mainCalculator.run(f"sqrt((({c})^2)-(({a})^2))")
            return b

        @classmethod
        def getC(cls, a, b):
            """
            :param a: length of base
            :param b: length of perpendicular
            :return: c: length of hypotenuse
            """
            c = mainCalculator.run(f"sqrt((({a})^2)+(({b})^2))")
            return c

    class LensFormula:
        """
        Lens Formula
        ----------
        1/u + 1/v = 1/f
        ----------
        ----------\n
        PARAMS:
            * u = object distance
            * v = image distance
            * f = focus length
        ----------\n
        FUNCTIONS:
            * getU(v, f):
                return the value of object distance
            * getV(u, f):
                return the value of image distance
            * getF(u, v):
                return the value of focus length
        """

        @classmethod
        def getU(cls, v, f):
            """
            :param v: image distance
            :param f: focus length
            :return: u: object distance
            """
            u = mainCalculator.run(f"1/((1/({f})-(1/({v}))))")
            return u

        @classmethod
        def getV(cls, u, f):
            """
            :param u: object distance
            :param f: focus length
            :return: u: image distance
            """
            v = mainCalculator.run(f"1/((1/({f})-(1/({u}))))")
            return v

        @classmethod
        def getF(cls, u, v):
            """
            :param u: object distance
            :param v: image distance
            :return: u: focus length
            """
            f = mainCalculator.run(f"1/((1/({u})+(1/({v}))))")
            return f

    class LinearMagnificationFormula:
        """
        Linear Magnification Formula
        ----------
        m = hᵢ/hₒ = v/u
        ----------
        ----------\n
        PARAMS:
            * m = Magnification of lens
            * hₒ = height of object
            * hᵢ = height of image
            * u = object distance
            * v = image distance
        ----------\n
        CLASS:
            * getM => get Magnification of lens
                * byHeight(o, i):
                    return m

                * byDistance(u, v):
                    return m
        """

        class getM:
            """
            Get Magnification of lens\n
            ----------\n
            FUNCTIONS:
                * byHeight(o, i):
                    return m
                * byDistance(u, v):
                    return m
            """

            @classmethod
            def byHeight(cls, o, i):
                """
                :param o: height of object
                :param i: height of image
                :return: m: Magnification of lens
                """
                m = mainCalculator.run(f"({o})/({i})")
                return m

            @classmethod
            def byDistance(cls, u, v):
                """
                :param u: object distance
                :param v: image distance
                :return: m: Magnification of lens
                """
                m = mainCalculator.run(f"({v})/({u})")
                return m

        class getI:

            @classmethod
            def byDistance(cls, v):
                pass

            @classmethod
            def byMagnification(cls, m, o):
                pass

        class getO:

            @classmethod
            def byDistance(cls, u):
                pass

            @classmethod
            def byMagnification(cls, m, i):
                pass

        class getV:

            @classmethod
            def byHeight(cls, i):
                pass

            @classmethod
            def byMagnification(cls, m, u):
                pass

        class getU:

            @classmethod
            def byHeight(cls, o):
                pass

            @classmethod
            def byMagnification(cls, m, v):
                pass

    PT = PythagorasTheorem
    LF = LensFormula
    LMF = LinearMagnificationFormula
