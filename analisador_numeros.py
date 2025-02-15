import tkinter as tk
from tkinter import messagebox

def analisar_numero():
    try:
        # Obter o número do campo de entrada
        num = int(entry.get())
        
        # Calcular unidade, dezena, centena e milhar
        u = num // 1 % 10
        d = num // 10 % 10
        c = num // 100 % 10
        m = num // 1000 % 10
        
        # Montar a mensagem
        resultado = (
            f'Analisando o número {num}\n'
            f'Unidade: {u}\n'
            f'Dezena: {d}\n'
            f'Centena: {c}\n'
            f'Milhar: {m}'
        )
        
        # Exibir resultado em uma caixa de mensagem
        messagebox.showinfo('Resultado', resultado)
    except ValueError:
        messagebox.showerror('Erro', 'Por favor, insira um número válido.')

# Criar a janela principal
root = tk.Tk()
root.title('Analisador de Números')

# Criar um label
label = tk.Label(root, text='Informe um número:')
label.pack()

# Criar um campo de entrada
entry = tk.Entry(root)
entry.pack()

# Criar um botão para analisar o número
button = tk.Button(root, text='Analisar', command=analisar_numero)
button.pack()

# Iniciar o loop da interface gráfica
root.mainloop()