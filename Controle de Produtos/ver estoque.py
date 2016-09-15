import time
import os

resposta = "sim"
loop = False

if resposta == "sim":
    while loop == False:
        print('produtos disponíveis: Leite Condensado(id=2), Sabão em Pó(id=24)\n')
        idn = int(input("Coloque o ID do produto: \n"))

        if idn == 2:
            leitec = open('estoque/leite.txt', 'r')
            ide = leitec.read()
            print(ide)
            if resposta == "s":
                res1 = str(input("Deseja voltar para o id dos produtos? ('S' para Sime 'N' para não)\n"))
                if res1 == "n":
                    loop = True
                else:
                    if res1 == "s":
                        loop = False
                        os.system('cls')
                    else:
                        print("Coloque um valor válido")
            leitec.close()
                        
        if idn == 24:
            sabao = open('estoque/sabao.txt', 'r')
            ide = sabao.read()
            print(ide)
            if resposta == "sim":
                res = str(input("Deseja voltar para o id dos produtos? ('S' para Sime 'N' para não)\n"))
            if res == "n":
                loop = True
            else:
                if res == "s":
                    loop = False
                    os.system('cls')
                else:
                    print("Coloque um valor válido")
            sabao.close()
            
                    
