# Stream Data App

## Description
This short project aims to generate financial transaction data and send it to a PostgreSQL database. Subsequently, this data will be captured by Debezium and forwarded to a Kafka topic for real-time processing.

## Project Structure
- `data-generator.py`: Script responsible for generating fake data and inserting it into the database.
- `debezium-postgres-connector.sh`: Script for configuring the Debezium connector for PostgreSQL.
- `docker-compose.yml`: Configuration file for setting up the Docker environment for PostgreSQL, Kafka, and Debezium.
- `requirements.txt`: List of dependencies required to run the project.

## Dependencies
Before running the project, install the dependencies listed in `requirements.txt`:
```bash
pip install -r requirements.txt
```

## Database Setup
The PostgreSQL database will run via Docker Compose. Make sure the service is running:
```bash
docker-compose up -d
```

## Execution
1. Run the data generator:
```bash
python data-generator.py
```
This will create the transactions table in the database and insert random records.

2. Configure the Debezium connector to capture changes in the database:
```bash
./debezium-postgres-connector.sh
```

3. Consume the generated events in Kafka using a consumer:
```bash
kafka-console-consumer --bootstrap-server localhost:9092 --topic transactions --from-beginning
```

## Author
This project was developed to demonstrate the integration of a transactional database with a Kafka-based streaming system.

