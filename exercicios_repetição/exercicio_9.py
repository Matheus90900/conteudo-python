num = int(input("Digite um número entre 1 e 10 para ver sua tabuada: "))

if 1 <= num <= 10:
    print(f"\nTabuada de {num}:")
    for i in range(1, 11):
        print(f"{num} X {i} = {num * i}")
else:
    print("Por favor, digite um número entre 1 e 10.")