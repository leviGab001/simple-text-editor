import tkinter as tk
import tkinter.filedialog as filedialog
import tkinter.scrolledtext as scrolledtext

# Initializing the class with the required variables
def __init__(self, master):
    self.master = master
    self.file_path = None
    self.setup_ui()

# Setting up the UI of the text editor window
def setup_ui(self):
    self.master.title("Text Editor")
    self.text_area = scrolledtext.ScrolledText(self.master, wrap=tk.WORD, undo=True)
    self.text_area.pack(fill=tk.BOTH, expand=True)
    self.create_menu()

# Creating the menu bar for the text editor
def create_menu(self):
    menubar = tk.Menu(self.master)
    filemenu = tk.Menu(menubar, tearoff=0)
    filemenu.add_command(label="New", command=self.new_file)
    filemenu.add_command(label="Open", command=self.open_file)
    filemenu.add_command(label="Save", command=self.save_file)
    filemenu.add_command(label="Save As...", command=self.save_file_as)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=self.master.quit)
    menubar.add_cascade(label="File", menu=filemenu)
    self.master.config(menu=menubar)

# Creating a new file
def new_file(self):
    self.file_path = None
    self.master.title("Untitled")
    self.text_area.delete(1.0, tk.END)

# Opening an existing file
def open_file(self):
    file_path = filedialog.askopenfilename()
    if file_path:
        self.file_path = file_path
        self.master.title(self.file_path)
        with open(file_path, "r") as file:
            file_content = file.read()
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.END, file_content)

# Saving the file
def save_file(self):
    if self.file_path:
        with open(self.file_path, "w") as file:
            file.write(self.text_area.get(1.0, tk.END))
    else:
        self.save_file_as()

# Saving the file with a new name
def save_file_as(self):
    file_path = filedialog.asksaveasfilename()
    if file_path:
        self.file_path = file_path
        self.master.title(self.file_path)
        with open(file_path, "w") as file:
            file.write(self.text_area.get(1.0, tk.END))

if __name__ == "__main__":
    root = tk.Tk()
    app = TextEditor(root)
    root.mainloop()
