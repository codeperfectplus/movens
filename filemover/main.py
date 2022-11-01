from shutil import move
from os import path
import os

print(r'''
   ______            __         ____               ____             __     ____   __            
  / ____/____   ____/ /___     / __ \ ___   _____ / __/___   _____ / /_   / __ \ / /__  __ _____
 / /    / __ \ / __  // _ \   / /_/ // _ \ / ___// /_ / _ \ / ___// __/  / /_/ // // / / // ___/
/ /___ / /_/ // /_/ //  __/  / ____//  __// /   / __//  __// /__ / /_   / ____// // /_/ /(__  ) 
\____/ \____/ \__,_/ \___/  /_/     \___//_/   /_/   \___/ \___/ \__/  /_/    /_/ \__,_//____/  1.0.5
    
  | _____________________________________________________________________________________ |
  | || This Program will move files according to their extension in respective folders.|| |
  | ------------------------------------------------------------------------------------- |
  | //                                     Version : 1.0.5                             // |
  | //                                  Programming : Python3                          // |
  | //                                GitHub : py contributors                         // |
  | //                                Author : Py-Contributors                         // |  
  | //                             Email : pycontributors@gmail.com                    // |
  | //                             Last Update : November 2022                         // |
  | ------------------------------------------------------------------------------------- |
''')

folder_ex = {
    'Programming Files': set(['ipynb', 'py', 'java', 'cs', 'js', 'vsix', 'jar', 'cc', 'ccc', 'html', 'xml', 'kt', 'c', 'css']),
    'Compressed': set(['zip', 'rar', 'arj', 'gz', 'sit', 'sitx', 'sea', 'ace', 'bz2', '7z']),
    'Applications': set(['exe', 'msi', 'deb', 'rpm']),
    'Pictures':  set(['jpeg', 'jpg', 'png', 'gif', 'tiff', 'raw', 'webp', 'jfif', 'ico', 'psd', 'svg', 'ai']),
    'Videos':  set(['mp4', 'webm', 'mkv', 'MPG', 'MP2', 'MPEG', 'MPE', 'MPV', 'OGG', 'M4P', 'M4V', 'WMV', 'MOV', 'QT', 'FLV', 'SWF', 'AVCHD', 'avi', 'mpg', 'mpe', 'mpeg', 'asf', 'wmv', 'mov', 'qt', 'rm']),
    'Documents': set(['txt', 'pdf', 'doc', 'xlsx', 'pdf', 'ppt', 'pps', 'docx', 'pptx']),
    'Music':  set(['mp3', 'wav', 'wma', 'mpa', 'ram', 'ra', 'aac', 'aif', 'm4a', 'tsa']),
    'Torrents': set(['torrent']),
    'Other': set([])
}


def create_folder(folder_name: str):
    '''
    Creates the folder

    Args:
        folder_name (str): folder to be created
    '''
    try:
        os.mkdir(folder_name)
        print('{} Created ✔'.format(folder_name))
    except OSError:
        print('{} Already Exists'.format(folder_name))


def move_files(folder_path:str, file_folder_map: dict):
    '''
    Move files to respective folder

    Args:
        ext_file_map (dict) : File to Folder map
    '''
    for folder, files in file_folder_map.items():
        for file in files:
            os.makedirs(os.path.join(folder_path, folder), exist_ok=True)
            move(os.path.join(folder_path, file), os.path.join(folder_path, folder))


def get_folder(ext):
    '''
    Returns the Folder that corresponds to the given extension.

    Args:
        ext (String): The extension of the file.

    Returns:
        String: The name of the Folder that holds the ext.
    '''
    for f, ex in folder_ex.items():
        if ext in ex:
            return f
    return 'Other'


def start(folder_path: str): # need to change function name
    '''
    Organize files on the current directory, each to the corresponding folder.
    
    folder_path: The path of the folder to be organized.
    '''

    file_folder_map = dict()
    for filename in os.listdir(folder_path):
        # ignore filemover.py, hidden files or a directory
        if filename == os.path.basename(__file__) or filename[0] == '.' or '.' not in filename:
            continue

        file_extension = os.path.basename(filename).split('.')[-1]
        folder = get_folder(file_extension)

        # ignore files present in the folders
        if os.path.isfile(os.path.join(folder, filename)):
            continue

        # insert file to file_folder_map
        if folder not in file_folder_map:
            file_folder_map[folder] = []
        file_folder_map[folder].append(filename)

    # create required folders
    for folder in file_folder_map.keys():
        create_folder(folder)

    # move files to folder
    move_files(folder_path, file_folder_map)

