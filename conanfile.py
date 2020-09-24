from conans import ConanFile, CMake, tools


class GreetingConan(ConanFile):
    name = "greeting"
    version = "0.1"
    license = "Apache License 2.0"
    author = "Miroslaw Tworkowski <miroslaw.tworkowski@gmail.com>"
    url = "https://github.com/mtworkowski/interview-exercises.git"
    description = "The Greeting project"
    topics = ("hello", "greeting", "interview")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    generators = "cmake"
    requires = "catch2/2.13.1"

    def source(self):
        git = tools.Git()
        git.clone(self.url, "solution")

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="cpp_cmake_conan")
        cmake.build()

    def package(self):
        self.copy("greeting_app", dst="bin")

    def package_info(self):
        self.cpp_info.bindirs = ["bin"]
