To build docker container with greeting_app and run it:

1) build docker container with:
$ docker build . -t <container_name>

2) run the greeting_app with following command:
$ docker run --rm <container_name>

For launching unite tests execute following command with previoulsy build container:

$ docker run --rm builder ctest

For building conan package and use it one have to:

1) log in into container with following command:

$ docker run --rm -w /opt/src  -it builder /bin/sh

2a) build conan package with:

$ conan create .

2b) if one want to run unite tests during package creation:

$ conan create -e CONAN_RUN_TESTS=1 .

3) install package with:

$ conan install greeting_app/1.0.0@ -g virtualrunenv

4) source files with env variables:

$ . ./activate_run.sh

5) run app:

$ greeting_app
