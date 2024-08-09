sc = 123456
tmx= 3

for i in range (3):
    senha = int(input(f"Digite a sua senha: "))

    if senha == sc:
        print("senha correta")
        exit()
    else:
        tr = tmx - (i + 1)
        if tr > 0:
            print(f"Senha incorreta! voce ainda tem {tr} tentativas")
        else:
            print("conta bloqueada!")
