#########################################################################
#########CREATING DOCKER IMAGE###########################################
#########################################################################
To build docker container image with greeting_app and run it:

1) build docker image with:
$ docker build . -t <image_name>

2) run the greeting_app inside container with following command:
$ docker run --rm <image_name>

For launching unit tests execute following command with previously built image:

$ docker run --rm <image_name> ctest

#########################################################################
#########CREATING CONAN PACKAGE##########################################
#########################################################################

For building conan package and use it one have to:

1) login into container with following command:

$ docker run --rm -w /opt/src  -it <image_name> /bin/sh

2a) build conan package with:

$ conan create .

2b) if one want to run unit tests during package creation:

$ conan create -e CONAN_RUN_TESTS=1 .

3) install package with:

$ conan install greeting_app/1.0.0@ -g virtualrunenv

4) source files with env variables:

$ . ./activate_run.sh

5) run app:

$ greeting_app
