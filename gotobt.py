
from kafka import KafkaConsumer
consumer = KafkaConsumer('log-movie',group_id='log-movie-consumer',bootstrap_servers=['192.168.3.90:9092'])
for message in consumer:

    print  (message.topic, 
            message.partition,
            message.offset, message.key,
            message.value.decode('utf-8'))