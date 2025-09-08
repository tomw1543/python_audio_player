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

        self.btn_play = tk.Button(toolbar, text="▶️", command=self.toggle_play_pause)
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

        right_frame = tk.Frame(main_frame)
        self.lbl_title = tk.Label(right_frame, text="Drop audio files here or use File → Open…", wraplength=400)
        self.lbl_title.pack(pady=10)
        # Text box to display dropped files
        self.text_box = tk.Listbox(right_frame , width=40, height=15)
        self.text_box.pack(fill="y", padx=(2,0), pady=(0, 10), anchor="n")
        self.text_box.drop_target_register(DND_FILES)
        self.text_box.dnd_bind("<<Drop>>", self.drop_files)
        play_btn = tk.Button(right_frame, text="Play", command=self.play_files)
        play_btn.pack(side="bottom", pady=10)

        

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

    # --- Placeholder Functions ---

    def play_files(self):
        self.text_box.delete(0, tk.END)
        
        play_files= FileManager.play_files(self)
        self.lbl_title.config(text=play_files)
    def drop_files(self, event):
        file = FileManager.drop_files(self, event)
        self.text_box.insert(tk.END, file)
    


    def play_previous(self):
        pass

    def play_next(self):
        pass

    def toggle_play_pause(self):
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
        UploadPopup(self.root)


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
    root.mainloop()


if __name__ == "__main__":
    main()
