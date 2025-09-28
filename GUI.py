"""
Audio Player Skeleton (Tkinter, audio-only GUI)
---------------------------------------------
This is a learning-first skeleton for a cross‑platform audio player GUI in Python.
It uses:
  - Tkinter for the GUI

Note: This version has no playback functionality. Functions are defined but empty.
Your task will be to fill them in step-by-step.
"""

#import files
from UploadPopupGUI import UploadPopup
from files import FileManager
import tkinter as tk
from tkinter import filedialog, messagebox, ttk 
from tkinter.filedialog import askopenfilenames, askdirectory # For file dialogs
from tkinterdnd2 import DND_FILES, TkinterDnD # For drag-and-drop support
import regex as re
import os
import platform
import pygame, sys, time
from PIL import Image, ImageTk

class AudioPlayerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Audio Player (Skeleton)")
        self.root.geometry("800x500")

        # --- Menu ---
        menubar = tk.Menu(root)
        # ...existing code...

        # --- Toolbar ---
        toolbar = tk.Frame(root, bd=1, relief=tk.RAISED)

        self.btn_prev = tk.Button(toolbar, text="⏮", command=self.play_previous)
        self.btn_prev.pack(side=tk.LEFT, padx=2, pady=2)

        self.btn_play = tk.Button(toolbar, text="▶️", command=self.stop)
        self.btn_play.pack(side=tk.LEFT, padx=2, pady=2)

        self.btn_stop = tk.Button(toolbar, text="⏹", command=self.stop)
        self.btn_stop.pack(side=tk.LEFT, padx=2, pady=2)

        self.btn_next = tk.Button(toolbar, text="⏭", command=self.play_next)
        self.btn_next.pack(side=tk.LEFT, padx=2, pady=2)

        # --- Upload Files Button ---
        self.btn_upload = tk.Button(toolbar, text="Upload Files", command=self.show_upload_dialog)
        self.btn_upload.pack(side=tk.LEFT, padx=5)

        volume_label = tk.Label(toolbar, text="Vol")
        volume_label.pack(side=tk.LEFT, padx=5)

        self.volume_slider = tk.Scale(toolbar, from_=0, to=100, orient=tk.HORIZONTAL, command=self.set_volume)
        self.volume_slider.set(80)
        self.volume_slider.pack(side=tk.LEFT, padx=2)

        self.btn_mute = tk.Checkbutton(toolbar, text="Mute", command=self.toggle_mute)
        self.btn_mute.pack(side=tk.LEFT, padx=5)

        toolbar.pack(side=tk.TOP, fill=tk.X)


        # --- Playlist and Track Info ---
        main_frame = tk.PanedWindow(root, orient=tk.HORIZONTAL)
        main_frame.pack(fill=tk.BOTH, expand=1)

        self.playlist_box = tk.Listbox(main_frame)
        main_frame.add(self.playlist_box)
        self.playlist_box.bind("<Double-Button-1>", self.get_selected_file)  # Bind double-click event

        # Text box to display eminem
        # Load and resize
        img = Image.open("Eminem.png")
        img = img.resize((200, 200))   # width=200, height=200
        self.img = ImageTk.PhotoImage(img)

        img2 = Image.open("tame.png")
        img2 = img2.resize((200, 200))
        self.img2 = ImageTk.PhotoImage(img2)

        # Place inside Label
        right_frame = tk.Frame(main_frame)

       

        self.lbl_title = tk.Label(right_frame, text="Drop audio files here or use File → Open…", wraplength=400)
        self.lbl_title.pack(pady=10, anchor="n")  # anchor north/top

        self.image_label = tk.Label(right_frame, image=self.img2)
        self.image_label.pack(padx=20, pady=20)  # anchor north/top

        # Play button at the bottom
        play_btn = tk.Button(right_frame, text="Play", command=self.play_files)
        play_btn.pack(side="bottom", pady=10)

        # Time frame below play button
        time_frame = tk.Frame(right_frame)
        self.lbl_time_current = tk.Label(time_frame, text="0:00")
        self.lbl_time_current.pack(side=tk.LEFT)

        self.seek_slider = tk.Scale(time_frame, from_=0, to=1000, orient=tk.HORIZONTAL, command=self.seek)
        self.seek_slider.pack(side=tk.LEFT, fill=tk.X, expand=True)

        self.lbl_time_total = tk.Label(time_frame, text="--:--")
        self.lbl_time_total.pack(side=tk.RIGHT)
        time_frame.pack(fill=tk.X, pady=5)

        main_frame.add(right_frame)


        # --- Status Bar ---
        self.status = tk.Label(root, text="Ready", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status.pack(side=tk.BOTTOM, fill=tk.X)

        # Initilized objects
        self.file_manager = FileManager() # Create an instance of the file manager
        self.file_dict = {} # Dictionary to hold file paths and names
        self.filesarr = self.file_manager.open_files() #list of raw audio file paths in cwd
   
   
   
    # --- Functions ---

    def open_files(self):
        self.file_dict.clear()
        self.playlist_box.delete(0, tk.END)  # Clear existing entries
        
        for file in self.filesarr:
            cleaned_file = re.sub(r'.*[\\\/]([^\\\/]+)\.[^.]+$', r'\1', file)  # Remove path, keep filename
            self.file_dict[cleaned_file] = file  # Map cleaned name to full path
            self.playlist_box.insert(tk.END, cleaned_file)  # Insert cleaned name into playlist box
        

    def play_files(self):
        self.Album_cover_box.delete(0, tk.END)
        
        play_files= FileManager.play_files(self)
        self.lbl_title.config(text=play_files)
    def drop_files(self, event):
        file = FileManager.drop_files(self, event)
        self.Album_cover_box.insert(tk.END, file)

    
    def get_selected_file(self, event): 
        selection = event.widget.curselection()
        if selection:
            index = selection[0]
            file_name = self.playlist_box.get(index)
            self.file_path = self.file_dict[file_name]
            print(f"Playing file: {self.file_path}")
            self.lbl_title.config(text=f"Playing: {file_name}")
            self.image_label.config(image=self.img)  # Update to the desired image impliment functionality later
            FileManager.play_files(self, self.file_path)
            



    
    def play_pause(self, event):
        pass

            

    


    def play_previous(self):
        pass

    def play_next(self):
        pass

  

    def stop(self):
        pass

    def set_volume(self, value):
        pass

    def toggle_mute(self):
        pass

    def seek(self, value):
        pass

    
    def show_upload_dialog(self):
        print("Upload dialog opened")
        # Open the custom upload popup
        UploadPopup(self.root, app=self)  # Make sure to pass 'self' as 'app'


        '''
        files = filedialog.askopenfilenames(
            title="Select Audio Files",
            filetypes=[("Audio Files", "*.mp3 *.wav *.ogg *.flac"), ("All Files", "*.*")]
        )
        if files:
            popup = tk.Toplevel(self.root)
            popup.title("Uploaded Files")
            popup.geometry("400x300")
            tk.Label(popup, text="Uploaded Files:").pack(pady=5)
            listbox = tk.Listbox(popup, width=50, height=12)
            listbox.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
            for f in files:
                listbox.insert(tk.END, f)
            tk.Button(popup, text="Close", command=popup.destroy).pack(pady=5)

'''
    
    def about(self):
        messagebox.showinfo("About", "Audio Player Skeleton\n\nTkinter GUI.\nNo playback functionality implemented yet.")


def main():
    root = TkinterDnD.Tk()
    app = AudioPlayerApp(root)
    root.after(100, app.open_files) # Call open_files after 100ms
    root.mainloop()


if __name__ == "__main__":
    main()
