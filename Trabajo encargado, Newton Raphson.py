class NewtonRaphson:
    def __init__(self, f, df, x0, tol, max_iter):
        self.f = f
        self.df = df
        self.x0 = x0
        self.tol = tol
        self.max_iter = max_iter

    def resolver(self):
        x = self.x0

        for i in range(1, self.max_iter + 1):
            fx = self.f(x)
            dfx = self.df(x)

            if dfx == 0:
                print(f"\nIteracion {i}: la derivada es 0, no se puede continuar.")
                return None

            x_nuevo = x - fx / dfx

            print(f"Iteración {i}: x = {x:.6f}, f(x) = {fx:.6f}")

            if abs(fx) < self.tol:
                print(f"\n Raiz aproximada encontrada: x = {x_nuevo:.6f}")
                print(f"Convergio en {i} iteraciones.")
                return x_nuevo

            x = x_nuevo

        print("\n No convergio despues del numero maximo de iteraciones.")
        return None



if __name__ == "__main__":
    import math

    print("MÉTODO DE NEWTON-RAPHSON")

    f_expr = input("f(x) = ")
    df_expr = input("f'(x) = ")

    f = lambda x: eval(f_expr, {"x": x, "math": math})
    df = lambda x: eval(df_expr, {"x": x, "math": math})

    x0 = float(input("\nValor inicial x0 = "))
    tol = float(input("Tolerancia (ej. 1e-6) = "))
    max_iter = int(input("Número máximo de iteraciones = "))

    metodo = NewtonRaphson(f, df, x0, tol, max_iter)
    raiz = metodo.resolver()

    if raiz is not None:
        print(f"\nVerificación: f({raiz:.6f}) = {f(raiz):.6e}")
