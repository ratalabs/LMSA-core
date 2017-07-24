import ConfigParser
import os

def load_config(path=os.path.expanduser('~/.lmsa.cfg')):
    config = ConfigParser.ConfigParser()
    config.readfp('defaults.cfg')
    config.read(path)
    return config
