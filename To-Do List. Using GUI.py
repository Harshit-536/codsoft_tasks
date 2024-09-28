import tkinter as tk
from tkinter import messagebox

class ToDoList:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.tasks = []
        self.checkboxes = []
        self.checkbutton_widgets = []

        #For GUI Interface
        self.task_list_frame = tk.Frame(self.root)
        self.task_list_frame.pack(padx=10, pady=10)

        self.entry = tk.Entry(self.root, width=40)
        self.entry.pack(padx=10, pady=10)

        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_button.pack(padx=10, pady=10)

        self.delete_button = tk.Button(self.root, text="Delete Tasks", command=self.delete_tasks)
        self.delete_button.pack(padx=10, pady=10)

    def add_task(self):
        task = self.entry.get()
        if task != "":
            self.tasks.append(task)
            checkbox = tk.BooleanVar()
            checkbox.set(False)
            self.checkboxes.append(checkbox)
            checkbutton = tk.Checkbutton(self.task_list_frame, text=task, variable=checkbox)
            checkbutton.pack(anchor=tk.W)
            self.checkbutton_widgets.append(checkbutton)
            self.entry.delete(0, tk.END)

    def delete_tasks(self):
        for i in range(len(self.checkboxes) - 1, -1, -1):
            if self.checkboxes[i].get():
                self.tasks.pop(i)
                self.checkboxes.pop(i)
                self.checkbutton_widgets[i].destroy()
                self.checkbutton_widgets.pop(i)

root = tk.Tk()
my_gui = ToDoList(root)
root.mainloop()