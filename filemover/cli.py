from filemover import start

import argparse

parser = argparse.ArgumentParser(description="CLI tool to arrange files smartly")
parser.add_argument("-p", "--path", help="Path of the file to be moved", required=True)

args = parser.parse_args()

def main():
    start(args.path)
    
if __name__ == "__main__":
    main()