print(r"""
   ______            __         ____               ____             __     ____   __            
  / ____/____   ____/ /___     / __ \ ___   _____ / __/___   _____ / /_   / __ \ / /__  __ _____
 / /    / __ \ / __  // _ \   / /_/ // _ \ / ___// /_ / _ \ / ___// __/  / /_/ // // / / // ___/
/ /___ / /_/ // /_/ //  __/  / ____//  __// /   / __//  __// /__ / /_   / ____// // /_/ /(__  ) 
\____/ \____/ \__,_/ \___/  /_/     \___//_/   /_/   \___/ \___/ \__/  /_/    /_/ \__,_//____/    1.0.3
    
   |_____________________________________________________________________________________|
  | || This Program will move files according to their extension in respective folders.|||
  |--------------------------------------------------------------------------------------|
  | //                                     Version : 1.0.3                             //|
  | //                                  Programming : Python3                          //|
  | //                                GitHub : pycontributors                          //|
  | //                                Author : Py-Contributors                         //|  
  | //                             Email : pycontributors@gmail.com                    //|
  | //                          Telegram : https://t.me/pycontributors                 //|
  | //                       Website : http://codeperfectplus.herokuapp.com            //|
  |  --------------------------------------------------------------------------------------
""")
import os
from os import path
from shutil import move
import tkinter as tk


def create_folder():
    paths = [
        "Programming File",
        "Compressed",
        "Application",
        "Picture",
        "Video",
        "Documents",
        "Music",    
        "Torrents"
    ]
    for root in paths:
        try:
            os.mkdir(root)
        except OSError:
            print("Folder Already Exists")

pic = [".jpeg", ".jpg", ".png", ".gif", ".tiff", ".raw", ".webp", ".jfif", ".ico", ".psd", ".svg", ".ai"]
pytho = [".ipynb", ".java", ".cs", ".js", ".vsix",".jar"]
txt = [".txt", ".pdf", ".doc", ".pdf", ".ppt", ".pps", ".docx", ".pptx"]
music = [".mp3", ".wav", ".wma", ".mpa", ".ram", ".ra", ".aac", ".aif", ".m4a", ".tsa"]
zip = [".zip", ".rar", ".arj", ".gz", ".sit", ".sitx", ".sea", ".ace", ".bz2", ".7z"]
app = [".exe", ".msi"]
vid = [".mp4",".webm",".mkv",".MPG",".MP2",".MPEG",".MPE",".MPV",".OGG",".M4P",".M4V",
    ".WMV",".MOV",".QT",".FLV",".SWF",".AVCHD",".avi",".mpg",".mpe",".mpeg",".asf",
    ".wmv",".mov",".qt",".rm",]
torrents = [".torrent"]

def transfer(arr,name,ex,file):
    for i in range(len(arr)):
        if ex == arr[i]:
            move(file,name)

def start():
    for files in os.listdir():
        try:
            _, ex = path.splitext(files)
            transfer(pic,"Picture",ex,files)
            transfer(vid,"Video",ex,files)
            transfer(pytho,"Programming File",ex,files)
            transfer(txt,"Documents",ex,files)
            transfer(music,"Music",ex,files)
            transfer(torrents,"Torrents",ex,files)
            transfer(txt,"Application",ex,files)
            transfer(zip,"Compressed",ex,files)
        except:
            print("Couldn't move file ", files)


if __name__ == "__main__":      
    # Gui
    effects = tk.RAISED

    window = tk.Tk()

    frame_a = tk.Frame(master=window, width=80, relief=effects, borderwidth=8)
    frame_b = tk.Frame(master=window, width=80, relief=effects, borderwidth=9)

    frame_a.grid(row=1, column=1)
    frame_b.grid(row=2, column=1)

    window.rowconfigure(2, minsize=300, weight=1)
    window.columnconfigure(1, minsize=300, weight=1)


    btn = tk.Button(
        master=frame_a,
        text="Create Folder",
        command=create_folder,
        bg="green",
        width=20,
        height=5,
    )
    btn2 = tk.Button(
        master=frame_b, text="Move Now", command=start, bg="red", width=20, height=5
    )
    lbl = tk.Label(
        master=window,
        text="Warning \n First Create Folder Then Click On Move",
        fg="red",
        bg="black",
        width=50,
    )

    lbl.grid(row=0, column=1)
    btn.grid(row=1, column=0)
    btn2.grid(row=1, column=1)
    window.mainloop()
