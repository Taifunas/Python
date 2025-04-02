import sys
from PyQt6.QtWidgets import QApplication, QDialog
from skaiciuotuvas import Ui_Dialog  # sugeneruota iš .ui failo naudojant PyQt6
from PyQt6.QtCore import Qt
import math  # viršuje faile


class Skaiciuotuvas(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # Rezultato laukelis – tik skaitymui
        self.ui.isvestis.setReadOnly(True)

        # Skaičių mygtukai
        self.ui.vienas.clicked.connect(lambda: self.append_to_expression("1"))
        self.ui.du.clicked.connect(lambda: self.append_to_expression("2"))
        self.ui.trys.clicked.connect(lambda: self.append_to_expression("3"))
        self.ui.keturi.clicked.connect(lambda: self.append_to_expression("4"))
        self.ui.penki.clicked.connect(lambda: self.append_to_expression("5"))
        self.ui.sesi.clicked.connect(lambda: self.append_to_expression("6"))
        self.ui.septyni.clicked.connect(lambda: self.append_to_expression("7"))
        self.ui.astuoni.clicked.connect(lambda: self.append_to_expression("8"))
        self.ui.devyni.clicked.connect(lambda: self.append_to_expression("9"))
        self.ui.nulis.clicked.connect(lambda: self.append_to_expression("0"))

        # Operatoriai
        self.ui.plius.clicked.connect(lambda: self.append_operator("+"))
        self.ui.minus.clicked.connect(lambda: self.append_operator("-"))
        self.ui.daugyba.clicked.connect(lambda: self.append_operator("*"))
        self.ui.dalyba.clicked.connect(lambda: self.append_operator("/"))
        self.ui.laipsnis.clicked.connect(lambda: self.append_operator("^"))
        self.ui.saknis.clicked.connect(lambda: self.append_function("√"))

        # skliausteliai
        self.ui.kairinis_skliaustas.clicked.connect(lambda: self.append_to_expression("("))
        self.ui.desininis_skliaustas.clicked.connect(lambda: self.append_to_expression(")"))
        
        # Lygus (=)
        self.ui.lygu.clicked.connect(self.calculate_result)

        # C ir CE
        self.ui.c.clicked.connect(self.clear_all)
        self.ui.ce.clicked.connect(self.clear_last)

        self.apply_dark_theme()

    def apply_dark_theme(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #2b2b2b;
                color: #ffffff;
                font-size: 16px;
            }
            QLineEdit {
                background-color: #1e1e1e;
                color: #00ffcc;
                border: 1px solid #444;
                padding: 5px;
            }
            QPushButton {
                background-color: #3c3f41;
                color: #ffffff;
                border: 1px solid #5c5c5c;
                border-radius: 5px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #505357;
            }
            QPushButton:pressed {
                background-color: #2a82da;
            }
        """)

    def append_to_expression(self, value):
        current = self.ui.ivestis.text()
        self.ui.ivestis.setText(current + value)

    def append_operator(self, op):
        current = self.ui.ivestis.text()
        if current and current[-1] in "+-*/":
            current = current[:-1]
        self.ui.ivestis.setText(current + op)

    def calculate_result(self):
        expression = self.ui.ivestis.text()
        expression = expression.replace("^", "**")
        expression = expression.replace("√", "math.sqrt")

        # Automatiškai įterpiam * tarp skaičiaus ir math.sqrt
        expression = expression.replace("math.sqrt", "*math.sqrt")
        expression = expression.replace("*math.sqrt", "math.sqrt", 1)  # bet pirmo nekeičiame, jei tiesiog prasideda nuo √
        try:
            result = eval(expression)
            self.ui.isvestis.setText(str(result))
        except Exception:
            self.ui.isvestis.setText("Klaida")

    def clear_all(self):
        self.ui.ivestis.clear()
        self.ui.isvestis.clear()

    def clear_last(self):
        current = self.ui.ivestis.text()
        self.ui.ivestis.setText(current[:-1])

    def append_function(self, func):
        current = self.ui.ivestis.text()
        if func == "√":
            self.ui.ivestis.setText(current + "√(")
    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    langas = Skaiciuotuvas()
    langas.setWindowTitle("Skaičiuotuvas")
    langas.show()
    sys.exit(app.exec())
