import tkinter as tk
from tkinter import filedialog
import os
import configparser

config = configparser.ConfigParser()
themecfg = configparser.ConfigParser()

icon_path = os.path.join(os.path.dirname(__file__), "newt.ico")
config_path = os.path.join(os.path.dirname(__file__), "config.ini")

with open(config_path, "r") as f:
    config.read_file(f)

theme_path = os.path.join(os.path.dirname(__file__), "themes")
theme_path = os.path.join(theme_path, config["theme"]["default-theme"] + ".ini")

with open(theme_path, "r") as f:
    themecfg.read_file(f)



class Newt:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Newt")
        self.root.configure(bg=f"{themecfg['root']['background']}")  # set background color
        self.root.option_add("*foreground", f"{themecfg['root']['foreground']}")  # set foreground color
        self.root.iconbitmap(icon_path) # set icon

        # configure text widget
        self.text = tk.Text(self.root, bg=f"{themecfg['text']['background']}", fg=f"{themecfg['text']['foreground']}", insertbackground=f"{themecfg['text']['insert-background']}", wrap=f"{themecfg['text']['wrap']}", font=(f"{themecfg['text']['font-family']}", int(themecfg['text']['font-size'])))

        # configure menu bar
        self.menu_bar = tk.Menu(self.root, bg=f"{themecfg['menu-bar']['background']}", fg=f"{themecfg['menu-bar']['foreground']}", activebackground=f"{themecfg['menu-bar']['active-background']}", activeforeground=f"{themecfg['menu-bar']['active-foreground']}")
        self.root.config(menu=self.menu_bar)

        # configure file menu
        self.file_menu = tk.Menu(self.menu_bar, bg=f"{themecfg['file-menu']['background']}", fg=f"{themecfg['file-menu']['foreground']}", activebackground=f"{themecfg['file-menu']['active-background']}", activeforeground=f"{themecfg['file-menu']['active-foreground']}")
        self.file_menu.add_command(label="Open (Ctrl+O)", command=self.open_file)
        self.file_menu.add_command(label="Save As (Ctrl+S)", command=self.save_file_as)
        self.file_menu.add_command(label="Save (Ctrl+S)", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Close Window", command=self.root.destroy)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

        # configure edit menu
        self.edit_menu = tk.Menu(self.menu_bar, bg=f"{themecfg['edit-menu']['background']}", fg=f"{themecfg['edit-menu']['foreground']}", activebackground=f"{themecfg['edit-menu']['active-background']}", activeforeground=f"{themecfg['edit-menu']['active-foreground']}")
        self.edit_menu.add_command(label="Undo (Ctrl+Z)", command=self.text.edit_undo)
        self.edit_menu.add_command(label="Redo (Ctrl+Y)", command=self.text.edit_redo)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)

        self.menu_bar.configure(bg=f"{themecfg['menu-bar']['background']}")

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
        self.root.bind()
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
