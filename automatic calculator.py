# Simple Calculator


num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))
def calculate(operator):

    if operator == "+":
        return( num1 + num2)

    elif operator == "-":
        return( num1 - num2)

    elif operator == "*":
        return( num1 * num2)

    elif operator == "/":
        if num2 != 0:
            return( num1 / num2)
        else:
            return("Error: Division by zero!")
        exit()
    else:
        return("sorry")
    
result= calculate(operator)
print( "Result",result)