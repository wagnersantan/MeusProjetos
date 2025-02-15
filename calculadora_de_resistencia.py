# Função para calcular resistência e potência
def calcular_resistencia_potencia():
    # Passo 1: Recebendo os dados do usuário
    V_fonte = float(input("Digite a tensão da fonte (em volts): "))
    V_LED = float(input("Digite a tensão do LED (em volts): "))
    I_LED = float(input("Digite a corrente do LED (em miliamperes): ")) * 1e-3  # Convertendo para amperes

    # Passo 2: Calculando a tensão que precisa ser dissipada pela resistência
    V_res = V_fonte - V_LED  # Tensão que a resistência precisa dissipar

    # Passo 3: Usando a Lei de Ohm para encontrar a resistência
    R = V_res / I_LED  # Cálculo da resistência usando a Lei de Ohm

    # Passo 4: Exibindo o resultado
    print(f"A resistência necessária é de {R:.2f} ohms.")

    # Passo 5: Calculando a potência dissipada pela resistência
    P = V_res * I_LED  # Potência dissipada na resistência

    # Passo 6: Exibindo a potência
    print(f"A potência dissipada pela resistência é de {P:.2f} watts.")

# Chamando a função para executar o programa
calcular_resistencia_potencia()