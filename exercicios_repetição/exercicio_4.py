while True:
    print("\n=== CÁLCULO DE CRESCIMENTO POPULACIONAL ===")

    try:
        populacao_A = float(input("Informe a população do país A: "))
        populacao_B = float(input("Informe a população do país B: "))
        taxa_A = float(input("Informe a taxa de crescimento anual de A (em %): "))
        taxa_B = float(input("Informe a taxa de crescimento anual de B (em %): "))
    except ValueError:
        print("Erro: digite apenas números válidos.")
        continue

    if populacao_A <= 0 or populacao_B <= 0:
        print("As populações devem ser maiores que zero.")
        continue
    if taxa_A <= 0 or taxa_B <= 0:
        print("As taxas de crescimento devem ser positivas.")
        continue

    taxa_A /= 100
    taxa_B /= 100

    anos = 0

    if populacao_A >= populacao_B:
        print("\nO país A já possui população maior ou igual à do país B.")
    else:
        while populacao_A < populacao_B:
            populacao_A += populacao_A * taxa_A
            populacao_B += populacao_B * taxa_B
            anos += 1

        print(f"\n➡️ Em {anos} anos a população do país A ultrapassará ou igualará a do país B.")
        print(f"População final de A: {int(populacao_A)} habitantes")
        print(f"População final de B: {int(populacao_B)} habitantes")

    repetir = input("\nDeseja realizar outro cálculo? (S/N): ").strip().upper()
    if repetir != "S":
        print("\nPrograma encerrado. 👋")
        break