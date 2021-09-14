from .calculator import Calculator


class Formula:

    def __init__(self):
        self.calculator = Calculator()

    def QuadraticEquation(self, a: int, b: int, c: int):
        x1 = self.calculator.run(f"(-({b})+sqrt((({b})**(2))-4*({a})*({c})))/(2*({a}))")
        x2 = self.calculator.run(f"(-({b})-sqrt((({b})**(2))-4*({a})*({c})))/(2*({a}))")
        return x1, x2

