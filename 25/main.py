import os
import openpyxl
from customtkinter import CTkButton, CTkLabel, CTk


class ExcelFileCounterApp:
    def __init__(self):
        self.excel_counter = None
        self.window = None
        self.label = None
        self.button = None
    
    def create_window(self):
        self.window = CTk()
        self.window.title("Title")
        self.window.geometry('500x500')
        self.label = CTkLabel(text="Click button", font=('Arial', 14), master=self.window)
        self.button = CTkButton(self.window, text='Count', font=('Arial', 14), command=self.display_count)
        self.label.grid(column=0, row=0)
        self.button.grid(column=0, row=1)

    def display_count(self):
        folder_path = "C:\\Users\\Аягоз\\Desktop\\NURASYL\\python\\25\\new"
        total_rows = self.ExcelFileCounter(folder_path)
        self.label.configure(text=f"Total rows in Excel files: {total_rows}")
    def ExcelFileCounter(self, folder_path):
        total_rows = 0
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if filename.endswith(".xlsx"):
                workbook = openpyxl.load_workbook(file_path)
                for sheet in workbook:
                    total_rows += sheet.max_row
        return total_rows

    def run(self):
        self.create_window()
        self.window.mainloop()

if __name__ == "__main__":
    app = ExcelFileCounterApp()
    app.run()
