from os import path
from glob import glob

class FileLoader:
    def _csv_file() -> str:
        main = path.join("G:\\")
        downloads = path.join(main, "Meu Drive", "Github", "MR-Processor", "source")
        for file in glob(path.join(downloads, "trending_BR_*.csv")):
            if path.isfile(file):
                return file