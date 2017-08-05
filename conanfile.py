from conans import ConanFile, tools, os

class BoostTimerConan(ConanFile):
    name = "Boost.Timer"
    version = "1.64.0"
    generators = "txt" 
    settings = "os", "arch", "compiler", "build_type"
    url = "https://github.com/boostorg/timer"
    description = "Please visit http://www.boost.org/doc/libs/1_64_0/libs/libraries.htm"
    license = "www.boost.org/users/license.html"
    lib_short_name = "timer"
    build_requires = "Boost.Build/1.64.0@bincrafters/testing" 
    requires =  "Boost.Config/1.64.0@bincrafters/testing", \
                      "Boost.System/1.64.0@bincrafters/testing", \
                      "Boost.Core/1.64.0@bincrafters/testing"
 
    def source(self):
        self.run("git clone --depth=50 --branch=boost-{0} {1}.git"
                 .format(self.version, self.url))

    def package(self):
        include_dir = os.path.join(self.build_folder, self.lib_short_name, "include")
        self.copy(pattern="*", dst="include", src=include_dir)

