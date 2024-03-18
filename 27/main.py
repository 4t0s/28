from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QFileDialog, QLabel, QVBoxLayout, QLineEdit 
import sys
from docx import Document
import re

pattern_password = re.compile(r'^(?=.*[0-9].*)(?=.*[a-z].*)(?=.*[A-Z].*)[0-9a-zA-Z$%#^]{8,}$')
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My application')
        
        self.widget = QWidget()
        self.label = QLabel("Write your password")
        self.layout = QVBoxLayout()
        self.input = QLineEdit()
        self.button = QPushButton('Check')
                
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.input)
        
        self.widget.setLayout(self.layout)
        
        self.button.clicked.connect(self.click)
        self.setCentralWidget(self.widget)
        
        self.dictionary = {}
    def click(self):
        FILE_PATH = "10-million-password-list-top-1000000.txt"
        if pattern_password.match(self.input.text()):
            with open (FILE_PATH, 'r') as file:
                file_data = file.readlines()
                for data in file_data:
                    if data.strip()==self.input.text():
                        self.label.setText('Your password is unsafe')
                        break
                    else:
                        self.label.setText('Your password is valid')
        else:
            self.label.setText('Your password does not have needed  characters and/or length')
app = QApplication([])
window = MainWindow()
window.show()
app.exec()