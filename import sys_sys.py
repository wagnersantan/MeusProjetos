import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QVBoxLayout

def on_button_click():
    QMessageBox.information(window, "Info", "Você clicou no botão!")

app = QApplication(sys.argv)

# Criar a janela principal
window = QWidget()
window.setWindowTitle("Exemplo PyQt")

# Criar um layout e um botão
layout = QVBoxLayout()
button = QPushButton("Clique aqui!")
button.clicked.connect(on_button_click)
layout.addWidget(button)

window.setLayout(layout)
window.show()

# Iniciar o loop principal
sys.exit(app.exec_())