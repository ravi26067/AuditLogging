from kafka import KafkaConsumer
from elasticsearch import Elasticsearch, helpers
import json
import logging
from redis import Redis
from .config import KAFKA_TOPIC, KAFKA_BOOTSTRAP_SERVERS, ELASTICSEARCH_HOST, REDIS_HOST

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def connect_elasticsearch():
    es = Elasticsearch([ELASTICSEARCH_HOST])
    if es.ping():
        logger.info('Connected to Elasticsearch')
    else:
        logger.error('Elasticsearch connection failed')
    return es

def connect_redis():
    redis_client = Redis(host=REDIS_HOST, port=6379, db=0)
    logger.info('Connected to Redis')
    return redis_client

def consume_messages():
    consumer = KafkaConsumer(
        KAFKA_TOPIC,
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='audit-log-group',
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )

    es = connect_elasticsearch()
    redis_client = connect_redis()
    actions = []

    for message in consumer:
        event = message.value
        action = {
            "_index": "events",
            "_source": event
        }
        actions.append(action)

        if len(actions) >= 1000:
            helpers.bulk(es, actions)
            actions = []

    if actions:
        helpers.bulk(es, actions)

if __name__ == "__main__":
    consume_messages()
