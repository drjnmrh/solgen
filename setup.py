from setuptools import setup, find_packages
from solgen import get_script_version, get_script_description

setup(
    name = "solgen",
    version = get_script_version(),
    packages = find_packages(),
    #
    install_requires = ['chardet', 'pylint'],
    python_requires = "3.5",
    #
    author = 'O.Z.',
    author_email = 'oleg.v.zhukov@gmail.com',
    license = "MIT",
    description = get_script_description(),
    classifiers = ["Programming Language :: Python :: 3.5"]
)
