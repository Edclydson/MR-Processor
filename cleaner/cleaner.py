import os
from loader.loader import FileLoader

class FileEraser:
    def erase():
        os.remove(FileLoader._csv_file())
