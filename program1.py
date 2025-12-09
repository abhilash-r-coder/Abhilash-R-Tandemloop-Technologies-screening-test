class Calculator:
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def multiplication(self, a, b):
        return a * b

    def division(self, a, b):
        try:
            return a / b
        except Exception as e:
            return e


cal = Calculator()
is_cal = True

while is_cal:

    try:
        a = float(input("Enter value of A:"))
        b = float(input("Enter value of B: "))
    except ValueError:
        print("Invalid number! Try again.\n")
        continue

    type_of_operation = input("Enter operation (+, -, *, /) or 'exit' to quit: ")

    if type_of_operation.lower() == "exit":
        print("Calculator exited.")
        break

    if type_of_operation == "+":
        print("Result:", cal.add(a, b))

    elif type_of_operation == "-":
        print("Result:", cal.sub(a, b))

    elif type_of_operation == "*":
        print("Result:", cal.multiplication(a, b))

    elif type_of_operation == "/":
        print("Result:", cal.division(a, b))

    else:
        print("Invalid operation! Enter +, -, *, or /")
