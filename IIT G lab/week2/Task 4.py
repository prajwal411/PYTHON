#Quadratic Equation Solver
from cmath import sqrt

a=float(input(f"Enter the value of a: "))
b=float(input(f"Enter the value of b: "))
c=float(input(f"Enter the value of c: "))
d=b**2 -4*a*c
x1=(-b+sqrt(d))/2*a
x2=(-b-sqrt(d))/2*a
print(f"Solutions are {x1} and {x2}")