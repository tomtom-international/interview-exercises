import os

from conans import ConanFile, CMake, tools


class GreetingLibTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = ("cmake_find_package",
                  "cmake_paths"
                  )

    def build(self):
        cmake = CMake(self)
        # Current dir is "test_package/build/<build_id>" and CMakeLists.txt is
        # in "test_package"
        cmake.configure()
        cmake.build()

    def imports(self):
        self.copy("*.dll", dst="bin", src="bin")
        self.copy("*.dylib*", dst="bin", src="lib")
        self.copy('*.so*', dst='bin', src='lib')

    def test(self):
        if not tools.cross_building(self):
            #os.chdir("bin")
            self.run(".%sexample" % os.sep)
