from src.whiteCalculator import Calculator, Formula

c = Calculator(skipError=True)
f = Formula()

i = None
while i != "q":
    i = c.run(input("Input: "))
    run = f.run(int(i))
    i = run()
    print("Output: "+str(i))
