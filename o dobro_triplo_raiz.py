import math
n = int(input("Digite um número: "))
d = n * 2
t = n * 3
r = math.sqrt(n)  # Usando a função sqrt da biblioteca math

print("O dobro de {} vale {}.".format(n, d))
print("O triplo de {} vale {}. A raiz quadrada de {} é igual a {:.2f}.".format(n, t, n, r))
