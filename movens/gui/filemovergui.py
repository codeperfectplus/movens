import os

import tkinter as tk
from os import path
from shutil import move

print(r'''
   ______            __         ____               ____             __     ____   __            
  / ____/____   ____/ /___     / __ \ ___   _____ / __/___   _____ / /_   / __ \ / /__  __ _____
 / /    / __ \ / __  // _ \   / /_/ // _ \ / ___// /_ / _ \ / ___// __/  / /_/ // // / / // ___/
/ /___ / /_/ // /_/ //  __/  / ____//  __// /   / __//  __// /__ / /_   / ____// // /_/ /(__  ) 
\____/ \____/ \__,_/ \___/  /_/     \___//_/   /_/   \___/ \___/ \__/  /_/    /_/ \__,_//____/  1.0.4
    
  | _____________________________________________________________________________________ |
  | || This Program will move files according to their extension in respective folders.|| |
  | ------------------------------------------------------------------------------------- |
  | //                                     Version : 1.0.4                             // |
  | //                                  Programming : Python3                          // |
  | //                                GitHub : py contributors                         // |
  | //                                Author : Py-Contributors                         // |  
  | //                             Email : pycontributors@gmail.com                    // |
  | //                             Last Update : July 2022                             // |
  | //                          Telegram : https://t.me/pycontributors                 // |
  | //                       Website : http://codeperfectplus.herokuapp.com            // |
  | ------------------------------------------------------------------------------------- |
''')

folder_ex = {
    'Programming Files': set(['ipynb', 'py', 'java', 'cs', 'js', 'vsix', 'jar', 'cc', 'ccc', 'html', 'xml', 'kt']),
    'Compressed': set(['zip', 'rar', 'arj', 'gz', 'sit', 'sitx', 'sea', 'ace', 'bz2', '7z']),
    'Applications': set(['exe', 'msi', 'deb', 'rpm']),
    'Pictures':  set(['jpeg', 'jpg', 'png', 'gif', 'tiff', 'raw', 'webp', 'jfif', 'ico', 'psd', 'svg', 'ai']),
    'Videos':  set(['mp4', 'webm', 'mkv', 'MPG', 'MP2', 'MPEG', 'MPE', 'MPV', 'OGG', 'M4P', 'M4V', 'WMV', 'MOV', 'QT', 'FLV', 'SWF', 'AVCHD', 'avi', 'mpg', 'mpe', 'mpeg', 'asf', 'wmv', 'mov', 'qt', 'rm']),
    'Documents': set(['txt', 'pdf', 'doc', 'xlsx', 'pdf', 'ppt', 'pps', 'docx', 'pptx']),
    'Music':  set(['mp3', 'wav', 'wma', 'mpa', 'ram', 'ra', 'aac', 'aif', 'm4a', 'tsa']),
    'Torrents': set(['torrent']),
    'Other': set([])
}

def create_folders():
    """Creates the required folders to organize files ('Pictures', 'Videos'...).
    """
    for root in folder_ex:
        try:
            os.mkdir(root)
            print('{root:20} Created ✔')
        except OSError:
            print('{root:20} Already Exists')


def get_folder(ext):
    """Returns the Folder that corresponds to the given extension.

    Args:
        ext (String): The extension of the file.

    Returns:
        String: The name of the Folder that holds the ext.
    """
    for f, ex in folder_ex.items():
        if ext in ex:
            return f
    return "Other"



def start():
    '''Organize files on the current directory, each to the corresponding folder.
    '''
    for filename in os.listdir():
        # Check it's not filemover.py, a hidden file or a directory
        if filename != __file__ and filename[0] != '.' and '.' in filename:
            ext = os.path.basename(filename).split('.')[-1]
            folder = get_folder(ext)
            if not os.path.isfile(os.path.join(folder, filename)):
                move(filename, folder)


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
        command=create_folders,
        bg="green",
        width=20,
        height=5,
    )
    btn2 = tk.Button(
        master=frame_b, 
        text="Move Now", 
        command=start, 
        bg="red", 
        width=20, 
        height=5
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
