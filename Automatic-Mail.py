from __future__ import annotations
import threading
import time
import pandas as pd
import pyautogui
import pyperclip
import keyboard

from PySide6 import QtCore, QtWidgets

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        QtWidgets.QMainWindow.__init__(self)

        self.dialog = QtWidgets.QFileDialog(self)
        self.dialog.setWindowTitle('Open csv...')

        self.setWindowTitle("Login")

        layout = QtWidgets.QVBoxLayout()

        self.email_label = QtWidgets.QLabel("Email:")
        self.email_input = QtWidgets.QLineEdit()
        layout.addWidget(self.email_label)
        layout.addWidget(self.email_input)

        self.password_label = QtWidgets.QLabel("Senha:")
        self.password_input = QtWidgets.QLineEdit()
        self.password_input.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)

        self.texto1_label = QtWidgets.QLabel("Texto Exibido:")
        self.texto1_input = QtWidgets.QLineEdit()
        layout.addWidget(self.texto1_label)
        layout.addWidget(self.texto1_input)

        self.texto2_label = QtWidgets.QLabel("Assunto:")
        self.texto2_input = QtWidgets.QLineEdit()
        layout.addWidget(self.texto2_label)
        layout.addWidget(self.texto2_input)

        self.login_button = QtWidgets.QPushButton("Login")
        self.login_button.clicked.connect(self.login)
        layout.addWidget(self.login_button)

        central_widget = QtWidgets.QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def login(self):
        global email_login, senha_login, texto1, texto2
        email_login = self.email_input.text()
        senha_login = self.password_input.text()
        texto1 = self.texto1_input.text()
        texto2 = self.texto2_input.text()
        self.hide()
        self.dialog.open(self, QtCore.SLOT('on_finished()'))

    @QtCore.Slot()
    def on_finished(self) -> None:
        global caminho
        for path in self.dialog.selectedFiles():
            caminho = path
            fazerOqTuQuiser(caminho)

def fazerOqTuQuiser(caminho):
    print(caminho)
    thread = threading.Thread(target=executar_pyautogui)
    thread.start()

def executar_pyautogui():
    global texto1, texto2
    # print(str(f'{texto1} {texto2}'))
    pyautogui.PAUSE = 1
    # abrir navegador e entrar no link
    pyautogui.press("win")
    pyautogui.write("Chrome")
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.hotkey("ctrl","shift","n")
    pyautogui.click(x=1203, y=29)
    # for _ in range(14):
    #     pyautogui.hotkey("tab")

    pyautogui.write("https://mail.google.com/")
    pyautogui.press("enter")
    time.sleep(3)
    # escrever o email
    # Fazer Login
    pyautogui.write(email_login)
    pyautogui.press("enter")
    time.sleep(3)
    pyautogui.write(senha_login)
    pyautogui.press("enter")
    time.sleep(10)
    # 12 tabs
    for _ in range(12):
        pyautogui.hotkey("tab")
    pyautogui.press("enter")
    # carregar os dados do csv
    tabela = pd.read_csv(caminho)
    time.sleep(4)
    # Cadastrar um produto
    linha = 0
    # Cadastrar um produto
    for linha in tabela.index:
        # Pegar os valores da linha atual
        nome = tabela.loc[linha, "nome"]
        email = tabela.loc[linha, "email"]
        

        # Preencher os campos
        pyautogui.write(str(email))
        pyautogui.press("enter")
        pyautogui.press("tab")
        pyperclip.copy(str(texto2))
        pyautogui.hotkey("ctrl", "v")
        pyautogui.press("tab")
        pyperclip.copy(str(texto1))
        pyautogui.hotkey("ctrl", "v")
        pyautogui.press("tab")
        pyautogui.press("enter")
        for _ in range(16):
            pyautogui.hotkey("tab")
        time.sleep(5)
        pyautogui.press("enter")
    if  pyautogui.confirm(text='Acabou os nomes?', title='Término do uso', buttons=['Sim' , 'Não']):
        return

# Função para inserir texto com acentos
def escrever_com_acentos(texto):
    keyboard.write(texto)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    window = MyWindow()
    window.show()

    app.exec()
