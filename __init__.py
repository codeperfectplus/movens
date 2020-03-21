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

paths = ['Moved Python',
        'Moved Picture',
        'Moved Video',
        'Moved Pdf',
        'Moved Text',
        'README']
for path in paths:
    try:  
        os.mkdir(path)  
    except OSError as error:  
        print(f'{path[36:]} - File Already Exists Sir !')
        print('*'*40)
        
#create Python file

f=open("README/README.txt", "a+")
f.write(head)
f.close()

class Move():
    def __init__(self):
        print('We Are Starting Moving Out Files')

    def start(self):
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
        else:
            print('*'*40)
            print('Sir ! All Files Are Moved Now')
            print('*'*40)

if __name__ == '__main__':
    Move().start()
