# airspark

This is a docker compose stack which facilitates Apache Hadoop, Apache
Spark, and Apache Airflow for prototyping and testing purposes.

## Requirements

- docker
- docker-compose

## How to Run

Change to the top level of the checked out directory. Then issue the
following commands in order:

```
$ docker-compose --profile=build build
$ docker-compose up init-hadoop init-hms init-spark
$ docker-compose up -d
```

## Accesses

### Spark Shell

```
$ docker-compose exec spark spark-shell
```

### Airflow Web UI

Obtain the credentials from the airflow logs:

```
$ docker-compose logs airflow | grep admin
```

Open your browser of choice and point it to [http://localhost:8080/][1]

Then login with the credentials obtained from the step above.

---
[1]: http://localhost:8080/
