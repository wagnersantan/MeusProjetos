num= int(input ("Digite um número inteiro:  "))
print("Escolha uma das bases para conversão")
print("[1] converter para Binário")
print("[2] converter para Octal")
print("[3] converter para hexatecimal")
opção = int(input("Sua opção: ") )
if opção == 1:
       print("{} convertido para Binário é igual a {}".format(num, bin(num)[2:]))
elif opção == 2:
    print("{} convertido para Octal é igual a {}" .format(num,oct(num))[2:])

elif opção == 3:
    print (" {} convertido para Hexadecimal é igual a {}".format(num,hex(num)[2:]))
else:
    print(" Opção inválida tente novamente")