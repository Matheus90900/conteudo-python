nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

print("Média do aluno:",media)

if media == 10:
    print("Aluno Destaque")
elif media >= 7:
    print("Aprovado")
else:
    print("Reprovado")