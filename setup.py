from setuptools import setup, find_packages

version = '0.1.0'

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

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
setup(
    name='PIRT ASU',
    version=version,
    description='Automation Framework for Blackboard',
    long_description=readme,
    author='Kenneth Reitz',
    author_email='me@kennethreitz.com',
    url='https://github.com/kennethreitz/samplemod',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
