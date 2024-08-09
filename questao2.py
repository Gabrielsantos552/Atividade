termo = int(input("Primeiro termo: "))
quantidade = int(input("Quantidade de termos: "))
razao = int(input("razâo: "))
a = 0
for x in range(termo, quantidade + 1, razao):
  a += x
  print(a)
