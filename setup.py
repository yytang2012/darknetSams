from setuptools import setup
from setuptools.command.install import install as _install
import os
import sys

_here = os.path.abspath(os.path.dirname(__file__))

if sys.version_info[0] < 3:
    with open(os.path.join(_here, 'README.md')) as f:
        long_description = f.read()
else:
    with open(os.path.join(_here, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()

version = {}
with open(os.path.join(_here, 'darknetSams', 'version.py')) as f:
    exec(f.read(), version)


class install(_install):
    def run(self):
        _install.run(self)

        libso_path = os.path.join(_here, "darknetSams", "libdarknet.so")
        if os.path.isfile(libso_path) is False:
            dir_path = os.path.join(_here, "darknet")
            if os.path.isdir(dir_path) is False:
                os.system("git clone https://github.com/yytang2012/darknet.git")
            os.system("cd {} && git pull && make -j$(nproc) && mv libdarknet.so {}".format(dir_path, libso_path))

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
            "libdarknet.so"
        ],
    },
    cmdclass={'install': install},
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6'],
)
