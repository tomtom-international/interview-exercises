## Using Conan inside a Docker container

First need to build Docker image from Dockerfile:
```bash
$ cd <path to interview-exercises/cpp_cmake_conan>
$ docker build -f Dockerfile -t alpine-conan --force-rm .
```

To build conan package from Docker container, need to share local folder with container:
```bash
$ docker run -it -v$(pwd):/home/conan/project --rm alpine-conan /bin/ash
$ cd /home/conan/project
$ conan create . user/channel --build missing
$ conan remote add myremote http://some.remote.url
$ conan upload "*" -r myremote --all
```
