import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QFileDialog
import pywhatkit as kit
import datetime
import csv

class WhatsAppBulkSenderApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('WhatsApp Bulk Sender')
        self.setGeometry(300, 300, 400, 200)

        self.phone_label = QLabel('Select CSV file with phone numbers:')
        self.phone_input = QLineEdit(self)

        self.file_button = QPushButton('Select File', self)
        self.file_button.clicked.connect(self.get_csv_file)

        self.message_label = QLabel('Enter the message:')
        self.message_input = QLineEdit(self)

        self.image_label = QLabel('Select folder with images:')
        self.image_input = QLineEdit(self)

        self.image_button = QPushButton('Select Folder', self)
        self.image_button.clicked.connect(self.get_image_folder)

        self.send_button = QPushButton('Send Messages', self)
        self.send_button.clicked.connect(self.send_messages)

        layout = QVBoxLayout()
        layout.addWidget(self.phone_label)
        layout.addWidget(self.phone_input)
        layout.addWidget(self.file_button)
        layout.addWidget(self.message_label)
        layout.addWidget(self.message_input)
        layout.addWidget(self.image_label)
        layout.addWidget(self.image_input)
        layout.addWidget(self.image_button)
        layout.addWidget(self.send_button)

        self.setLayout(layout)
        self.show()

        self.csv_filename = None
        self.image_folder = None

    def get_csv_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        csv_file, _ = QFileDialog.getOpenFileName(self, "Select CSV File", "", "CSV Files (*.csv);;All Files (*)", options=options)
        if csv_file:
            self.csv_filename = csv_file
            self.phone_input.setText(self.csv_filename)

    def get_image_folder(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        folder = QFileDialog.getExistingDirectory(self, "Select Image Folder", options=options)
        if folder:
            self.image_folder = folder
            self.image_input.setText(self.image_folder)

    def send_messages(self):
        if not self.csv_filename or not self.image_folder:
            return

        phone_numbers = []
        with open(self.csv_filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row:  # Check for empty rows
                    phone_numbers.append(row[0])

        message = self.message_input.text()
        image_files = [os.path.join(self.image_folder, filename) for filename in os.listdir(self.image_folder) if filename.lower().endswith(('.jpg', '.jpeg', '.png'))]

        if not phone_numbers:
            print('No phone numbers found in the CSV file.')
            return
        if not image_files:
            print('No image files found in the selected folder.')
            return

        now = datetime.datetime.now()
        hours = now.hour
        minutes = now.minute + 2  # Send messages 2 minutes from now

        for phone_number in phone_numbers:
            image_file = image_files.pop(0)
            kit.sendwhats_image(f"+{phone_number}",img_path=image_file,caption='',wait_time=30)
            kit.sendwhatmsg_instantly(f"+{phone_number}", message, wait_time=30)
            print(f'Message scheduled to send to {phone_number} ')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WhatsAppBulkSenderApp()
    sys.exit(app.exec_())

