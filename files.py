

from tkinter.filedialog import askopenfilenames, askdirectory # For file dialogs
from tkinterdnd2 import DND_FILES, TkinterDnD # For drag-and-drop support
import regex as re
import os
import platform
import pygame, sys, time
import shutil
pygame.mixer.init()
class FileManager:
    @staticmethod
    def open_files():
        if platform.system() == "Windows":
                path = r"C:" # REMEMBER TO CHANGE BACK TO "C:\\"
        else:
                path = "/" # Default to root on Unix-like systems
        
        
        if path:

            if platform.system() == "Windows":
                os.startfile(path)
            elif platform.system() == "Darwin":  # macOS
                os.system(f'open "{path}"')
            else:  # Linux
                os.system(f'xdg-open "{path}"')
            
        
    @staticmethod      
    def drop_files(self,event):

        
        raw_str = event.data.strip("{}")
        self.current_file = raw_str
        print(self.current_file)
         # Handle different OS path formats
        paths = re.search(r'[^\\/]+$', raw_str)
        if paths:
           self.cleaned_path = paths.group(0)
           return self.cleaned_path


           
    def upload_files(self): 
        src = self.current_file
        dst = os.getcwd()
        if self.current_file:
            if os.path.exists(src):
                 shutil.copy(src, dst) 
            else:
                print("Source file does not exist.")
                return  
        print("Uploading file...")
        print(f"Source: {src}")
        print(f"Destination: {dst}")
        time.sleep(5) # Simulate upload time
        print("File uploaded successfully.")
        


    

    
    def play_files(self):
        
            if self.current_file:
                file_end_group = re.search(r'\.[^.]+$', self.current_file) # Extract file extension
                file_end = file_end_group.group(0)
                print(file_end)
                if file_end.lower() not in [".mp3", ".wav", ".ogg"]: 
                    return "Invalid file type. Please select an audio file."
                else:

            
                    file_path = self.current_file
                    pygame.mixer.music.load(file_path)
                    pygame.mixer.music.play()
                    return f"Playing: {self.cleaned_path}"

            else:
                return "No file selected"



        #self.playlist_box.delete(0, tk.END)  # Clear existing entries

