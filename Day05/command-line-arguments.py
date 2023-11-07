import sys    # Here sys is the module, it will installed inbuilt, just  we are calling the argument.

def add(num1, num2):  # Here 1)Keywords = def. --> 2)functions = add, sub, mul, division --> 3)Datatypes = float.
    add = num1 + num2
    return add  # Return is the statement to return the result of the given programm.


def sub(num1, num2):
    s = num1 - num2
    return s

def mul(num1, num2):
    m = num1 * num2
    return m

def division(num1, num2):
    div = num1 / num2
    return div

num1 = float(sys.argv[1])
operation = sys.argv[2]
num2 = float(sys.argv[3])

if operation == "add":  # Desired operations = operations.
   output = add(num1, num2)
   print(output)


if operation == "sub":
   output = sub(num1, num2)
   print(output)


if operation == "mul":
   output = mul(num1, num2)
   print(output)


if operation == "division":
   output = division(num1, num2)
   print(output)

