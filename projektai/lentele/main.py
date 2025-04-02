import sqlite3
from datetime import datetime
from design import Ui_MainWindow
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt6.QtCore import Qt

class Langas(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.conn = sqlite3.connect("duomenys.db")
        self.c = self.conn.cursor()
        self.sukurti_db()

        print("Langas atidarytas")

        self.prideti.clicked.connect(self.prideti_eilute)

        # Susiejam įvesties laukus su filtravimu
        self.vardas.textChanged.connect(self.filtruoti_lentele)
        self.pavarde.textChanged.connect(self.filtruoti_lentele)
        self.adresas.textChanged.connect(self.filtruoti_lentele)
        self.telefonas.textChanged.connect(self.filtruoti_lentele)
        self.el_pastas.textChanged.connect(self.filtruoti_lentele)

        self.paisyti_eilutes()

    def sukurti_db(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS kontaktai (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            vardas TEXT,
                            pavarde TEXT,
                            adresas TEXT,
                            telefonas TEXT,
                            el_pastas TEXT)''')
        # Pridedam stulpelius jei jų trūksta
        self.c.execute("PRAGMA table_info(kontaktai)")
        stulpeliai = [row[1] for row in self.c.fetchall()]

        if 'created_on' not in stulpeliai:
            self.c.execute("ALTER TABLE kontaktai ADD COLUMN created_on TEXT")
        if 'updated_on' not in stulpeliai:
            self.c.execute("ALTER TABLE kontaktai ADD COLUMN updated_on TEXT")

        self.conn.commit()

    def prideti_eilute(self):
        vardas = self.vardas.text().strip()
        pavarde = self.pavarde.text().strip()
        adresas = self.adresas.text().strip()
        telefonas = self.telefonas.text().strip()
        el_pastas = self.el_pastas.text().strip()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if not (vardas and pavarde and adresas and telefonas and el_pastas):
            print("Klaida: visi laukai turi būti užpildyti!")
            return

        self.c.execute('''
            INSERT INTO kontaktai (vardas, pavarde, adresas, telefonas, el_pastas, created_on, updated_on)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (vardas, pavarde, adresas, telefonas, el_pastas, timestamp, timestamp))
        self.conn.commit()

        self.vardas.clear()
        self.pavarde.clear()
        self.adresas.clear()
        self.telefonas.clear()
        self.el_pastas.clear()

        self.paisyti_eilutes()

    def paisyti_eilutes(self):
        self.c.execute("SELECT vardas, pavarde, adresas, telefonas, el_pastas, created_on, updated_on FROM kontaktai")
        duomenys = self.c.fetchall()
        self.uzpildyti_lentele(duomenys)

    def filtruoti_lentele(self):
        vardas = self.vardas.text().strip()
        pavarde = self.pavarde.text().strip()
        adresas = self.adresas.text().strip()
        telefonas = self.telefonas.text().strip()
        el_pastas = self.el_pastas.text().strip()

        sql = '''SELECT vardas, pavarde, adresas, telefonas, el_pastas, created_on, updated_on FROM kontaktai WHERE 1=1'''
        params = []

        if vardas:
            sql += " AND vardas LIKE ?"
            params.append(f"%{vardas}%")
        if pavarde:
            sql += " AND pavarde LIKE ?"
            params.append(f"%{pavarde}%")
        if adresas:
            sql += " AND adresas LIKE ?"
            params.append(f"%{adresas}%")
        if telefonas:
            sql += " AND telefonas LIKE ?"
            params.append(f"%{telefonas}%")
        if el_pastas:
            sql += " AND el_pastas LIKE ?"
            params.append(f"%{el_pastas}%")

        self.c.execute(sql, params)
        duomenys = self.c.fetchall()
        self.uzpildyti_lentele(duomenys)

    def uzpildyti_lentele(self, duomenys):
        self.lentele.setColumnCount(7)
        self.lentele.setHorizontalHeaderLabels(["Vardas", "Pavardė", "Adresas", "Telefonas", "El. paštas", "Sukurta", "Atnaujinta"])
        self.lentele.setRowCount(len(duomenys))

        for eilutes_nr, stulpeliai in enumerate(duomenys):
            for stulpelio_nr, reiksme in enumerate(stulpeliai):
                self.lentele.setItem(eilutes_nr, stulpelio_nr, QTableWidgetItem(reiksme))

# Aplikacijos paleidimas
app = QApplication([])
langas = Langas()
langas.show()
app.exec()