import sys
from PyQt6.QtWidgets import QApplication, QDialog
from PyQt6.uic import loadUi

# 10 populiarių Google klausimų
questions = [
    "What to watch",
    "What is my IP",
    "Where's my refund",
    "Where is my train",
    "How many days until Christmas",
    "What time is it",
    "Who won the election 2024",
    "How many weeks in a year",
    "How many ounces in a cup",
    "Where am I"
]

class MainWindow(QDialog):  # BUVO QMainWindow
    def __init__(self):
        super().__init__()
        loadUi("c:/Users/manta/Desktop/Python/dropdown/dropdown.ui", self)
        self.ivestis.textChanged.connect(self.filtruoti_rezultatus)
        self.dropdownas.clear()

        # Pradinis sąrašas (tuščias kol kas)
        self.dropdownas.clear()

    def filtruoti_rezultatus(self, tekstas):
        tekstas = tekstas.strip().lower()
        self.dropdownas.clear()

        if tekstas == "":
            return

        # Filtruojame klausimus pagal tikslų tekstą (bet case-insensitive)
        atitikmenys = [q for q in questions if tekstas in q.lower()]
        self.dropdownas.addItems(atitikmenys)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    langas = MainWindow()
    langas.show()
    sys.exit(app.exec())
