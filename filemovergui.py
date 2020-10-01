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
from filemover import create_folder, start


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
