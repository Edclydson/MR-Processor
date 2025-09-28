from cleaner.cleaner import FileEraser
from reader.reader import File
from sender.sender import TrendSender

if __name__ == "__main__":
    data = File.read_csv()
    TrendSender.send(data)
    FileEraser.erase()

