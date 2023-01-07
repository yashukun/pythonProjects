#Calculator
from art import logo


#Addition
def Add(n1, n2):
    return n1 + n2


#Subtract
def Subtract(n1, n2):
    return n1 - n2


#Multiply
def Multiply(n1, n2):
    return n1 * n2


#Divide
def Divide(n1, n2):
    return n1 / n2


#Dictionary
operations = {"+": Add, "-": Subtract, "*": Multiply, "/": Divide}

#Taking Ipputs
def calculator():
  print(logo)
  
  num1 = float(input("What is you first number."))
  
  for Symbols in operations:
      print(Symbols)
  
  should_continue = True
  
  while should_continue:
      the_Operation = input("Choose Your Operation.")
      num2 = float(input("What is you next number."))
      calculation_function = operations[the_Operation]
      answer = calculation_function(num1, num2)
      print(f"{num1} {the_Operation} {num2} = {answer}")
      if input(f"Type 'y' to continue with {answer} or 'n' to Start new calculation. ") == "y":
          num1 = answer
      else:
          should_continue = False
          calculator()
        
calculator()  
