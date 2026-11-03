
import sympy as sp

t = sp.symbols('t')

s = t**3 - 6*t**2 + 9*t + 5

v = sp.diff(s, t)
a = sp.diff(v, t)

print("Velocity:", v)
print("Acceleration:", a)

print("At Rest:", sp.solve(v, t))

d = sp.integrate(s, (t, 0, 2))
print("Displacement Integral:", d)
