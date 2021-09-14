
from src.whiteCalculator.Formula import Formula

f = Formula()

i = None
while i != "q":
    i = input("Input: ")
    args = []
    for arg in eval(f"f.{i}.__code__.co_varnames[:f.{i}.__code__.co_argcount]"):
        if arg != "self":
            args.append(input(arg+": "))
    print(eval(f"f.{i}(*args)"))

