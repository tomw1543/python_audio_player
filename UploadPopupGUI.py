from files import FileManager
import tkinter as tk
from tkinter import filedialog, messagebox, ttk 
from tkinter.filedialog import askopenfilenames, askdirectory # For file dialogs
from tkinterdnd2 import DND_FILES, TkinterDnD # For drag-and-drop support
import regex as re
import os
import platform
import pygame, sys, time
class UploadPopup:
    def __init__(self, parent):
        self.top = tk.Toplevel(parent)
        self.top.title("Upload Audio Files")
        self.top.geometry("400x300")
        self.uploaded_files = []
        
        # Add a frame with a white background to look like the container
        frame = tk.Frame(self.top, bg="white", bd=2, relief="solid", padx=20, pady=20)
        frame.place(relx=0.5, rely=0.5, anchor="center")

        # Title label
        title_label = tk.Label(frame, text="Upload Files", font=("Helvetica", 16, "bold"), bg="white")
        title_label.pack(pady=10)

        # Container for drag-and-drop or browse
        self.upload_container = tk.Label(frame, text="Drag files to upload\nor\nBrowse Files", font=("Helvetica", 12, "italic"), 
                            bg="#f5f5f5", fg="#6c757d", width=40, height=6, relief="solid")  # <-- changed from "dashed" to "solid"
        self.upload_container.drop_target_register(DND_FILES)
        self.upload_container.dnd_bind("<<Drop>>", self.drop_files)
        self.upload_container.pack(pady=10)

        # Button to browse files
        browse_button = tk.Button(frame, text="Browse Files", command=self.browse_files, relief="solid", width=20)
        browse_button.pack(pady=5)

        # Button to upload files
        upload_button = tk.Button(frame, text="Upload", command=self.upload_files, relief="solid", width=20)
        upload_button.pack(pady=5)

        # Button to cancel/close
        cancel_button = tk.Button(frame, text="Cancel", command=self.cancel_upload, relief="solid", width=20)
        cancel_button.pack(pady=5)

        # Label to show the selected file
        file_label = tk.Label(frame, text="No file selected", bg="white", fg="black")
        file_label.pack(pady=5)

        # Progress bar for uploading
        progress_bar = ttk.Progressbar(frame, length=200, mode='determinate', maximum=100)
        progress_bar.pack(pady=10)

        # Status label
        status_label = tk.Label(frame, text="Waiting for file upload", bg="white", fg="#6c757d")
        status_label.pack(pady=5)

    def browse_files(self):
        return FileManager.open_files()

    def drop_files(self, event, filesarray=[]):
        file = FileManager.drop_files(self, event)
        filesarray.append(file)
        file = "\n".join(filesarray)
        self.upload_container.config(text=file)

    def upload_files(self):
        return FileManager.upload_files(self)

    def cancel_upload(self):
        pass
