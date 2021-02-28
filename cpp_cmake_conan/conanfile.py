from conans import ConanFile, CMake, tools


class GreetingLibConan(ConanFile):
    name = "greeting_app"
    version = "1.0.0"
    license = "MIT"
    author = "Adam Perdeusz adam.perdeusz@gmail.com"
    url = "https://github.com/Gogler/interview-exercises/tree/solution"
    settings = "os", "compiler", "cppstd", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}
    requires = ("catch2/2.13.4")
    generators = ("cmake_find_package",
                  "cmake_paths"
                  )
    scm = {
        "type": "git",
        "url": "https://github.com/Gogler/interview-exercises.git",
        "revision": "solution"
    }
    exports_sources = "cpp_cmake_conan"

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.configure(source_folder="cpp_cmake_conan")
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()
        if tools.get_env("CONAN_RUN_TESTS", False):
            cmake.test()

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()
        self.copy("*.h", dst="include", src="src")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.dylib*", dst="lib", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["greeting_lib"]
