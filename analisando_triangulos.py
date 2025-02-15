r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

# Verifica se os segmentos podem formar um triângulo
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar um triângulo')
    
    # Verifica o tipo de triângulo
    if r1 == r2 == r3:
        print('Triângulo equilátero')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Triângulo isósceles')
    else:
        print('Triângulo escaleno')
else:
    print('Os segmentos acima não podem formar um triângulo')