import os
import sys
import shutil
from datetime import datetime
from PyQt6 import QtGui
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QTableWidgetItem, QPushButton,
    QMessageBox, QInputDialog
)
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
from filemanager import Ui_MainWindow

ICON_MAPPING = {
    'jpg': 'jpg.png',
    'jpeg': 'jpg.png',
    'png': 'png.png',
    'txt': 'txt.png',
    'pdf': 'pdf.png',
    'py': 'python.png',
    'db': 'db.png',
    'ui': 'ui.png'
}

PROTECTED_FILES = ['main.py', 'filemanager.py']

class FileManager(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.current_path = os.getcwd()
        self.history = []

        self.ui.naujas_failas.clicked.connect(self.create_file)
        self.ui.Atgal.clicked.connect(self.go_back)
        self.ui.lentele.cellDoubleClicked.connect(self.handle_double_click)

        self.load_directory(self.current_path)

    def load_directory(self, path):
        self.ui.lentele.setRowCount(0)
        self.current_path = path

        try:
            entries = os.listdir(path)
        except Exception as e:
            QMessageBox.critical(self, "Klaida", f"Nepavyko nuskaityti: {e}")
            return

        self.ui.lentele.setColumnCount(5)
        self.ui.lentele.setHorizontalHeaderLabels(["Pavadinimas", "Tipas", "Paskutine modifikacija", "Naršyti", "Veiksmai"])

        for i, entry in enumerate(entries):
            full_path = os.path.join(path, entry)
            is_dir = os.path.isdir(full_path)

            row_position = self.ui.lentele.rowCount()
            self.ui.lentele.insertRow(row_position)

            icon = self.getFileIcon(full_path)
            item = QTableWidgetItem(icon, entry)
            item.setData(Qt.ItemDataRole.UserRole, full_path)
            self.ui.lentele.setItem(row_position, 0, item)
            self.ui.lentele.setItem(row_position, 1, QTableWidgetItem("Aplankas" if is_dir else "Failas"))
            mod_time = datetime.fromtimestamp(os.path.getmtime(full_path)).strftime('%Y-%m-%d %H:%M')
            self.ui.lentele.setItem(row_position, 2, QTableWidgetItem(mod_time))

            browse_btn = QPushButton("Atidaryti")
            browse_btn.setEnabled(is_dir)
            if is_dir:
                browse_btn.clicked.connect(lambda _, p=full_path: self.open_directory(p))
            self.ui.lentele.setCellWidget(row_position, 3, browse_btn)

            action_btn = QPushButton("...")
            action_btn.clicked.connect(lambda _, e=entry, fp=full_path: self.show_actions(e, fp))
            self.ui.lentele.setCellWidget(row_position, 4, action_btn)

    def handle_double_click(self, row, column):
        item = self.ui.lentele.item(row, 0)
        if item:
            full_path = item.data(Qt.ItemDataRole.UserRole)
            if os.path.isdir(full_path):
                self.open_directory(full_path)
            else:
                try:
                    os.startfile(full_path)
                except Exception as e:
                    QMessageBox.warning(self, "Nepavyko atidaryti", str(e))

    def getFileIcon(self, filename):
        icons_dir = os.path.join(os.path.dirname(__file__), "icons")
        if os.path.isdir(filename):
            icon_path = os.path.join(icons_dir, "folder.png")
        else:
            ext = filename.split(".")[-1].lower()
            icon_file = ICON_MAPPING.get(ext, "file.png")
            icon_path = os.path.join(icons_dir, icon_file)

        if os.path.exists(icon_path):
            return QtGui.QIcon(QtGui.QPixmap(icon_path))
        else:
            return QtGui.QIcon()

    def show_actions(self, name, full_path):
        actions = QMessageBox()
        actions.setWindowTitle("Pasirinkite veiksmą")
        actions.setText(f"Pasirinkite veiksmą failui: {name}")
        rename = actions.addButton("Pervadinti", QMessageBox.ButtonRole.AcceptRole)
        delete = actions.addButton("Ištrinti", QMessageBox.ButtonRole.DestructiveRole)
        cancel = actions.addButton("Atšaukti", QMessageBox.ButtonRole.RejectRole)
        actions.exec()

        if actions.clickedButton() == rename:
            self.rename_file(full_path, name)
        elif actions.clickedButton() == delete:
            self.delete_file(full_path, name)

    def rename_file(self, full_path, old_name):
        new_name, ok = QInputDialog.getText(self, "Pervadinti", "Naujas pavadinimas:")
        if ok and new_name:
            new_path = os.path.join(self.current_path, new_name)
            try:
                os.rename(full_path, new_path)
                self.load_directory(self.current_path)
            except Exception as e:
                QMessageBox.critical(self, "Klaida", f"Nepavyko pervadinti: {e}")

    def delete_file(self, full_path, name):
        if name in PROTECTED_FILES:
            QMessageBox.warning(self, "Draudžiama", "Šio failo trinti negalima!")
            return
        try:
            if os.path.isdir(full_path):
                shutil.rmtree(full_path)
            else:
                os.remove(full_path)
            self.load_directory(self.current_path)
        except Exception as e:
            QMessageBox.critical(self, "Klaida", f"Nepavyko ištrinti: {e}")

    def create_file(self):
        name, ok = QInputDialog.getText(self, "Naujas failas", "Įveskite pavadinimą:")
        if ok and name:
            path = os.path.join(self.current_path, name)
            try:
                with open(path, 'w') as f:
                    f.write("")
                self.load_directory(self.current_path)
            except Exception as e:
                QMessageBox.critical(self, "Klaida", f"Nepavyko sukurti failo: {e}")

    def open_directory(self, path):
        self.history.append(self.current_path)
        self.load_directory(path)

    def go_back(self):
        if self.history:
            prev = self.history.pop()
            self.load_directory(prev)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FileManager()
    window.show()
    sys.exit(app.exec())