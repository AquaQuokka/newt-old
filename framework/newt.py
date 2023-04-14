import tkinter as tk
from tkinter import filedialog
import os
import configparser

icon_path = os.path.join(os.path.dirname(__file__), "newt.ico")


class Newt:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Newt")
        self.root.configure(bg="#1E1E1E")  # set background color
        self.root.option_add("*foreground", "white")  # set foreground color
        self.root.iconbitmap(icon_path) # set icon

        # configure text widget
        self.text = tk.Text(self.root, bg="#1E1E1E", fg="white", insertbackground="white", wrap="word", font=("Consolas", 12))

        # configure menu bar
        self.menu_bar = tk.Menu(self.root, bg="#1E1E1E", fg="white", activebackground="#3A3A3A", activeforeground="white")
        self.root.config(menu=self.menu_bar)

        # configure file menu
        self.file_menu = tk.Menu(self.menu_bar, bg="#1E1E1E", fg="white", activebackground="#3A3A3A", activeforeground="white")
        self.file_menu.add_command(label="Open (Ctrl+O)", command=self.open_file)
        self.file_menu.add_command(label="Save As (Ctrl+S)", command=self.save_file_as)
        self.file_menu.add_command(label="Save (Ctrl+S)", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Undo (Ctrl+Z)", command=self.text.edit_undo)
        self.file_menu.add_command(label="Redo (Ctrl+Y)", command=self.text.edit_redo)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Close Window", command=self.root.destroy)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

        self.menu_bar.configure(bg="#1E1E1E")

        # pack text widget
        self.text.pack(fill=tk.BOTH, expand=1)

        # configure scrollbar
        self.scrollbar = tk.Scrollbar(self.text)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.text.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.text.yview)
        
        # configure keyboard shortcuts
        self.root.bind("<Control-o>", self.open_file)
        self.root.bind("<Control-s>", self.save_file)
        self.root.bind("<Control-z>", self.text.edit_undo)
        self.root.bind("<Control-y>", self.text.edit_redo)

    def open_file(self, event=None):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, "r") as file:
                self.text.delete("1.0", tk.END)
                self.text.insert("1.0", file.read())
                self.root.title(f"Newt - {file_path}")

    def save_file(self, event=None):
        if self.root.title() == "Newt":
            # If the file hasn't been saved before, open the "Save As" dialog
            self.save_file_as()
        else:
            # Otherwise, save the file to the current path
            file_path = self.root.title()[8:]
            with open(file_path, "w") as file:
                file.write(self.text.get("1.0", tk.END))

    def save_file_as(self, event=None):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt")
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.text.get("1.0", tk.END))
                self.root.title(f"Newt - {file_path}")

    def run(self):
        self.root.mainloop()

