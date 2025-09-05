
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

        # Upload Button
        self.upload_button = tk.Button(self.top, text="Upload Files", command=self.upload_files)
        self.upload_button.pack(pady=10)

        # Listbox to show uploaded files
        self.file_listbox = tk.Listbox(self.top, width=50, height=10)
        self.file_listbox.pack(padx=10, pady=10)

        # Remove Selected Button
        self.remove_button = tk.Button(self.top, text="Remove Selected", command=self.remove_selected)
        self.remove_button.pack(pady=5)

        # Close Button
        self.close_button = tk.Button(self.top, text="Done", command=self.top.destroy)
        self.close_button.pack(pady=10)

    def upload_files(self):
        filetypes = [("Audio Files", "*.mp3 *.wav *.ogg"), ("All Files", "*.*")]
        filenames = filedialog.askopenfilenames(title="Select Audio Files", filetypes=filetypes)

        if filenames:
            for file in filenames:
                if file not in self.uploaded_files:
                    self.uploaded_files.append(file)
                    self.file_listbox.insert(tk.END, file.split("/")[-1])
                else:
                    messagebox.showinfo("Info", f"{file} is already added.")

    def remove_selected(self):
        selected = self.file_listbox.curselection()
        if selected:
            index = selected[0]
            self.file_listbox.delete(index)
            del self.uploaded_files[index]
        else:
            messagebox.showwarning("Warning", "No file selected.")
