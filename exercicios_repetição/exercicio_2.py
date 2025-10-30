def validar_nome():
    while True:
        nome = input("Digite o seu nome (mais de 3 caracteres): ")
        if len(nome) > 3:
            return nome
        else:
            print("Nome inválido. O nome deve ter mais de 3 caracteres.")


def validar_idade():
    while True:
        try:
            idade = int(input("Digite a sua idade (entre 0 e 150): "))
            if 0 <= idade <= 150:
                return idade
            else:
                print("Idade inválida. A idade deve estar entre 0 e 150.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.")

def validar_salario():
    while True:
        try:
            salario = float(input("Digite o seu salário (maior que zero): "))
            if salario > 0:
                return salario
            else:
                print("Salário inválido. O salário deve ser maior que zero.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um valor numérico válido.")


def validar_estado_civil():
    while True:
        stado_civil = input("Digite o seu estado civil ('s' para solteiro, 'c' para casado, 'v' para viúvo, 'd' para divorciado): ").lower()
        if estado_civil in ['s', 'c', 'v', 'd']:
            return estado_civil
        else:
            print("Estado civil inválido. Por favor, insira uma das opções: 's', 'c', 'v', ou 'd'.")


nome = validar_nome()
idade = validar_idade()
salario = validar_salario()
estado_civil = validar_estado_civil()

print("\nInformações validadas:")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Salário: R${salario:.2f}")
print(f"Estado Civil: {estado_civil}")