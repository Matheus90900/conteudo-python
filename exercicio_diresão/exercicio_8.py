preco1 = float(input("Digite o preço do primeiro produto: R$ "))
preco2 = float(input("Digite o preço do segundo produto: R$ "))
preco3 = float(input("Digite o preço do terceiro produto: R$ "))

mais_barato = 0
produto = 0

if preco1 <= preco2:
    mais_barato = preco1
    produto = 1
elif preco2 <= preco1:
    mais_barato = preco2
    produto = 2
else:
    mais_barato = preco3
    produto = 3

print("Você deve comprar o produto",produto,"que custa R$",mais_barato)