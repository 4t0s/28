import tkinter as tk
from tkinter import simpledialog

class ToDo():
    def __init__(self, root):
        self.root = root
        self.tasks = []
        self.task_list = tk.Listbox(root, 'task_list', bg='white', font=('Helvetica', 12), selectbackground='lightblue')
        self.task_list.pack()
        
        add_button = tk.button(root, 'Add', command=self.create_task)
        add_button.pack()
        update_button = tk.button(root, 'Update', command=self.update_task_list)
        update_button.pack()
        self.root.title("To-Do List")
        self.root.geometry("500x500")
        self.root.resizable(False, False)

        self.label = tk.Label(self.frame, text="To-Do List", font=("Helvetica", 20))
    def create_task(self):
        task = simpledialog.askstring("Create Task", "Enter Task:")
        self.tasks.append(task)
        self.update_task_list()
    def update_task(self):
        index = self.task_list.curselection()
        if(index):
            task = simpledialog.askstring("Update task", "Enter new value:")
            initial_value = self.task_list[index[0]]
            self.tasks.pop(index[0])
            self.tasks.insert(index[0], task)
            self.update_task_list()  
    def update_task_list(self):
        self.task_list.delete(0, tk.END)
        for task in self.tasks:
            self.task_list.insert(tk.END,task)
        
if __name__ == '__main__':
    root = tk.Tk()
    ToDo(root)
    root.mainloop()