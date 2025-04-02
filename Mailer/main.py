import sys
from PyQt6 import QtWidgets, QtCore
from service.google_mail import GoogleMail


class GmailApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.gmail = GoogleMail()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Gmail API App")
        self.resize(800, 600)

        layout = QtWidgets.QVBoxLayout(self)

        # Input fields
        self.recipient_input = QtWidgets.QLineEdit(self)
        self.recipient_input.setPlaceholderText("Gavėjas (Recipient)")
        layout.addWidget(self.recipient_input)

        self.subject_input = QtWidgets.QLineEdit(self)
        self.subject_input.setPlaceholderText("Tema (Subject)")
        layout.addWidget(self.subject_input)

        self.message_input = QtWidgets.QTextEdit(self)
        self.message_input.setPlaceholderText("Žinutė (Message)")
        layout.addWidget(self.message_input)

        # Buttons
        self.send_button = QtWidgets.QPushButton("Siųsti laišką", self)
        self.send_button.clicked.connect(self.send_email)
        layout.addWidget(self.send_button)

        self.mark_read_button = QtWidgets.QPushButton("Pažymėti kaip skaitytus", self)
        self.mark_read_button.clicked.connect(self.mark_emails_as_read)
        layout.addWidget(self.mark_read_button)

        self.refresh_button = QtWidgets.QPushButton("Atnaujinti", self)
        self.refresh_button.clicked.connect(self.load_emails)
        layout.addWidget(self.refresh_button)

        # Search
        self.search_input = QtWidgets.QLineEdit(self)
        self.search_input.setPlaceholderText("Ieškoti laiškų...")
        self.search_input.textChanged.connect(self.filter_emails)
        layout.addWidget(self.search_input)

        # Email table
        self.email_table = QtWidgets.QTableWidget(self)
        self.email_table.setColumnCount(5)
        self.email_table.setHorizontalHeaderLabels(["Siuntėjas", "Tema", "Žinutė", "Statusas", "Veiksmai"])
        self.email_table.horizontalHeader().setStretchLastSection(True)
        layout.addWidget(self.email_table)

        # Load emails
        self.load_emails()

    def send_email(self):
        recipient = self.recipient_input.text().strip()
        subject = self.subject_input.text().strip()
        message = self.message_input.toPlainText().strip()

        if not recipient or not subject or not message:
            QtWidgets.QMessageBox.warning(self, "Klaida", "Visi laukai turi būti užpildyti!")
            return

        try:
            self.gmail.send_message(recipient, subject, message)
            QtWidgets.QMessageBox.information(self, "Sėkmė", "Laiškas išsiųstas sėkmingai!")
            self.recipient_input.clear()
            self.subject_input.clear()
            self.message_input.clear()
            self.load_emails()  # Automatiškai atnaujina lentelę
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Klaida", f"Laiško siuntimas nepavyko: {e}")

    def load_emails(self):
        self.email_table.setRowCount(0)
        try:
            messages = self.gmail.search_messages("")  # All messages
            for message in messages:
                data = self.gmail.read_message(message)
                row_position = self.email_table.rowCount()
                self.email_table.insertRow(row_position)

                # Extract fields
                sender = ""
                subject = ""
                snippet = data["snippet"]
                labels = data.get("labelIds", [])
                is_unread = "UNREAD" in labels

                for header in data["payload"]["headers"]:
                    if header["name"].lower() == "from":
                        sender = header["value"]

                subject = next((h["value"] for h in data["payload"]["headers"] if h["name"].lower() == "subject"), "(Be temos)")

                # Fill table
                self.email_table.setItem(row_position, 0, QtWidgets.QTableWidgetItem(sender))
                self.email_table.setItem(row_position, 1, QtWidgets.QTableWidgetItem(subject))
                self.email_table.setItem(row_position, 2, QtWidgets.QTableWidgetItem(snippet))

                status_text = "Neskaitytas" if is_unread else "Skaitytas"
                self.email_table.setItem(row_position, 3, QtWidgets.QTableWidgetItem(status_text))

                # Delete button
                delete_button = QtWidgets.QPushButton("Ištrinti")
                delete_button.clicked.connect(lambda checked, msg=message: self.delete_email(msg))
                self.email_table.setCellWidget(row_position, 4, delete_button)
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Klaida", f"Laiškų įkėlimas nepavyko: {e}")

    def filter_emails(self):
        filter_text = self.search_input.text().lower()
        for row in range(self.email_table.rowCount()):
            match = False
            for column in range(self.email_table.columnCount() - 1):  # skip "Veiksmai"
                item = self.email_table.item(row, column)
                if item and filter_text in item.text().lower():
                    match = True
                    break
            self.email_table.setRowHidden(row, not match)

    def delete_email(self, message):
        try:
            self.gmail.delete_message(message)
            QtWidgets.QMessageBox.information(self, "Sėkmė", "Laiškas ištrintas sėkmingai!")
            self.load_emails()
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Klaida", f"Laiško ištrynimas nepavyko: {e}")

    def mark_emails_as_read(self):
        try:
            filter_text = self.search_input.text().strip()
            self.gmail.mark_as_read(query=filter_text)
            QtWidgets.QMessageBox.information(self, "Sėkmė", "Laiškai pažymėti kaip skaityti.")
            self.load_emails()
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Klaida", f"Nepavyko pažymėti laiškų: {e}")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = GmailApp()
    window.show()
    sys.exit(app.exec())