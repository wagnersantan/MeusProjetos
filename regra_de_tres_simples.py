import tkinter as tk  # Importa a biblioteca Tkinter para criar a interface gráfica.

def regra_de_tres_simples(a, b, c):
    d = (b * c) / a
    return d

def calcular():  # Define a função que será chamada ao clicar no botão.
    a = float(entry_a.get())  # Obtém o valor de 'a' do campo de entrada.
    b = float(entry_b.get())  # Obtém o valor de 'b' do campo de entrada.
    c = float(entry_c.get())  # Obtém o valor de 'c' do campo de entrada.
    
    d = regra_de_tres_simples(a, b, c)  # Chama a função para calcular 'd'.
    resultado_label.config(text=f"O valor de d é: {d}")  # Atualiza o rótulo com o resultado.

# Criação da janela principal.
root = tk.Tk()
root.title("Regra de Três Simples")  # Define o título da janela.

# Criação dos campos de entrada e rótulos.
tk.Label(root, text="Digite o valor de a:").pack()  # Rótulo para 'a'.
entry_a = tk.Entry(root)  # Campo de entrada para 'a'.
entry_a.pack()  # Adiciona o campo à janela.

tk.Label(root, text="Digite o valor de b:").pack()  # Rótulo para 'b'.
entry_b = tk.Entry(root)  # Campo de entrada para 'b'.
entry_b.pack()  # Adiciona o campo à janela.

tk.Label(root, text="Digite o valor de c:").pack()  # Rótulo para 'c'.
entry_c = tk.Entry(root)  # Campo de entrada para 'c'.
entry_c.pack()  # Adiciona o campo à janela.

# Criação do botão para calcular.
calcular_button = tk.Button(root, text="Calcular", command=calcular)  # Botão que chama a função calcular.
calcular_button.pack()  # Adiciona o botão à janela.

# Rótulo para exibir o resultado.
resultado_label = tk.Label(root, text="")  # Cria um rótulo vazio para o resultado.
resultado_label.pack()  # Adiciona o rótulo à janela.

root.mainloop()  # Inicia o loop principal da interface gráfica.
