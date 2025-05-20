FROM airspark/hadoop
ARG SPARK_VERSION
ENV SPARK_VERSION=${SPARK_VERSION:-3.5.5}
ENV SPARK_HOME=/usr/lib/spark
ENV SPARK_CONF_DIR=$SPARK_HOME/conf
ENV PATH=$SPARK_HOME/bin:$SPARK_HOME/sbin:$PATH
USER root
COPY ./hadoop_conf_dir/* $HADOOP_CONF_DIR/
RUN SPARK_BASE_URL='https://downloads.apache.org/spark' \
	&& SPARK_KEYS_URL="$SPARK_BASE_URL/KEYS" \
	&& SPARK_TARBALL="spark-${SPARK_VERSION}-bin-hadoop3.tgz" \
	&& SPARK_TARBALL_URL="$SPARK_BASE_URL/spark-${SPARK_VERSION}/$SPARK_TARBALL" \
	&& curl -o ./KEYS $SPARK_KEYS_URL \
	&& curl -o ./$SPARK_TARBALL $SPARK_TARBALL_URL \
	&& curl -o ./$SPARK_TARBALL.asc $SPARK_TARBALL_URL.asc \
	&& curl -o ./$SPARK_TARBALL.sha512 $SPARK_TARBALL_URL.sha512 \
	&& gpg --import ./KEYS \
	&& gpg --verify ./$SPARK_TARBALL.asc \
	&& sha512sum ./$SPARK_TARBALL \
	&& rm ./KEYS ./$SPARK_TARBALL.asc ./$SPARK_TARBALL.sha512 \
	&& tar -zxvf ./$SPARK_TARBALL -C /usr/lib/ \
	&& rm ./$SPARK_TARBALL
RUN ln -sf /usr/lib/spark-${SPARK_VERSION}-bin-hadoop3 $SPARK_HOME
COPY ./spark_conf_dir/* $SPARK_CONF_DIR/
RUN useradd -r -m -g hadoop -s /bin/bash spark
USER spark
RUN ssh-keygen -t rsa -q -N "" -f ~/.ssh/id_rsa \
	&& cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys \
	&& chmod 0600 ~/.ssh/authorized_keys
WORKDIR /home/spark
