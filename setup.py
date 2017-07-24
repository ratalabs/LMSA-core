#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name = "LMSA",
      version = "0.1.0",
      description = "A full service Non-invasive automation framework for the Blackboard LMS system.",
      long_description = "",
      author = "Samuel McCaffrey",
      author_email = "samccaff@asu.edu",
      license = "Apache-2",
      url = "https://github.com/smccaffrey/lmsa-core",
      keywords = "python automation selenium blackboard",
      classifiers = [
          "Development Status :: Pre-Alpha",
          "Enviroment :: Console",
          "Intended Audience :: Industry/Academic",
          "Operating System :: UNIX",
          "Programming Language :: Python 2.7",
      ],
      packages=find_packages('src'),
      package_dir={'':'src'},
      install_requires=['selenium',
                        'pandas']
)
