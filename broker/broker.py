import pika

def rabbit_deliver(message:str):
    #creating a connection to RabbitMQ server
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='google_trends_queue', durable=True)
    
    #sending the message to the queue
    channel.basic_publish(
        exchange='',
        routing_key='google_trends_queue',
        body=message
    )
    
    connection.close()
