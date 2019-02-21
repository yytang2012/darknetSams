from setuptools import setup
import os
import sys

_here = os.path.abspath(os.path.dirname(__file__))

if sys.version_info[0] < 3:
    with open(os.path.join(_here, 'README.rst')) as f:
        long_description = f.read()
else:
    with open(os.path.join(_here, 'README.rst'), encoding='utf-8') as f:
        long_description = f.read()

version = {}
with open(os.path.join(_here, 'darknetSams', 'version.py')) as f:
    exec(f.read(), version)

setup(
    name='darknetSams',
    version=version['__version__'],
    description=('Show how to structure a Python project.'),
    long_description=long_description,
    author='Yutao Tang',
    author_email='kissingers800@gmail.com',
    url='https://github.com/yytang2012/darknetSams.git',
    license='MPL-2.0',
    packages=['darknetSams'],
    #   no dependencies in this example
    #   install_requires=[
    #       'dependency==1.2.3',
    #   ],
    #   no scripts in this example
    #   scripts=['bin/a-script'],
    include_package_data=True,
    package_data={
        "darknetSams": [
            "modelConfigs/Cart/cfg/*",
            "modelConfigs/Coco/cfg/*",
            "modelConfigs/Logo/cfg/*",
            "darknet.so"
        ],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6'],
)
