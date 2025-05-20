FROM airspark/hadoop
ARG HIVE_VERSION
ENV HIVE_VERSION=${HIVE_VERSION:-3.0.0}
ENV HIVE_HOME=/usr/lib/hive
ENV HIVE_CONF_DIR=$HIVE_HOME/conf
ENV PATH=$HIVE_HOME/bin:$PATH
WORKDIR /data
RUN HIVE_BASE_URL='https://archive.apache.org/dist/hive/' \
	&& HIVE_KEY_URL="$HIVE_BASE_URL/KEYS" \
	&& HIVE_TARBALL="hive-standalone-metastore-${HIVE_VERSION}-bin.tar.gz" \
	&& HIVE_TARBALL_URL="$HIVE_BASE_URL/hive-standalone-metastore-${HIVE_VERSION}/$HIVE_TARBALL" \
	&& curl -o ./KEYS $HIVE_KEY_URL \
	&& curl -o ./$HIVE_TARBALL $HIVE_TARBALL_URL \
	&& curl -o ./$HIVE_TARBALL.asc $HIVE_TARBALL_URL.asc \
	&& curl -o ./$HIVE_TARBALL.sha512 $HIVE_TARBALL_URL.sha512 \
	&& gpg --import ./KEYS \
	&& gpg --verify ./$HIVE_TARBALL.asc \
	&& sha512sum ./$HIVE_TARBALL \
	&& rm ./KEYS ./$HIVE_TARBALL.asc ./$HIVE_TARBALL.sha512 \
	&& tar -zxvf ./$HIVE_TARBALL -C /usr/lib/ \
	&& rm ./$HIVE_TARBALL
RUN ln -sf /usr/lib/apache-hive-metastore-${HIVE_VERSION}-bin $HIVE_HOME \
	&& mv $HIVE_CONF_DIR/metastore-site.xml $HIVE_CONF_DIR/metastore-site.xml.backup
COPY ./hive_conf_dir/* $HIVE_CONF_DIR/
