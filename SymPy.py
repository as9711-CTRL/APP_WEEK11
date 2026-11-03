
import sympy as sp

x = sp.symbols('x')

expr = (x + 2)**2

print("Expanded:", sp.expand(expr))
print("Factorized:", sp.factor(x**2 + 5*x + 6))
print("Simplified:", sp.simplify((x**2 - 1)/(x - 1)))

eq = x**2 - 5*x + 6
print("Roots:", sp.solve(eq, x))
