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
        * Linear Magnification Formula
    """

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
            * v = images distance
            * f = focus length
        ----------\n
        FUNCTIONS:
            * getU(v, f):
                return the value of object distance
            * getV(u, f):
                return the value of images distance
            * getF(u, v):
                return the value of focus length
        """

        @classmethod
        def getU(cls, v, f):
            """
            :param v: images distance
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
            :return: u: images distance
            """
            v = mainCalculator.run(f"1/((1/({f})-(1/({u}))))")
            return v

        @classmethod
        def getF(cls, u, v):
            """
            :param u: object distance
            :param v: images distance
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
            * hₒ (o) = height of object
            * hᵢ (i) = height of images
            * u = object distance
            * v = images distance
        ----------\n
        CLASS:
            * getM => get Magnification of lens
                * byHeight(o, i):
                    return m

                * byDistance(u, v):
                    return m
        ----------\n
        FUNCTIONS:
            * getO(m, i):
                return o
            * getI(m, o):
                return i
            * getV(m, u):
                return v
            * getU(m, v):
                return u
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
                :param i: height of images
                :return: m: Magnification of lens
                """
                m = mainCalculator.run(f"({o})/({i})")
                return m

            @classmethod
            def byDistance(cls, u, v):
                """
                :param u: object distance
                :param v: images distance
                :return: m: Magnification of lens
                """
                m = mainCalculator.run(f"({v})/({u})")
                return m

        @classmethod
        def getO(cls, m, i):
            """
            :param m: Magnification of lens
            :param i: height of images
            :return: o: height of object
            """
            o = mainCalculator.run(f"({i})/({m})")
            return o

        @classmethod
        def getI(cls, m, o):
            """
            :param m: Magnification of lens
            :param o: height of object
            :return: i: height of images
            """
            i = mainCalculator.run(f"({m})*({o})")
            return i

        @classmethod
        def getV(cls, m, u):
            """
            :param m: Magnification of lens
            :param u: object distance
            :return: v: images distance
            """
            v = mainCalculator.run(f"({m})*({u})")
            return v

        @classmethod
        def getU(cls, m, v):
            """
            :param m: Magnification of lens
            :param v: images distance
            :return: u: object distance
            """
            u = mainCalculator.run(f"({v})/({m})")
            return u

    PT = PythagorasTheorem
    LF = LensFormula
    LMF = LinearMagnificationFormula
