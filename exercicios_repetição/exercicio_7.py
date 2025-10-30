num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))

print(f"\nNúmeros inteiros entre {num1} e {num2}:")

if num1 < num2:
    for i in range(num1 + 1, num2):
        print(i)
elif num2 < num1:
    for i in range(num2 + 1, num1):
        print(i)
else:
    print("Os números são iguais, portanto não há intervalo entre eles.")