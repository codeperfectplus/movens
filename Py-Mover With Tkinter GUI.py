head = '''Python program to move file from one folder to another folder.
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
import shutil
import tkinter as tk
''' 
Warning:
    1.Change Your Root Here
'''
window = tk.Tk()
frame = tk.Frame(window)

def create_folder():
    paths = [f'Moved Mp3',
            f'Moved Python',
            f'Moved Picture',
            f'Moved Video',
            f'Moved Pdf',
            f'Moved Text',
            ]
    for path in paths:
        try:  
            os.mkdir(path)
        except OSError as error:  
            print(f'{path[35:]} - File Already Exists Sir !')
            print('*'*40)
        
def start():
    for f in os.listdir():
        if f[-5:] == 'ipynb':
            shutil.move(f,f'Moved Python')
            print(f"Moving {f}")
            print('_'*30)
        elif f[-3:] == 'png':
            shutil.move(f,f'Moved Picture')
            print(f"Moving {f}")
            print('_'*30)
        elif f[-3:] == 'txt':
            shutil.move(f,f'Moved Text')
            print(f"Moving {f}")
            print('_'*30)
        elif f[-3:] == 'pdf':
            shutil.move(f,f'moved pdf')
            print(f"Moving {f}")
            print('_'*30)
        elif f[-4:] == 'jpeg':
            shutil.move(f,f'Moved Picture')
            print(f"Moving {f}")
            print('_'*30)
        elif f[-3:] == 'jpg':
            shutil.move(f,f'Moved Picture')
            print(f"Moving {f}")
            print('_'*30)
        elif f[-3:] == 'mp4':
            shutil.move(f,f'Moved Video')
            print(f"Moving {f}")
            print('_'*30)
        elif f[-4:] == 'webm':
            shutil.move(f,f'Moved Video')
            print(f"Moving {f}")
            print('_'*30)
        elif f[-3:] == 'mp3':
            shutil.move(f,f'Moved Mp3')
            print(f"Moving {f}")
            print('_'*30)
    else:
        print('*'*40)
        print('Sir ! All Files Are Moved Now')
        print('*'*40)
window.rowconfigure(2,minsize=100,weight=1)
window.columnconfigure(1,minsize=100,weight=1)

btn = tk.Button(text='Move Now',command=start)
btn2 = tk.Button(text='Create Folder',command=create_folder)
lbl = tk.Label(text='Warning \n First Create Folder Then Click On Move')
lbl2 = tk.Label(text='change the root in Python file')
lbl.grid(row=0,column=0,sticky='nsew')
lbl2.grid(row=1,column=0,sticky='nsew')
btn2.grid(row=2,column=0)
btn.grid(row=2,column=1)
window.mainloop()