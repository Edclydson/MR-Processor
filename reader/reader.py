import pandas as pd
from loader.loader import FileLoader

class File:
    def read_csv():
        df = pd.read_csv(FileLoader._csv_file())
        sections = df["Detalhamento da tendência"]
        search_list = list()
        for section in sections:
            search_list.append(str(section).split(","))
        return search_list
