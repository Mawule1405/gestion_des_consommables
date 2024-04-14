import tkinter as tk
from tkinter import ttk
from openpyxl import Workbook

class ExcelSheet:
    def _init_(self, root):
        self.root = root
        self.root.title("Feuille de calcul Excel")

        self.workbook = Workbook()
        self.sheet = self.workbook.active

        self.tree = ttk.Treeview(self.root)
        self.tree["columns"] = ("A", "B", "C")

        self.tree.heading("#0", text="Row/Column")
        self.tree.heading("A", text="A")
        self.tree.heading("B", text="B")
        self.tree.heading("C", text="C")

        self.tree.pack(expand=True, fill="both")

        self.add_button = tk.Button(self.root, text="Ajouter ligne", command=self.add_row)
        self.add_button.pack()

    def add_row(self):
        row_number = len(self.sheet["A"]) + 1
        self.sheet.append([f"A{row_number}", f"B{row_number}", f"C{row_number}"])
        self.update_treeview()

    def update_treeview(self):
        self.tree.delete(*self.tree.get_children())
        for row in self.sheet.iter_rows(values_only=True):
            self.tree.insert("", "end", text=row[0], values=row[1:])

if __name__ == "__main__":
    root = tk.Tk()
    excel_sheet = ExcelSheet(root)
    root.mainloop()