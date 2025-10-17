import math

class Secante:
    def __init__(self, f, x0, x1, tol, nmax):
        self.f = f
        self.x0 = x0
        self.x1 = x1
        self.tol = tol
        self.nmax = nmax

    def resolver(self):
        for i in range(self.nmax):
            f0, f1 = self.f(self.x0), self.f(self.x1)
            if f1 - f0 == 0:
                print("Error: division por cero.")
                return
            x2 = self.x1 - f1 * (self.x1 - self.x0) / (f1 - f0)
            if abs(x2 - self.x1) < self.tol:
                print(f"Convergio en {i+1} iteraciones: x ≈ {x2:.6f}")
                return
            self.x0, self.x1 = self.x1, x2
        print("No convergio.")

f = lambda x: eval(input("Ingrese f(x): "))    
x0 = float(input("x0: "))
x1 = float(input("x1: "))
tol = float(input("tolerancia: "))
nmax = int(input("numero máximo de iteraciones: "))

metodo = Secante(f, x0, x1, tol, nmax)
metodo.resolver()
