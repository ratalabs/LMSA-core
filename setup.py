from setuptools import setup, find_packages

version = '0.1.0'

setup(name="PIRT ASU",
      version=version,
      author="Sam McCaffrey",
      author_email="samccaff@asu.edu",
      license="Apache-2.0",
      packages=find_packages('src'),
      package_dir={'': 'src'},
      scripts=['scripts/bulk_upload'],
      install_requires=['selenium',
                        'xlrd',
                        ],
      zip_safe=True,
)
