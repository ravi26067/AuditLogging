import unittest
from event_consumer.consumer import connect_elasticsearch, connect_redis

class TestKafkaConsumer(unittest.TestCase):

    def test_elasticsearch_connection(self):
        es = connect_elasticsearch()
        self.assertTrue(es.ping())

    def test_redis_connection(self):
        redis_client = connect_redis()
        self.assertTrue(redis_client.ping())

if __name__ == "__main__":
    unittest.main()
