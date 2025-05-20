FROM debian:12-slim
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
ENV PATH=$JAVA_HOME/bin:$PATH
RUN apt update \
	&& apt install -y curl gpg gpg-agent netcat-openbsd openjdk-17-jre openssh-client openssh-server procps ssh sudo wget \
	&& rm -rf /var/cache/apt/*
RUN ssh-keygen -t rsa -q -N "" -f ~/.ssh/id_rsa \
	&& cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys \
	&& chmod 0600 ~/.ssh/authorized_keys
