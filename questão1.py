a = int(input("informe o primeiro número inteiro(a)"))
b = int(input("informe o segundo número inteiro(a)"))

if a < b:
  soma = sum(range(a,b + 1))
  print(f"a soma dos número inteiros no intervalo [{a}, {b}] é:{soma}")
else:
  print("Erro:  O primeiro número deve ser menor que o segundo número")
