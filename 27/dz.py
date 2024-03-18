from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QFileDialog, QLabel, QVBoxLayout, QLineEdit 
import sys
from docx import Document
import re
import requests

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My application')
        
        self.widget = QWidget()
        self.label = QLabel("Write your id for json")
        self.layout = QVBoxLayout()
        self.input = QLineEdit()
        self.button = QPushButton('Check')
                
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.input)
        
        self.widget.setLayout(self.layout)
        
        self.button.clicked.connect(self.click)
        self.setCentralWidget(self.widget)
        
        self.id = 0
    def click(self):
        self.id = self.label.text
        url = f'https://jsonplaceholder.typicode.com/posts/{self.id}'
        response = requests.get(url)
        self.label.setText(f'{response}')


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()