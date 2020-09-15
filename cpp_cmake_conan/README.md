# CMake and Conan basics

*Requirements:*

* Compile with C++11 support
* Conan (>= 1.20)
* CMake (>=3.14)
* C++ compiler (eg. g++, clang, etc.)

## Task 1: Implement a `Greeting` class

* Implement the *greet* method in the skeleton class `Greeting` and let it return `hello`.
* Create unit tests for the class `Greeting`.
  * Use [Catch2](https://github.com/catchorg/Catch2/blob/master/docs/tutorial.md#top) as a testing framework.
* The project has to compile and run tests with CMake/CTest.

## Task 2: Manage Catch2 testing framework dependency with Conan

* Use Conan for downloading the Catch2 testing framework

## Task 3: Create a Conan package of the Greeting project

* Create a Conan package recipe for the Greeting app
* Create the Conan package

## Bonus Task: Build the project within a Docker image

* Create a [Dockerfile](Dockerfile) with all the tools required to build, test and package
  * You can use any Docker base image (eg. Alpine, Ubuntu, etc.)
* Create a markdown file (eg. BUILD.md) how to build the project by using the Docker image
