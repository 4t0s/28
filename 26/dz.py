import tkinter as tk
import requests
import json

root = tk.Tk()
root.title("JSONPlaceholder Data Fetcher")

class MainWindow:
    def __init__(self):
        super().__init__()
        self.frame = tk.Frame(root)
        self.frame.pack()
        self.label = tk.Label(self.frame, text="Enter post ID:")
        self.label.grid(row=0, column=0)
        self.entry = tk.Entry(self.frame)
        self.entry.grid(row=0, column=1)
        self.fetch_button = tk.Button(self.frame, text="Fetch Data", command=self.fetch_data)
        self.fetch_button.grid(row=1)
        self.result_label = tk.Label(self.frame, text="")
        self.result_label.grid(row=2)
    def fetch_data(self):
        post_id = int(self.entry.get())
        response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}")
        data = response.json()
        with open("data.json", "w") as file:
            json.dump(data, file)
        self.result_label.config(text="Data saved successfully!")
    def run(self):
        self.create_window()
        self.window.mainloop()

if __name__ == "__main__":
    app = MainWindow()
    app.run()