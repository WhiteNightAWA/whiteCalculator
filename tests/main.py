from src.white_calculator import Calculator

c = Calculator(skipError=True)

i = None
while i != "q":
    i = c.run(input("Input: "))
    print("Output: "+str(i))
