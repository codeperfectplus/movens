from shutil import move
from os import path
import os


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

folder_ex = {
    "Programming Files": set([".ipynb", ".py", ".java", ".cs", ".js", ".vsix", ".jar"]),
    "Compressed": set([".zip", ".rar", ".arj", ".gz", ".sit", ".sitx", ".sea", ".ace", ".bz2", ".7z"]),
    "Applications": set([".exe", ".msi"]),
    "Pictures":  set([".jpeg", ".jpg", ".png", ".gif", ".tiff", ".raw", ".webp", ".jfif", ".ico", ".psd", ".svg", ".ai"]),
    "Videos":  set([".mp4", ".webm", ".mkv", ".MPG", ".MP2", ".MPEG", ".MPE", ".MPV", ".OGG", ".M4P", ".M4V", ".WMV", ".MOV", ".QT", ".FLV", ".SWF", ".AVCHD", ".avi", ".mpg", ".mpe", ".mpeg", ".asf", ".wmv", ".mov", ".qt", ".rm"]),
    "Documents": set([".txt", ".pdf", ".doc", ".xlsx", ".pdf", ".ppt", ".pps", ".docx", ".pptx"]),
    "Music":  set([".mp3", ".wav", ".wma", ".mpa", ".ram", ".ra", ".aac", ".aif", ".m4a", ".tsa"]),
    "Torrents": set([".torrent"]),
    "Others": set([])
}


def create_folders():
    """Creates the required folders to organize files ('Pictures', 'Videos'...).
    """
    for root in folder_ex:
        try:
            os.mkdir(root)
            print(f"'{root:20}' Created ✔")
        except OSError:
            print(f"'{root:20}' Already Exists")


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
    """Organize files on the current directory, each to the corresponding folder.
    """
    for file in os.listdir():
        # Check it's not filemover.py, a hidden file or a directory
        if file != __file__ and file[0] != '.' and '.' in file:
            try:
                _, ex = path.splitext(file)
                folder = get_folder(ex)
                move(file, folder)
            except KeyError as error:
                print(error)
                print("Couldn't move file ", file)


if __name__ == "__main__":
    create_folders()
    start()
