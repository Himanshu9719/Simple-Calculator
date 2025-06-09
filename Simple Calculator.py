Num1 = float(input("Enter First Number:"))
Num2 = float(input("Enter Second Number:"))
operation = input("Enter Operator(+, -, *, /):")

if operation == '+':
    result = Num1 + Num2

elif operation == '-':
    result = Num1 - Num2
    
elif operation == '*':
    result = Num1 * Num2
    
elif operation == '/':
    if Num2 == 0:
        result = "Cannot Be Divided By 0"
    else:
        result = Num1 / Num2
        
else:
    result = "Invalid Operator!"
    
print("Result :" , result)
