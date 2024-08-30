import tkinter as tk 
import tkinter 
import filedialogue,messagebox
from PIL import Image,ImageTk
import os 

class ImageViewer(tk,Tk):
    def __init__(self):
        super().__init__()

        self.title("Image Viewer")
        self.geometry("800x600")
        self.resizable(False,False)

        self.image_list = []

        self.current_image_index = 0 

        self.create_widgets()

    def create_widgets(self):
        self.image_label = tk.Label(self,bg="gray")
        self.image_label.pack(exapnd = True,fill=tk.BOTH)

        button_frame = tk.Frame(self)
        button_frame.pack(fill=tk.X, pady = 10)

        self.prev_button = tk.Button(button_frame,text="Previous")
        self.prev_button.pack(side=tk.LEFT,padx=20)

        self.next_button = tk.Button(button_frame,text="Next")
        self.next_button.pack(side=tk.LEFT,padx=20)

        self.open_button = tk.Button(button_frame,text="Open")
        self.open_button.pack(side=tk.LEFT,padx=20)

    def open_folder(self):
        folder_path = filedialogue.askdirectory()
        if folder_path:
            self.image_list = [os.path.join(folder_path,f) for f in os.listdir(folder_path) if f.lower().endswith(('.png','.jpg','.jpeg','.gif','.bmp'))]
            if self.image_list:
                self.current_image_index = 0
                self.show_image()
            else:
                messagebox.showinfo("Error","No images found in the selected folder.")
    
    