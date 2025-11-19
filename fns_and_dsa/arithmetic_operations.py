def perform_operation(num1, num2, operation):
     if operation == "add":
        return num1 + num2

     elif operation == "subtract":
         return num1 - num2

     elif operation == "multiply":
         return num1 * num2

     elif operation == "divide":
       if num2 == 0:
         return "Error: Cannot divide by zero."
         return num1 / num2

     else:
         return "Invalid operation. Choose add, subtract, multiply, or divide."
result = perform_operation(5, 6, "add")
print("Result:", result)
Result: 11
result = perform_operation(5, 6, "subtract")
print("Result:", result)
Result: -1
result = perform_operation(5, 6, "multiply")
print("Result:", result)
Result: 30
result = perform_operation(5, 6, "divide")
print("Result:", result)
Result: 0.8333333333333334
