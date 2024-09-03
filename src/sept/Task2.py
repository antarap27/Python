# Create a program , take 2 inputs from the user num1, num2 and give them
#
# max
# pow num1 to num2
# sub, mul, sum, div.
# Format your out with f{""}

Num1 = int(input("Enter num1\n"))
Num2 = int(input("Enter num2\n"))

Max = max(Num1, Num2)
Pow = Num1 ** Num2
Sub = Num1 - Num2
Mul = Num1 * Num2
Sum = Num1 + Num2
Div =Num1 / Num2 if Num2 != 0 else "undefined cannot divide by zero"

print(f"Max of {Num1} and {Num2} is:", Max)
print(f"Pow of {Num1} and {Num2} is:", Pow)
print(f"Sub of {Num1} and {Num2} is:", Sub)
print(f"Mul of {Num1} and {Num2} is:", Mul)
print(f"Sum of {Num1} and {Num2} is:", Sum)
print(f"Div of {Num1} and {Num2} is:", Div)