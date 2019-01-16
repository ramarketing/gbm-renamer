import sys

from renamer import Renamer


if __name__ == '__main__':
    Renamer(sys.argv[1:]).handle()
