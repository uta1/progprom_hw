import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
channel = connection.channel()
channel.queue_declare(queue='queue_hw1')

def isint(arg):
    try:
        int(arg)
        return True
    except ValueError:
        return False

def callback(ch, method, properties, body):
    message = body.decode()
    if isint(message):
        print(body.decode())
    else:
        print("Error: wrang data recieved")
    sys.stdout.flush()

channel.basic_consume(callback, queue='queue_hw1', no_ack=True)
channel.start_consuming()
