# base centos 7
# describe sshd nginx-ssl
# date 20161229

FROM centos
MAINTAINER hcylus

ENV LANG en_US.UTF-8
WORKDIR /root

RUN echo 'install epel repo'
RUN yum -y install epel-release
RUN yum makecache
RUN yum makecache fast

RUN echo 'install system-tools'
RUN yum install -y ntp tree net-tools lsof bind-utils nc lrzsz rsync telnet
	
RUN echo 'install ssh'
RUN yum install -y openssl openssh-server openssh-clients
RUN ssh-keygen -q -t rsa -b 2048 -f /etc/ssh/ssh_host_rsa_key -N ''
RUN ssh-keygen -q -t ecdsa -f /etc/ssh/ssh_host_ecdsa_key -N ''
RUN ssh-keygen -t dsa -f /etc/ssh/ssh_host_ed25519_key  -N ''
	
RUN echo 'install nginx-1.10.2'
RUN yum install -y pcre-devel gcc zlib zlib-devel make openssl-devel
ADD http://nginx.org/download/nginx-1.10.2.tar.gz .
RUN tar xf nginx-1.10.2.tar.gz
RUN cd nginx-1.10.2 && ./configure --prefix=/usr/local/nginx --with-http_ssl_module && make && make install
RUN rm -rf nginx-1.10.2*

RUN echo 'install supervisor'
RUN yum install -y python-pip
RUN pip install supervisor
ADD supervisord.conf /etc/supervisord.conf

EXPOSE 22 80

ENTRYPOINT ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]

