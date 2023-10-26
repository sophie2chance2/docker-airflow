# docker-airflow

## How to Start

1. Run `docker-compose up -d` to start the docker container
2. Open http://localhost:8080/home in the browser
   Might take a minute to load
   Use the default username and password (airflow/airflow) to login if prompted

## How to Stop

1. Run `docker-compose down` to stop the docker container

## Initial Set Up

USED THIS TUTORIAL: https://www.youtube.com/watch?v=K9AnJ9_ZAXE  
Loved it! Super easy to follow.

1. Download docker compose file from apache

```
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.0.1/docker-compose.yaml'
```

2. Create folders for ./dags, ./logs, ./plugins

```
mkdir ./dags ./logs ./plugins
```

3. Initialize docker compose

```
docker-compose up airflow-init
```

4. Start docker compose

```
docker-compose up -d
```

5. Navigate to http://localhost:8080/ and use the default username and password (airflow/airflow) to login.
