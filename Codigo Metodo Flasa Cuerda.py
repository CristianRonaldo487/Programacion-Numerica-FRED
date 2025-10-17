import math

class FalsaCuerda:
    def __init__(self, f, a, b, tol, nmax):
        self.f = f
        self.a = a
        self.b = b
        self.tol = tol
        self.nmax = nmax

    def resolver(self):
        fa, fb = self.f(self.a), self.f(self.b)
        if fa * fb > 0:
            print("No hay cambio de signo en el intervalo.")
            return
        for i in range(self.nmax):
            c = self.b - fb * (self.b - self.a) / (fb - fa)
            fc = self.f(c)
            if abs(fc) < self.tol:
                print(f"Convergió en {i+1} iteraciones: x ≈ {c:.6f}")
                return
            if fa * fc < 0:
                self.b, fb = c, fc
            else:
                self.a, fa = c, fc
        print("No convergió.")

f = lambda x: eval(input("Ingrese f(x): "))
a = float(input("a: "))
b = float(input("b: "))
tol = float(input("tolerancia: "))
nmax = int(input("número máximo de iteraciones: "))

metodo = FalsaCuerda(f, a, b, tol, nmax)
metodo.resolver()

