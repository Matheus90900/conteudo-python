import math

a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))

if a == 0:
    print("Não é uma equação de segundo grau")
    exit(1)

delta = b ** 2 - 4 * a * c

if delta < 0:
    print("Delta:",delta)
    print("Não é possivel calcular raiz de numeros negativos")
    exit(1)

if delta == 0:
    x = (b * -1) / (2 * a)
    print(f"O valor de x é {x}")
else:
    raiz = math.sqrt(delta)
    xa = ((b * -1) + raiz) / (2 * a)
    xb = ((b * -1) + raiz) / (2 * a)
    print(f"O valor de x' é {xa}")
    print(f"O valor de x'' é {xb}")
