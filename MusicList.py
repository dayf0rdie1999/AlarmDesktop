# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 16:57:57 2020

@author: Duong Anh Vu

Description: Creating an entire new class called musiclist to contain all the directory of the music in the folder for easy accessability 
"""

import pygame
import os
from pathlib import Path
import shutil
import sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
    # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
            base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def main():
    
    musicalList = musicList();
    
    


#    pathFolder = r"C:\Users\Owner\Desktop\AlarmClockDesign\sound"
#    fileList = os.listdir(pathFolder)
#    print(fileList)
    
#    songPath = os.path.abspath(os.path.join(pathFolder,fileList[0]))
#    pygame.mixer.init()
#    pygame.mixer.pre_init(44100, -16, 2, 2048)
#    pygame.init()
#    pygame.mixer.music.load(songPath)
#    pygame.mixer.music.play()
  
    
class musicList():
    def __init__(self):
        self.getMusicList()
          
    def getMusicList(self):
        self.root = resource_path(Path("sound").absolute())
        self.fileList = os.listdir(self.root)
        
    
    def playSong(self,song):
        songPath = resource_path(os.path.abspath(os.path.join(self.root,song)))
        pygame.mixer.init()
        pygame.mixer.pre_init(44100, -16, 2, 2048)
        pygame.init()
        pygame.mixer.music.load(songPath)
        pygame.mixer.music.play()
        
        
    def addSong(self,songpath):
        try:
            shutil.copy(songpath,self.root)
            self.getMusicList()
        except:
            self.Warning = "It is the same file, Check Your ComboBox"
            print(self.Warning)
            
    def stopPlay(self):
        pygame.mixer.music.stop()
        
if __name__ == "__main__": main()