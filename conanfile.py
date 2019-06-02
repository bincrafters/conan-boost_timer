#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/2.0.0@bincrafters/testing")


class BoostTimerConan(base.BoostBaseConan):
    name = "boost_timer"
    version = "1.70.0"

    @property
    def boost_build_requires(self):
        return ["io"]
