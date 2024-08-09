nmb = ""
vmb = float("inf")
tdp = 0

for i in range(5):
    nome_medicamento = input(f"Digite o nome do medicamento {i + 1}: ")
    preço = float(input(f"Informe o preço do medicamento {i + 1}: "))

    if preço < vmb:
        nmb = nome_medicamento
        vmb = preço

    tdp += preço

media = tdp / 5

print(f"O medicamento mais barato é {nmb} com o preço de R${vmb:.2f}")
print(f"A média dos preços dos medicamentos é R${media:.2f}")
