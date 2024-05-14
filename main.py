from PyQt5 import QtWidgets, QtGui

class LoanCalculator(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora de Empréstimo")
        self.setGeometry(500, 500, 400, 200)
        self.setWindowIcon(QtGui.QIcon('calculadora.png'))
        self.create_widgets()
        self.set_layout()

    def create_widgets(self):
        self.label_PV = QtWidgets.QLabel("Valor do empréstimo (R$):")
        self.entry_PV = QtWidgets.QLineEdit()
        self.entry_PV.setToolTip("Insira o valor do empréstimo em R$")

        self.label_r = QtWidgets.QLabel("Taxa de juros a.m.(%):")
        self.entry_r = QtWidgets.QLineEdit()
        self.entry_r.setToolTip("Insira a taxa de juros mensal em %")

        self.label_n = QtWidgets.QLabel("N° de parcelas (meses):")
        self.entry_n = QtWidgets.QLineEdit()
        self.entry_n.setToolTip("Insira o número de parcelas em meses")

        self.resultado_label = QtWidgets.QLabel("Resultado:")
        self.calcular_button = QtWidgets.QPushButton("Calcular")
        self.calcular_button.clicked.connect(self.calcular)

    def set_layout(self):
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.label_PV)
        layout.addWidget(self.entry_PV)
        layout.addWidget(self.label_r)
        layout.addWidget(self.entry_r)
        layout.addWidget(self.label_n)
        layout.addWidget(self.entry_n)
        layout.addWidget(self.resultado_label)
        layout.addWidget(self.calcular_button)
        self.setLayout(layout)

    def calcular(self):
        try:
            PV = self.entry_PV.text()
            r = self.entry_r.text()
            n = self.entry_n.text()

            if not PV or not r or not n:
                raise ValueError("Todos os campos devem ser preenchidos.")
            
            PV = float(PV)
            r = float(r)
            n = int(n)

            if PV <= 0 or r <= 0 or n <= 0:
                raise ValueError("Os valores devem ser maiores que zero.")

            P = self.calcular_parcela_emprestimo(PV, r, n)
            self.exibir_resultados(PV, r, n, P)
        except ValueError as e:
            QtWidgets.QMessageBox.critical(self, "Erro", str(e))

    def calcular_parcela_emprestimo(self, PV, r, n):
        r_decimal = r / 100
        P = (PV * (1 + r_decimal)**n * r_decimal) / ((1 + r_decimal)**n - 1)
        return P

    def exibir_resultados(self, PV, r, n, P):
        total_pago = P * n
        total_juros = total_pago - PV
        self.resultado_label.setText(f"Parcela: R$ {P:.2f}\nTotal Pago: R$ {total_pago:.2f}\nJuros: R$ {total_juros:.2f}")

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = LoanCalculator()
    window.show()
    app.exec_()
