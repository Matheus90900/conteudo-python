litros = float(input("Digite a quantidade de litros vendidos: "))
tipo = input("Digite o tipo de combustível (A - Álcool, G - Gasolina): ")

preco_alcool = 4.17
preco_gasolina = 6.29

desconto = 0
preco_litro = 0

if tipo == 'A':
    preco_litro = preco_alcool
    if litros <= 20:
        desconto = 0.03
    else:
        desconto = 0.05
elif tipo == 'G':
    preco_litro = preco_gasolina
    if litros <= 20:
        desconto = 0.04
    else:
        desconto = 0.06
else:
    print("Tipo de combustível inválido!")
    exit()

valor_bruto = litros * preco_litro
valor_final = valor_bruto * (1 - desconto)

print("Valor a ser pago: R$ ",valor_final)