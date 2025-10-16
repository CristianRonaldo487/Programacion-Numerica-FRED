class Biseccion:
    def __init__(self):
        self.funcion_str = input("Ingrese la funcion f(x): ")  
        self.a = float(input("Ingrese el límite inferior (a): "))
        self.b = float(input("Ingrese el límite superior (b): "))
        self.tol = float(input("Ingrese la tolerancia: "))

    def f(self, x):
        return eval(self.funcion_str, {"x": x, "__builtins__": {}})

    def resolver(self):
        a, b = self.a, self.b
        
        if self.f(a) * self.f(b) > 0:
            print("Error: No hay cambio de signo en el intervalo.")
            return
        
        print(f"\n{'Iter':<6} {'a':<10} {'b':<10} {'c':<10} {'f(c)':<10} {'Error':<10}")
        print("-" * 60)
        
        iteracion = 0
        while True:
            c = (a + b) / 2
            fc = self.f(c)
            error = abs(b - a)
            iteracion += 1
            
            print(f"{iteracion:<6} {a:<10.5f} {b:<10.5f} {c:<10.5f} {fc:<10.5f} {error:<10.5f}")
            
            if error < self.tol or abs(fc) < self.tol:
                print(f"\nRaiz encontrada: {c:.8f}")
                print(f"  Iteraciones: {iteracion}")
                print(f"  f({c:.8f}) = {fc:.8f}")
                return c
            
            if self.f(a) * fc < 0:
                b = c
            else:
                a = c


print("=" * 60)
print("MÉTODO DE BISECCIÓN")
print("=" * 60)

metodo = Biseccion()
metodo.resolver()
