import random
from broker import broker

class TrendSender:
    def send(search_list):
        for search in search_list:
            if len(search) == 1:
                broker.rabbit_deliver(search[0])
            if len(search) > 1:
                index_section = random.randrange(len(search))
                broker.rabbit_deliver(search[index_section])
