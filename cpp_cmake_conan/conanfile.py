from conans import ConanFile, CMake

class GreetingConan(ConanFile):
    name = "greeting"
    version = "0.1"
    requires = "catch2/2.11.1"
    url = "https://github.com/jovanz/interview-exercises.git"
    license = "SPDX"
    description = """This is a Greeting Package."""
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake_find_package"
    scm = {
        "type": "git",
        "url": "https://github.com/jovanz/interview-exercises.git",
        "revision": "solution"
    }

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="cpp_cmake_conan")
        cmake.build()
        # here you can run CTest, launch your binaries, etc
        cmake.test()

    def package(self):
        self.copy(pattern="*greeting_app*", dst="bin", src="app")

    def package_info(self):
        self.cpp_info.name = "greeting"
