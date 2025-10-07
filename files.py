

from tkinter.filedialog import askopenfilenames, askdirectory # For file dialogs
from tkinterdnd2 import DND_FILES, TkinterDnD # For drag-and-drop support
import regex as re
import os
import platform
import pygame, sys, time
import shutil #for shell commands in python (used to copy files)
from mutagen import File #for reading metadata from audio files
pygame.mixer.init()
class FileManager:
    def __init__(self):
        self.current_file = None
    @staticmethod
    def browse_files():
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
            
        
    
    def drop_files(self,event):

        
        raw_str = event.data.strip("{}")
        current_file = raw_str
        print(current_file)
        return current_file
        
        
        
    @staticmethod
    def open_files(): 
         cwd = os.getcwd()
         files_arr = []
         for file in os.listdir(cwd):
              if file.endswith(('.mp3', '.wav', '.ogg')):
                   file_path = os.path.join(cwd,file)
                   files_arr.append(file_path)
                   print(file_path)
              else:
                   print(f"Skipped non-audio file: {file}")
         return files_arr
            

        



           
    def upload_files(self, files): 
        print(files)
        dst = os.getcwd()
        for src in files:
            if src == dst:
                print("Source and destination cannot be the same.")
                continue
            if os.path.exists(src):
                shutil.copy(src, dst) 
                print(f"Uploaded: {src}")
            else:
                print("Source file does not exist.")
         
        


    

    
    def play_files(self, file_path):
        
            if file_path:
                file_end_group = re.search(r'\.[^.]+$', file_path) # Extract file extension
                file_end = file_end_group.group(0)
                print(file_end)
                if file_end.lower() not in [".mp3", ".wav", ".ogg"]: 
                    return "Invalid file type. Please select an audio file."
                else:
                    pygame.mixer.music.load(file_path)
                    pygame.mixer.music.play()
            else:
                return "No file selected"
            

    def pause_files(self):
        pygame.mixer.music.pause()


    def unpause_files(self):
        pygame.mixer.music.unpause()   


    def set_volume(self, value):
        pygame.mixer.music.set_volume(value)

    def getFileLength(self, file_path):
         audio = File(file_path)
         if audio is not None: 
              global total_length
              total_length = audio.info.length
              return total_length #length in seconds 
         else: 
              return 0
         
    def seek(self, position):
         pass
         

