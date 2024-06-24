# Audit Logging System

## Overview
This project implements an audit logging system using Kafka, Redis, Elasticsearch, and Flask. The system consists of a Kafka consumer that reads events from a Kafka topic, processes them, and stores them in Elasticsearch. A Flask API is provided to query the stored events with various filters and caching support via Redis.

## Project Structure
```
audit-logging-system/
├── docker-compose.yml
├── Dockerfile
├── event_consumer/
│   ├── __init__.py
│   ├── consumer.py
│   └── config.py
├── api/
│   ├── __init__.py
│   ├── app.py
│   ├── config.py
│   └── requirements.txt
├── tests/
│   ├── test_consumer.py
│   └── test_api.py
├── scripts/
│   └── setup_kafka.sh
└── README.md
```

## Setup Instructions

### Prerequisites
- Docker
- Docker Compose
- Python 3.9
- pip
- Visual Studio Code (VS Code) for development

### Step 1: Start Services with Docker Compose
1. Open a terminal and navigate to the project directory.
2. Run the following command to start the services:
   ```sh
   docker-compose up -d
   ```

### Step 2: Set Up Kafka Topic
1. Run the setup script to create the Kafka topic:
   ```sh
   bash scripts/setup_kafka.sh
   ```

### Step 3: Run Kafka Consumer
1. Open a terminal and navigate to the project directory.
2. Run the consumer script:
   ```sh
   python event_consumer/consumer.py
   ```

### Step 4: Run Flask API
1. Open another terminal and navigate to the project directory.
2. Install dependencies:
   ```sh
   pip install -r api/requirements.txt
   ```
3. Run the Flask API:
   ```sh
   python api/app.py
   ```

### Testing
- To run the tests, navigate to the `tests/` directory and run:
  ```sh
  python -m unittest test_consumer.py
  python -m unittest test_api.py
  ```

### API Usage
- You can test the API by accessing the following endpoint:
  ```
  GET /events?actor=<actor>&action=<action>&resource=<resource>&tenant_id=<tenant_id>&time_from=<time_from>&time_to=<time_to>
  ```
  Example:
  ```
  GET /events?actor=john_doe&action=user_logged_in
  ```

### File Explanations

#### Docker Compose File (`docker-compose.yml`)
Defines the services required for the system: Zookeeper, Kafka, Redis, Elasticsearch, Flask API, and Kafka consumer.

#### Dockerfile (`Dockerfile`)
Defines the base image and setup instructions for the Docker container running the Flask API.

#### Event Consumer (`event_consumer/`)
- `__init__.py`: Initializes the package.
- `consumer.py`: Contains the Kafka consumer logic.
- `config.py`: Configuration settings for Kafka, Elasticsearch, and Redis.

#### Flask API (`api/`)
- `__init__.py`: Initializes the package.
- `app.py`: Contains the Flask application with endpoints.
- `config.py`: Configuration settings for Elasticsearch and Redis.
- `requirements.txt`: Lists the dependencies for the Flask application.

#### Tests (`tests/`)
- `test_consumer.py`: Tests the Kafka consumer connections.
- `test_api.py`: Tests the Flask API endpoints.

#### Scripts (`scripts/`)
- `setup_kafka.sh`: Script to set up Kafka topics.

## Technology Stack
- **Kafka**: For event streaming.
- **Redis**: For caching query results.
- **Elasticsearch**: For storing and querying event data.
- **Flask**: For providing the REST API.


## Author
Ravi Kumar

## Contact
For any questions or suggestions, please contact me at ravi26067@gmail.com .