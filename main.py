import time
from cleaner.cleaner import FileEraser
from reader.reader import File
from sender.sender import TrendSender
import os

if __name__ == "__main__":
    while True:
        if os.listdir("source") == []:
            continue
        time.sleep(5)
        data = File.read_csv()
        TrendSender.send(data)
        FileEraser.erase()


