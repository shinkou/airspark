FROM airspark/spark
USER root
ARG VIRTUAL_ENV_DIR
ENV VIRTUAL_ENV_DIR=${VIRTUAL_ENV_DIR:-/venv/py3_12}
RUN apt update \
	&& apt install -y build-essential gcc linux-headers-amd64 musl-dev python3-pip python3-dev python3-venv \
	&& rm -rf /var/cache/apt/*
RUN mkdir -p $(dirname $VIRTUAL_ENV_DIR) \
	&& python3 -m venv $VIRTUAL_ENV_DIR
ENV PATH="$VIRTUAL_ENV_DIR/bin:$PATH"
RUN pip3 install "pyspark==${SPARK_VERSION}"
RUN pip3 install "apache-airflow==3.0.0" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-3.0.0/constraints-3.12.txt"
RUN groupadd airflow \
	&& useradd -r -m -g airflow -s /bin/bash airflow
USER airflow
WORKDIR /home/airflow
ENTRYPOINT [""]
