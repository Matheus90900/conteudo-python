peso = float(input("Digite o peso do peixe: "))
limite = 50.0
multa_por_quilo = 4.00
excesso = peso - limite
multa = excesso * multa_por_quilo

print(f"Peso informado: {peso:.2f} kg")
print(f"Excesso de peso: {excesso:.2f} kg")
print(f"Multa a pagar: R$ {multa:.2f}")