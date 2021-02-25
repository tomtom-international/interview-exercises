FROM alpine:latest
COPY . /opt/src
RUN apk update
RUN apk add \
            g++ \
            cmake \
            make \
            python3 \
            py3-pip

RUN pip install conan
WORKDIR /opt/build
RUN conan profile new default --detect && \
            conan profile update settings.compiler.libcxx=libstdc++11 default

CMD conan install /opt/src -if /opt/build  && \
        cmake /opt/src  -G "Unix Makefiles" -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/opt/install && \
        cmake --build . && \
        cmake --install .

