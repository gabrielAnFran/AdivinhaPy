import random

print("**************************")
print("Bem vindo ao jogo de adivinhação")
print("**************************")

num_secreto = round(random.randrange(1, 101))
print(num_secreto)
total_de_tentativas = 3


for rodada in range (1,total_de_tentativas+1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute = int(input('Entre com um número entre 1 e 100: '))
    acertou = chute == num_secreto
    maior = chute > num_secreto
    menor = chute < num_secreto
    if (chute >1 and chute<=100):
        if (acertou):
            print("Acertou")
            break
        else :
            if(maior):
                print("Seu chute foi maior que o a resposta correta")
            elif(menor):
                print("Seu chute foi menor que o a resposta correta")
    else:
        print('Numero inválido')
        continue
print('Fim')