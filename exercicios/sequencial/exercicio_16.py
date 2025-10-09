import math

area = float(input("Digite o tamanho da área a ser pintada (em m²): "))
litros_necessarios = area / 3
latas_necessarias = math.ceil(litros_necessarios / 18)
preco_total = latas_necessarias * 80
print("Você precisa de", latas_necessarias,"lata(s) de tinta.")
print("Preço total: R$ ",preco_total)