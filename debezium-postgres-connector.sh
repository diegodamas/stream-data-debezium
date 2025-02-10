docker exec -it debezium curl -H 'Content-Type: application/json' localhost:8083/connectors --data '
{ 
  "name": "conn-postgres-2",
  "config": {
    "connector.class": "io.debezium.connector.postgresql.PostgresConnector",
    "plugin.name": "pgoutput",
    "database.hostname": "postgres",
    "database.port": "5432",
    "database.user": "postgres",
    "database.password": "postgres",
    "database.dbname" : "financial_db",
    "database.server.name": "postgres",
    "table.include.list": "public.transactions",
    "topic.prefix": "cdc",
    "decimal.handling.mode": "string"
  }
}'