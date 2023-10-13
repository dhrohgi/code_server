# 사칙 연산기

"""
def get_result(a, b, c):
    if c == '+':
        return a + b
    elif c == "-":
        return a - b
    elif c == "*":
        return a * b
    elif c == "/":
        return a / b
    elif c == "exit":
        return

calculating = True

while calculating:
    a = int(input("Choose a number:"))
    b = int(input("Choose another number:"))
    c = input("Choose an operation: \n    Options are: +, -, * or /. \n    Write 'exit' to finish \n")

    result = get_result(a, b, c)
    
    if c == "exit":
        calculating = False
    else:
          print("Result:", result)
    
"""

playing = True
  
# add your code here!

def get_result(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        return a / b
    elif operation == "exit":
        return

while playing:
    a = int(input("Choose a number:\n"))
    b = int(input("Choose another one:\n"))
    operation = input("Choose an operation:\n    Options are: + , - , * or /.\n    Write 'exit' to finish.\n")
    result = get_result(a, b, operation)
    
    if operation == "exit":
        playing = False
    else:
          print("Result:", result)
    