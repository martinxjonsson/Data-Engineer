import os
from configparser import ConfigParser


def config(filename=None, section='postgresql'):
    if filename is None:
        base_dir = os.path.dirname(__file__)
        filename = os.path.join(base_dir, 'database.ini')

    parser = ConfigParser()
    parser.read(filename)

    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception(f"Section {section} not found in the {filename} file")
    return db
