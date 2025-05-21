# airspark

This is a docker compose stack which facilitates Apache Hadoop, Apache
Spark, and Apache Airflow for prototyping and testing purposes.

## Requirements

- docker
- docker-compose

## How to Run

First, change to the top level directory of the checkout.

If you want to build your own docker images, do this optional step before
bringing up the stack:

```
$ docker-compose --profile=build build
```

Then, if it is your first time running the stack, or if you have deleted the
persistence volumes, do these to initialize them:

```
$ docker-compose up init-hadoop init-hms init-spark
$ docker-compose --profile=init down  # remove containers for initialization
```

Finally, issue the following command to bring up the stack:

```
$ docker-compose up -d
```

## Accesses

### Spark Shell

```
$ docker-compose exec spark spark-shell
```

### pyspark

```
$ docker-compose exec airflow pyspark
```

### Airflow Web UI

Obtain the credentials from the airflow logs:

```
$ docker-compose logs airflow | grep admin
```

Open your browser of choice and point it to [http://localhost:8080/][1]

Then login with the credentials obtained from the step above.

### Airflow DAGs

Simply copy the `.py` files into the `dags` directory, then they will show
up in the web UI once airflow loads them in.

## How to Stop

Change to the top level directory of the checkout and do this:

```
$ docker-compose down
```

Optionally, you can delete the persistence volumes to start fresh next time:

```
$ docker volume rm airspark_pv-hadoop-log airspark_pv-hdfs airspark_pv-hms airspark_pv-spark-log
```

---
[1]: http://localhost:8080/
