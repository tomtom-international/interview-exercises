FROM alpine:3.13

# http://bugs.python.org/issue19846
# > At the moment, setting "LANG=C" on a Linux system *fundamentally breaks Python 3*, and that's not OK.
ENV LANG C.UTF-8

# if this is called "PIP_VERSION", pip explodes with "ValueError: invalid truth value '<VERSION>'"
ENV PYTHON_PIP_VERSION 21.1
# https://github.com/pypa/get-pip
ENV PYTHON_GET_PIP_URL https://github.com/pypa/get-pip/raw/ab9dde151f662745c13461f00c453dcf32a51ea9/public/get-pip.py
ENV PYTHON_GET_PIP_SHA256 0ed17e859b835ad5bf00851f4dc8bbc3520c13dfff6c131d410cdb3a92ff0af9

RUN apk add --update --no-cache \
    ca-certificates wget build-base make ninja git cmake clang \
    python3 \
    && ln -sf python3 /usr/bin/python && \
    wget -O get-pip.py "$PYTHON_GET_PIP_URL" && \
	echo "$PYTHON_GET_PIP_SHA256 *get-pip.py" | sha256sum -c - && \
	python get-pip.py --disable-pip-version-check --no-cache-dir "pip==$PYTHON_PIP_VERSION" && \
	pip install conan
