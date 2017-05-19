try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


config = {
    'description': 'Blackboard Automation Framework',
    'author': 'Sam McCaffrey',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'samccaff@asu.edu',
    'version': '0.1.0',
    'install_requires': ['selenium','pandas'],
    'packages': ['blackboard_automation'],
    'scripts': [],
    'name': 'blackboard automation'
}

setup(**config)
