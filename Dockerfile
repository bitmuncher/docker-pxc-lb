FROM debian:latest
MAINTAINER Frank Fuhrmann <frank.fuhrmann@mailbox.org>

RUN apt-get -y update 
RUN apt-get -y upgrade

RUN apt-get -y install haproxy python

COPY conf/haproxy.cfg /etc/haproxy/haproxy.cfg
COPY start.py /start.py
RUN chmod a+rx /start.py

RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/*

EXPOSE 3306
EXPOSE 8181

CMD sh -c '/start.py && /usr/sbin/haproxy -f /etc/haproxy/haproxy.cfg -p /var/run/haproxy.pid'
