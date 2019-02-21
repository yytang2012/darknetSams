# darknetSams

Provide a package for coco, cart and logo detection

Need to compile the darknet and provide libdarknet.so to the library path.

Prerequisites:

    sudo apt-get -y install cmake git libopenexr-dev python3-tk
    pip3 install --user Cython



# Install opencv 3.4

    export OPENCV_ROOT=~/Downloads/
    cd $OPENCV_ROOT && git clone https://github.com/opencv/opencv_contrib.git && \
        cd opencv_contrib && git checkout tags/3.4.0 && \
        cd $OPENCV_ROOT && git clone https://github.com/opencv/opencv.git && \
        cd opencv && git checkout tags/3.4.0 && mkdir -p build && cd build && \
        cmake -D CMAKE_BUILD_TYPE=Release \
        cmake -D WITH_TBB=ON -D WITH_OPENMP=ON -D WITH_IPP=ON -D BUILD_PNG=ON \
        -D OPENCV_EXTRA_MODULES_PATH=$OPENCV_ROOT/opencv_contrib/modules \
        -D CMAKE_BUILD_TYPE=RELEASE -D BUILD_EXAMPLES=OFF -D WITH_QT=OFF \
        -D WITH_CUDA=OFF -D BUILD_DOCS=OFF -D BUILD_PERF_TESTS=OFF \
        -D WITH_CSTRIPES=ON -D WITH_OPENCL=ON -D BUILD_opencv_cnn_3dobj=OFF \
        -D CMAKE_INSTALL_PREFIX=/usr/local/ -D BUILD_TESTS=OFF -D WITH_NVCUVID=ON \
        -D BUILD_opencv_dnn_modern=OFF -D WITH_GTK=ON -D WITH_GTK_2_X=ON .. && \
        make -j$(nproc) && sudo make install && sudo ldconfig && cd $OPENCV_ROOT && rm -Rf opencv_contrib && rm -Rf opencv


1. Run the following command to get the darknet project

    - git clone https://github.com/AlexeyAB/darknet.git

    - vim Makefile, and modify the following parameters
    
            GPU=1
            CUDNN=1
            CUDNN_HALF=0
            OPENCV=1
            AVX=0
            OPENMP=0
            LIBSO=1
     
     - make $(nproc)

2. copy the libdarknet.so to the right path

Great resources
===============

- https://manikos.github.io/a-tour-on-python-packaging
- https://docs.python-guide.org/writing/structure/
- http://veekaybee.github.io/2017/09/26/python-packaging/
- https://github.com/audreyr/cookiecutter-pypackage


Recommendations
===============


Python 2 or 3?
--------------

- Develop your code under Python 3, test it for both Python 2 and Python 3
  but consider Python 3 to be the default today.


Split your code into packages, modules, and functions
-----------------------------------------------------

- All code should be inside some function (except perhaps ``if __name__ == '__main__':``).
- Split long functions into smaller functions.
- If you need to scroll through a function over several screens, it is probably too long.
- Functions should do one thing and one thing only.
- Hide internals with underscores.
- Organize related functions into modules.
- If modules grow too large, split them.
- Import from other modules under ``somepackage/`` using ``from .somemodule import something``.
- Do file I/O on the "outside" of your code, not deep inside.


Classes vs. functions
---------------------

- Do not overuse classes.
- Prefer immutable data structures.
- Prefer pure functions.


Naming
------

- Give the subdirectory the same name as your package.
- Before you name your package, check that the name is not taken on https://pypi.org
  (you may want to upload your package to PyPI one day).


Interfaces
----------

- In ``somepackage/__init__.py`` define what should be visible to the outside.
- Use https://semver.org.


Testing
-------

- Test all non-trivial code. I recommend to use https://pytest.org.
- Use Travis CI: https://docs.travis-ci.com/user/languages/python/.


Dependency management
---------------------

- Package dependencies for developers should be listed in ``requirements.txt``.
- Alternatively, consider using http://pipenv.readthedocs.io.
- Package dependencies for users of your code (who will probably install via pip) should be listed in ``setup.py``.


Code style
----------

- Follow PEP8: https://www.python.org/dev/peps/pep-0008/
- Use ``pycodestyle`` to automatically check for PEP8.


Type checking
-------------

- Consider using type hints: https://docs.python.org/3/library/typing.html
- Consider using http://mypy-lang.org.
- Consider verifying type annotations at runtime: https://github.com/RussBaz/enforce


Share your package
------------------

- Choose a license and add a LICENSE file.
- Share your package on PyPI. For this you can follow https://github.com/bast/pypi-howto.


Documentation
-------------

- Use RST for your README (to make it easier for https://pypi.org).


Suggestions? Corrections? Pull requests?
----------------------------------------

Yes please!
