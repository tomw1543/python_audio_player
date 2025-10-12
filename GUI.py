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

        # --- Upload Files Button ---
        self.btn_upload = tk.Button(toolbar, text="Upload Files", command=self.show_upload_dialog)
        self.btn_upload.pack(side=tk.LEFT, padx=5)

        volume_label = tk.Label(toolbar, text="Vol")
        volume_label.pack(side=tk.LEFT, padx=5)

        self.volume_slider = tk.Scale(toolbar, from_=0, to=100, orient=tk.HORIZONTAL, command=self.set_volume)
        self.volume_slider.set(80)
        self.volume_slider.pack(side=tk.LEFT, padx=2)

        self.var_mute = tk.BooleanVar()
        self.btn_mute = tk.Checkbutton(toolbar, text="Mute", variable=self.var_mute, command=self.toggle_mute)
        self.btn_mute.pack(side=tk.LEFT, padx=5)
        

        toolbar.pack(side=tk.TOP, fill=tk.X)


        # --- Playlist and Track Info ---
        main_frame = tk.PanedWindow(root, orient=tk.HORIZONTAL)
        main_frame.pack(fill=tk.BOTH, expand=1)

        self.playlist_box = tk.Listbox(main_frame)
        self.playlist_box.bind('<<ListboxSelect>>', lambda event: (self.get_selected_file(), self.songLength()))
        main_frame.add(self.playlist_box)

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

       

        self.lbl_title = tk.Label(right_frame, text="Add audio files by selecting Upload Files -> Browse Files", wraplength=400)
        self.lbl_title.pack(pady=10, anchor="n")  # anchor north/top
        
        self.image_label = tk.Label(right_frame, image=self.img2)
        self.image_label.pack(padx=20, pady=20)  # anchor north/top

        # Play button at the bottom
        controls_frame = tk.Frame(right_frame)
        controls_frame.pack(side="bottom", pady=(10,50))

        # Buttons arranged left to right inside the controls frame
        self.btn_prev = tk.Button(controls_frame, text="⏮", command=self.play_previous)
        self.btn_prev.pack(side="left", padx=5)

        self.btn_play = tk.Button(controls_frame, text="▶️", command=self.play_pause)
        self.btn_play.pack(side="left", padx=5)
        self.btn_play.bind('<space>', self.play_pause)
        
        


        self.btn_next = tk.Button(controls_frame, text="⏭", command=self.play_next)
        self.btn_next.pack(side="left", padx=5) 

        # Time frame below play button
        time_frame = tk.Frame(right_frame)
        self.lbl_time_current = tk.Label(time_frame, text="0:00")
        self.lbl_time_current.pack(side=tk.LEFT)

        self.seek_slider = tk.Scale(time_frame, from_=0, to=100, orient=tk.HORIZONTAL, command=self.seek)
        self.seek_slider.set(0)

        self.seek_slider.pack(side=tk.LEFT, fill=tk.X, expand=True)

        self.slider_label = tk.Label(time_frame, text=0)
        self.slider_label.pack(pady=10)


        self.lbl_time_total = tk.Label(time_frame, text=())
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
        self.file_playing_counter = 0 #is set to 0 everytime a new file is played
   
   
   
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


    def get_selected_file(self): 
        selection = self.playlist_box.curselection()
        if selection:
            index = selection[0]
            file_name = self.playlist_box.get(index)
            global file_path
            file_path = self.file_dict[file_name]
            print(f"Playing file: {file_path}")
            self.lbl_title.config(text=f"Playing: {file_name}")
            self.image_label.config(image=self.img)  # Update to the desired image impliment functionality later
            FileManager.play_files(self, file_path)
            self.file_playing_counter = 1
            self.btn_play.config(text= "⏸️")
            



    
    def play_pause(self):
        current_text = self.btn_play.cget("text")

       
        
        if current_text == "▶️":
            FileManager.unpause_files(self)
            self.btn_play.config(text= "⏸️")
        elif current_text == "⏸️":
            FileManager.pause_files(self)
            self.btn_play.config(text= "▶️")


        

            

    


    def play_previous(self):
       selection = self.playlist_box.curselection()
       if selection:
           index = selection[0] - 1
           if index >= 0:
               self.playlist_box.select_clear(0, tk.END)
               self.playlist_box.select_set(index)
               self.get_selected_file()
               self.songLength()

    def play_next(self):
       selection = self.playlist_box.curselection()
       if selection:
           index = selection[0] + 1
           if index < self.playlist_box.size():
               self.playlist_box.select_clear(0, tk.END)
               self.playlist_box.select_set(index)
               self.get_selected_file()
               self.songLength()



    def set_volume(self, value):
        value = self.volume_slider.get()
        FileManager.set_volume(self, int(value) / 100)  # Scale 0-100 to 0.0-1.0

    def toggle_mute(self):
        if self.var_mute.get():
            pygame.mixer.music.set_volume(0)
        else:
            value = self.volume_slider.get()
            pygame.mixer.music.set_volume(int(value) / 100)
        

    def seek(self, value):
        self.slider_label.config(text=int(float(value)))



    
    def songLength(self):
        global file_path
        if (FileManager.getFileLength(self, file_path)) != 0:
            total_length = FileManager.getFileLength(self, file_path)
            current_time = pygame.mixer.music.get_pos() // 1000 #convert from ms to seconds
            #print(total_length)
            #print(current_time)
            mins, secs = divmod(current_time, 60)
            mins = round(mins)
            secs = round(secs)
            current_timeformat = '{:02d}:{:02d}'.format(mins, secs)


            total_mins, total_secs = divmod(total_length, 60)
            total_mins = round(total_mins)
            total_secs = round(total_secs)
            total_timeformat = '{:02d}:{:02d}'.format(total_mins, total_secs)
            self.lbl_time_total.config(text= current_timeformat + "of " + total_timeformat)


            # Schedule this function to run again after 1000ms (1 second)
            self.lbl_time_total.after(1000, self.songLength)
           

    
    def show_upload_dialog(self):
        print("Upload dialog opened")
        # Open the custom upload popup
        UploadPopup(self.root, app=self)  # Make sure to pass 'self' as 'app'



    
    def about(self):
        messagebox.showinfo("About", "Audio Player Skeleton\n\nTkinter GUI.\nNo playback functionality implemented yet.")


def main():
    root = TkinterDnD.Tk()
    app = AudioPlayerApp(root)
    root.after(100, app.open_files) # Call open_files after 100ms
    root.mainloop()


if __name__ == "__main__":
    main()
