FROM shinkou/airspark-base
ARG HADOOP_VERSION
ENV HADOOP_VERSION=${HADOOP_VERSION:-3.4.1}
ENV HADOOP_HOME=/usr/lib/hadoop
ENV HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
ENV HADOOP_OPTS="-Djava.library.path=$HADOOP_HOME/lib/native"
ENV PATH=$HADOOP_HOME/bin:$HADOOP_HOME/sbin:$PATH
WORKDIR /data
RUN HADOOP_BASE_URL='https://downloads.apache.org/hadoop/common' \
	&& HADOOP_KEYS_URL="$HADOOP_BASE_URL/KEYS" \
	&& HADOOP_TARBALL="hadoop-${HADOOP_VERSION}.tar.gz" \
	&& HADOOP_TARBALL_URL="$HADOOP_BASE_URL/hadoop-${HADOOP_VERSION}/$HADOOP_TARBALL" \
	&& curl -o ./KEYS $HADOOP_KEYS_URL \
	&& curl -o ./$HADOOP_TARBALL $HADOOP_TARBALL_URL \
	&& curl -o ./$HADOOP_TARBALL.asc $HADOOP_TARBALL_URL.asc \
	&& curl -o ./$HADOOP_TARBALL.sha512 $HADOOP_TARBALL_URL.sha512 \
	&& gpg --import ./KEYS \
	&& gpg --verify ./$HADOOP_TARBALL.asc \
	&& sha512sum ./$HADOOP_TARBALL \
	&& rm ./KEYS ./$HADOOP_TARBALL.asc ./$HADOOP_TARBALL.sha512 \
	&& tar -zxvf ./$HADOOP_TARBALL -C /usr/lib/ \
	&& rm ./$HADOOP_TARBALL
RUN ln -sf /usr/lib/hadoop-${HADOOP_VERSION} $HADOOP_HOME \
	&& mv $HADOOP_CONF_DIR/hadoop-env.sh $HADOOP_CONF_DIR/hadoop-env.sh.default \
	&& cp $HADOOP_HOME/bin/hdfs $HADOOP_HOME/bin/hdfs.default
RUN echo "export JAVA_HOME=$JAVA_HOME" >> $HADOOP_CONF_DIR/hadoop-env.sh \
	&& echo "export HDFS_NAMENODE_USER=root" >> $HADOOP_CONF_DIR/hadoop-env.sh \
	&& echo "export HDFS_DATANODE_USER=root" >> $HADOOP_CONF_DIR/hadoop-env.sh \
	&& echo "export HDFS_SECONDARYNAMENODE_USER=root" >> $HADOOP_CONF_DIR/hadoop-env.sh \
	&& echo "export YARN_RESOURCEMANAGER_USER=root" >> $HADOOP_CONF_DIR/hadoop-env.sh \
	&& echo "export YARN_NODEMANAGER_USER=root" >> $HADOOP_CONF_DIR/hadoop-env.sh \
	&& echo "export YARN_PROXYSERVER_USER=root" >> $HADOOP_CONF_DIR/hadoop-env.sh
COPY ./hadoop_conf_dir/* $HADOOP_CONF_DIR/
RUN groupadd hadoop \
	&& usermod -g root -G hadoop root \
	&& useradd -r -m -g hadoop -s /bin/bash hadoop
USER hadoop
RUN ssh-keygen -t rsa -q -N "" -f ~/.ssh/id_rsa \
	&& cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys \
	&& chmod 0600 ~/.ssh/authorized_keys
USER root
RUN chown -R hadoop:hadoop /usr/lib/hadoop-${HADOOP_VERSION} \
	&& chown hadoop:hadoop $HADOOP_HOME
ENTRYPOINT ["/bin/bash"]
