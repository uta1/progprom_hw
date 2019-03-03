import pika
import random
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
channel = connection.channel()
channel.queue_declare(queue='queue_hw1')

while True:
    sleepTime = random.randint(0, 5)
    time.sleep(sleepTime)
    message = str(random.randint(100, 1000))
    channel.basic_publish(exchange='', routing_key='queue_hw1', body=message.encode())
connection.close()
