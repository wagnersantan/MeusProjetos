import random

estudantes = []

num_estudantes = int(input("Quantos estudantes você tem? "))

for i in range(num_estudantes):
    nome = input(f'Digite o nome do estudante {i + 1}: ')
    estudantes.append(nome)

estudante_sorteado = random.choice(estudantes)
print(f"O estudante sorteado para apagar o quadro é {estudante_sorteado}.")