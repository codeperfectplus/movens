import os
from pathlib import Path
from shutil import move

# Define categories with subfolders and file extensions
FOLDER_STRUCTURE = {
    # Programming
    'Programming/Python': {'py', 'ipynb', 'pyd', 'pyc'},
    'Programming/JavaScript': {'js', 'ts', 'tsx'},
    'Programming/Java': {'java', 'jar'},
    'Programming/C_CPP': {'c', 'cpp', 'cc', 'h', 'hpp'},
    'Programming/CSharp': {'cs'},
    'Programming/Web': {'html', 'css', 'xml', 'php'},
    'Programming/Kotlin': {'kt'},
    'Programming/VS Extensions': {'vsix'},
    'Programming/Others': {'r', 'go', 'rs', 'dart', 'swift', 'lua', 'sh', 'bat'},

    # Compressed files
    'Compressed': {'zip', 'rar', 'arj', 'gz', 'bz2', '7z', 'xz', 'tar', 'iso'},

    # Applications / Executables
    'Applications/Windows': {'exe', 'msi'},
    'Applications/Linux': {'deb', 'rpm', 'AppImage'},
    'Applications/Android': {'apk'},

    # Images
    'Pictures/RAW': {'raw', 'arw', 'cr2', 'nef', 'orf', 'rw2', 'dng', 'raf', 'pef', 'srw', 'x3f', 'cr3'},
    'Pictures/Photos': {'jpeg', 'jpg', 'png', 'gif', 'tiff', 'webp', 'bmp', 'ico', 'heic', 'jfif'},
    'Pictures/3D': {'3ds', 'blend', 'fbx', 'obj', 'stl', 'dae', 'ply'},
    'Pictures/Vector': {'svg', 'ai'},

    # Videos
    'Videos/Standard': {'mp4', 'webm', 'mkv', 'mov', 'avi', 'flv', 'wmv'},
    'Videos/Legacy': {'qt', 'rm', 'vob', 'mpg', 'mpeg', 'm4v', '3gp', 'mts'},
    'Videos/Streaming': {'ts'},


    # Audio / Music
    'Music': {'mp3', 'aac', 'wma', 'm4a', 'flac', 'ogg', 'opus', 'wav', 'aiff', 'ape', 'mid', 'midi', 'ra'},

    # Torrents
    'Torrents': {'torrent'},

    # Documents
    'Documents/PDF': {'pdf'},
    'Documents/Word': {'doc', 'docx'},
    'Documents/Excel': {'xls', 'xlsx', 'csv'},
    'Documents/PowerPoint': {'ppt', 'pptx', 'pps'},
    'Documents/Text': {'txt', 'md', 'rtf', 'log'},
    'Documents/Notebooks': {'ipynb'},
    'Documents/LaTeX': {'tex', 'bib'},
    'Documents/Code Snippets': {'json', 'yaml', 'yml', 'toml', 'ini'},
    'Documents/Others': {'odt', 'odp', 'ods', 'epub'},

    # Fallback
    'Other': set()
}


def create_folder(path: Path) -> None:
    """Create a folder if it doesn't exist."""
    try:
        path.mkdir(parents=True, exist_ok=True)
        print(f"[✔] Folder ready: {path}")
    except Exception as e:
        print(f"[✖] Failed to create {path}: {e}")


def classify_extension(extension: str) -> str:
    """Return the folder path based on file extension."""
    for folder, extensions in FOLDER_STRUCTURE.items():
        if extension.lower() in extensions:
            return folder
    return 'Other'


def organize_files_in_directory(folder_path: str) -> None:
    """
    Organize files in the given folder into subfolders based on their extensions.

    Args:
        folder_path (str): Path of the folder to organize.
    """
    folder = Path(folder_path).resolve()
    if not folder.exists():
        print(f"[!] Provided path does not exist: {folder_path}")
        return

    current_dir_name = folder.name.lower()
    files_to_move = {}

    for item in folder.iterdir():
        if item.is_file() and not item.name.startswith('.') and '.' in item.name:
            if item.name == Path(__file__).name:
                continue  # Avoid moving the script itself
            extension = item.suffix[1:]  # Remove the dot
            category_path = classify_extension(extension)
            parts = category_path.split('/')
            top_level = parts[0].lower()

            # Determine actual destination path
            if top_level == current_dir_name:
                # Remove the top-level category from path
                destination_folder = '/'.join(parts[1:]) if len(parts) > 1 else ''
            else:
                destination_folder = category_path

            if destination_folder:  # Only move if there's a subfolder
                files_to_move.setdefault(destination_folder, []).append(item)

    for category in files_to_move:
        full_folder_path = folder / category
        create_folder(full_folder_path)
        for file in files_to_move[category]:
            try:
                move(str(file), str(full_folder_path / file.name))
                print(f"  ↳ Moved: {file.name} → {full_folder_path}")
            except Exception as e:
                print(f"[✖] Could not move {file.name}: {e}")


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        organize_files_in_directory(sys.argv[1])
    else:
        organize_files_in_directory(os.getcwd())
