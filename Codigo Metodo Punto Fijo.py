import math

class PuntoFijo:
    def __init__(self, g, x0, tol, nmax):
        self.g = g
        self.x = x0
        self.tol = tol
        self.nmax = nmax

    def resolver(self):
        for i in range(self.nmax):
            x1 = self.g(self.x)
            if abs(x1 - self.x) < self.tol:
                print(f"Convergió en {i+1} iteraciones: x ≈ {x1:.6f}")
                return
            self.x = x1
        print("No convergió.")

g = lambda x: eval(input("Ingrese g(x): "))     
x0 = float(input("x0: "))
tol = float(input("tolerancia: "))
nmax = int(input("número máximo de iteraciones: "))

metodo = PuntoFijo(g, x0, tol, nmax)
metodo.resolver()
