
import random


print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")
numero_secreto = random.randrange (1,101) 
total_de_tentativas = 3
pontos=1000

print("Qual nível de dificuladade?")
print ("(1) fácil (2) Médio (3) Dificil")
nivel=int(input("Define o nivel:"))

if(nivel==1):
    total_de_tentativas=20
elif (nivel==2):
    total_de_tentativas=10
else:
    total_de_tentativas=5


for rodada in range (1,total_de_tentativas +1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))

    chute_str = input("Digite o seu número: ")
    print("Você digitou " , chute_str)
    chute = int(chute_str)
    if (chute < 1 or chute > 100):
        print("Você deve digitar um número de 0 e 100!")
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("Parabéns! Você acertou  efez {} pontos".format(pontos))
        break
    else:
        if(maior):
            print("O seu chute foi maior do que o número secreto!")
        elif(menor):
            print("O seu chute foi menor do que o número secreto!")
        pontos_perdidos= abs(numero_secreto-chute)
        pontos = pontos-pontos_perdidos

print("Fim do jogo")