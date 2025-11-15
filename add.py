try:
  a=float(input("Enter first number"))
  b=float(input("Enter second number"))
  print(f"Addition:{a+b}")
  print(f"Substraction:{a-b}")
  print(f"mMultiplication:{a*b}")
  ifb != 0:
  print(f"division:{a/b}")
else:
  print("division by zero is not allowed")
except ValueError:
  print("Please enter valid numbers.")
