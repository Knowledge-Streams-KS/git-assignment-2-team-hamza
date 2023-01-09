from add import add
from subtract import subtract
from Multiply import multiply
from Divide import divide
from module import module
from square_root import square_root 

a = int(input("Enter A value: "))
b = int(input("Enter B value: "))

print("\nAdd: ",add(a,b))
print("Subtract: ",subtract(a,b))
print("Multiply: ",multiply(a,b))
print("Divide: ",divide(a,b))
print("Module: ",module(a,b))
print("Square Root: ",square_root(a))