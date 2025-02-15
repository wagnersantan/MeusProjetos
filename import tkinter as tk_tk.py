import tkinter as tk
from tkinter import messagebox

def on_button_click():
    messagebox.showinfo("Info", "Você clicou no botão!")

# Criar a janela principal
root = tk.Tk()
root.title("Exemplo Tkinter")

# Criar um botão
button = tk.Button(root, text="Clique aqui!", command=on_button_click)
button.pack(pady=20)

# Iniciar o loop principal
root.mainloop()