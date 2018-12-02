#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.68.0@bincrafters/testing")

class BoostTimerConan(base.BoostBaseConan):
    name = "boost_timer"
    url = "https://github.com/bincrafters/conan-boost_timer"
    lib_short_names = ["timer"]
    options = {"shared": [True, False]}
    default_options = "shared=False"
    source_only_deps = [
        "io",
        "throw_exception"
    ]
    b2_requires = [
        "boost_chrono",
        "boost_config",
        "boost_core",
        "boost_system"
    ]
    b2_build_requires = ["boost_io"]
