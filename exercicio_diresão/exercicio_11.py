salario = float(input("Digite o salário do colaborador: R$ "))

if salario <= 1450.00:
    percentual = 20
elif salario <= 2800.00:
    percentual = 15
elif salario <= 3500.00:
    percentual = 10
else:
    percentual = 5

valor_aumento = salario * (percentual / 100)
novo_salario = salario + valor_aumento

print("REAJUSTE SALARIAL")
print("Salário antes do reajuste: R$",salario)
print("Percentual de aumento aplicado:",percentual,"%")
print("Valor do aumento: R$",valor_aumento)
print("Novo salário: R$",novo_salario)