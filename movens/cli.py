import sys
sys.path.append('.')
from movens.main import organize_files_in_directory
from movens.about import __version__

import argparse

parser = argparse.ArgumentParser(prog="Movens", description="CLI tool to arrange files smartly")
parser.add_argument("-p", "--path", help="Path of the file to be moved", required=True)
parser.add_argument("-v", "--version", action="version", version=__version__)

args = parser.parse_args()


def main():
    organize_files_in_directory(args.path)


if __name__ == "__main__":
    main()
