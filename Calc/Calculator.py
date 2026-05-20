import math
num = float(input("Enter a number: "))
result = num
def calc(operator,result,num2=None):
    if operator == "+":
       return result + num2
    elif operator == "-":
        return result - num2
    elif operator == "*":
        return result * num2
    elif operator == "/":
        return result / num2
    elif operator == "sqrt":
        return math.sqrt(result)
while True:
    while True:
        operator = input("Enter what operator to use +, -, *, / , sqrt or 'done' to quit ")
        if operator not in ["+","-","*","/","sqrt" and 'done']:
            print("Enter a valid operator")
        else: break  
    if operator == "done":
            break
    elif operator == "sqrt":
            result = calc(operator, result)
    else:
            num2 = float(input("Enter the next number: "))
            result = calc(operator,result,num2)    
print(f"Result = {result}")
    
