#!/bin/bash

docker-compose up -d zookeeper kafka
sleep 10

# Create Kafka topic
docker-compose exec kafka kafka-topics --create --topic user_activities --bootstrap-server kafka:9092 --replication-factor 1 --partitions 1
