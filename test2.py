import tkinter as tk
from tkinter import PhotoImage
from PIL import ImageTk
from tkinter import filedialog
from pdf2image import convert_from_path

def open_pdf():
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if file_path:
        images = convert_from_path(file_path)
        display_images(images)

def display_images(images):
    for image in images:
        photo_image = ImageTk.PhotoImage(image)
        # Créer un label avec l'image
        img_label = tk.Label(root, image=photo_image)
        img_label.image = photo_image  # Conserver une référence à l'image pour éviter la suppression par le garbage collector
        img_label.pack()
root = tk.Tk()
root.title("PDF Viewer")

open_button = tk.Button(root, text="Open PDF", command=open_pdf)
open_button.pack()

root.mainloop()

