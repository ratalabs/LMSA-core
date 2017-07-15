#!/usr/bin/env python
#-*- coding: utf-8 -*-

try:
    from setuptools import setup, find_packages
except ImportError:
    print('Error importing setup from setuptools. DEFAULTING to disutils.code')
    from distutils.core import setup

version = __import__('blackboard_automation.version').get_version()

setup(
    name = "Blackboard_Assistant",
    version = version,
    description = "A full service Non-invasive automation framework for the Blackboard LMS system.",
    long_description = "", #open("README.rst").read()
    author = "Samuel McCaffrey",
    author_email = "samccaff@asu.edu",
    license = "Apache-2",
    url = "https://github.com/smccaffrey/blackboard_automation",
    keywords = "python automation selenium blackboard",
    classifiers = [
        "Development Status :: Pre-Alpha",
        "Enviroment :: Console",
        "Intended Audience :: Industry/Academic",
        "Operating System :: UNIX",
        "Programming Language :: Python 2.7",
    ]
)
