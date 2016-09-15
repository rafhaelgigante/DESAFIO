import os
import time

loop = False

while loop == False:
    loopi = False
    leitec = open('../estoque/leite.txt', 'w')
    pos = leitec.write(input("Coloque os valores do produto de 'Leite Condensado' (Ex:Marca : xx // Quantidade: xx) \n"))
    cert = str(input("tem certeza de que voce digitou os valores corrertamente ? \n"))
    os.system('cls')
    resp = str(input("Voce deseja por outro valor? \n"))
    
    if resp == "sim":
        time.sleep(2)
        os.system('cls')
        leitec.write('\n')
        pos3 = leitec.write(input("Coloque os valores do produto de 'Leite Condensado' (Ex:Marca : xx // Quantidade: xx) \n"))
        loop = True
    else:
        if resp == "nao":
            loop = True
            time.sleep(2)
            os.system('cls')

loop2 = False

while loop2 == False:
    sabao = open('../estoque/sabao.txt', 'w')
    sabao.write(input("Coloque os valores do produto de 'SABAO EM PÓ' (Ex:Marca : xx // Quantidade: xx) \n"))
    cert = str(input("tem certeza de que voce digitou os valores corrertamente ?"))
    resp = str (input("Voce deseja por outro valor ? \n"))
    if resp == "sim":
        time.sleep(2)
        os.system('cls')
        sabao.write('\n')
        pos3 = sabao.write(input("Coloque os valores do produto de 'SABÃO EM PÓ' (Ex:Marca : xx // Quantidade: xx) \n"))
        loop = True
    else:
        if resp == "nao":
            loop2 = True
            time.sleep(2)
            os.system('cls')





    


