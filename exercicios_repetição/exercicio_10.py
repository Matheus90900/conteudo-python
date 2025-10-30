base = int(input("Digite o número base: "))
expoente = int(input("Digite o expoente: "))

resultado = 1

if expoente > 0:
    for i in range(expoente):
        resultado *= base
elif expoente == 0:
    resultado = 1
else:
    for i in range(-expoente):
        resultado *= base
    resultado = 1 / resultado

print(f"\n{base} elevado a {expoente} = {resultado}")