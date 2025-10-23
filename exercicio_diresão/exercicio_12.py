valor_hora = float(input("Digite o valor da sua hora de trabalho (R$): "))
horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas no mês: "))

salario_bruto = valor_hora * horas_trabalhadas

if salario_bruto <= 900:
    perc_ir = 0
elif salario_bruto <= 1500:
    perc_ir = 5
elif salario_bruto <= 2500:
    perc_ir = 10
else:
    perc_ir = 20

perc_inss = 10
perc_fgts = 11

valor_ir = salario_bruto * (perc_ir / 100)
valor_inss = salario_bruto * (perc_inss / 100)
valor_fgts = salario_bruto * (perc_fgts / 100)

total_descontos = valor_ir + valor_inss
salario_liquido = salario_bruto - total_descontos


print("FOLHA DE PAGAMENTO")
print("Salário Bruto: (",valor_hora * horas_trabalhadas,"): R$ ",salario_bruto)
print("(-) IR ({perc_ir}%) {' ' * (22 - len(str(perc_ir)))}: R$ {valor_ir:8.2f}")
print(f"(-) INSS ({perc_inss}%) {' ' * 18}: R$ {valor_inss:8.2f}")
print(f"FGTS ({perc_fgts}%) {' ' * 21}: R$ {valor_fgts:8.2f}")
print(f"Total de descontos{' ' * 12}: R$ {total_descontos:8.2f}")
print(f"Salário Líquido{' ' * 15}: R$ {salario_liquido:8.2f}")