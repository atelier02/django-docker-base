FROM ubuntu:16.04
MAINTAINER fnndsc "dev@babymri.org"

ENV PYTHONIOENCODING "utf-8"
ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8
ENV TZ Asia/Tokyo
RUN apt-get update \
  && apt-get install -y curl git sudo vim \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python

# WORKDIR /opt
# RUN git clone https://github.com/taku910/mecab.git
# WORKDIR /opt/mecab/mecab
# RUN ./configure  --enable-utf8-only \
#   && make \
#   && make check \
#   && make install \
#   && ldconfig

# WORKDIR /opt/mecab/mecab-ipadic
# RUN ./configure --with-charset=utf8 \
#  && make \
#  &&make install

# WORKDIR /opt
# RUN git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git
# WORKDIR /opt/mecab-ipadic-neologd
# RUN ./bin/install-mecab-ipadic-neologd -n -y


COPY . /opt/backend
WORKDIR /opt/backend
COPY requirements.txt /opt/backend/

RUN python -m pip install pip --upgrade \
 && python -m pip install -r requirements.txt

RUN useradd -m myuser
USER myuser

CMD exec gunicorn -b 0.0.0.0:$PORT main.wsgi 