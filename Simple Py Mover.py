'''Python program to move file from one folder to another folder.
@author : CodePerfectPLus
@language : Python 3
Website : http://codeperfectplus.github.io/
Github : https://github.com/codePerfectPlus
  ______            __         ____               ____             __     ____   __            
  / ____/____   ____/ /___     / __ \ ___   _____ / __/___   _____ / /_   / __ \ / /__  __ _____
 / /    / __ \ / __  // _ \   / /_/ // _ \ / ___// /_ / _ \ / ___// __/  / /_/ // // / / // ___/
/ /___ / /_/ // /_/ //  __/  / ____//  __// /   / __//  __// /__ / /_   / ____// // /_/ /(__  ) 
\____/ \____/ \__,_/ \___/  /_/     \___//_/   /_/   \___/ \___/ \__/  /_/    /_/ \__,_//____/  

'''
import os
from os import path
from shutil import move

paths = ['Moved Python',
        'Moved Picture',
        'Moved Video',
        'Moved Pdf',
        'Moved Music'
        'CodePerfectPlus']
for root in paths:
    try:  
        os.mkdir(root)  
    except OSError as error:  
        print('Folder Already Exists')
        
pic = ['.jpeg','.jpg','png','gif','tiff','raw']
vid = ['.mp4','.webm','.mkv','.MPG', '.MP2', '.MPEG', '.MPE', '.MPV', '.OGG', '.M4P', '.M4V', '.AVI', '.WMV', '.MOV', '.QT', '.FLV', '.SWF','.AVCHD']
pytho =['.py','.ipynb','.java']
txt = ['.txt','.pdf']
music = [ '.WAV', '.AIF', '.MP3','.MID']
def start():
    for f in os.listdir():
        name , ex = path.splitext(f)
        for i in range(len(pic)):
            if ex == pic[i]:
                move(f,'Moved Picture')
        for i in range(len(vid)):
            if ex == vid[i]:
                move(f,'Moved Video')
        for i in range(len(pytho)):
            if ex == pytho[i]:
                move(f,'Moved Python')
        for i in range(len(txt)):
            if ex == txt[i]:
                move(f,'Moved Pdf')
        for i in range(len(music)):
            if ex == music[i]:
                move(f,'Moved Music')
start()

