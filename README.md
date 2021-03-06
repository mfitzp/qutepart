# Code editor component for PyQt and Pyside

Component has been created for [Enki editor](http://enki-editor.org) as replacement for [QScintilla](http://www.riverbankcomputing.com/software/qscintilla/intro)

[API documentation](https://qutepart.readthedocs.org/en/latest/)

## Features
* Syntax highlighting for 196 languages
* Smart indentation for many languages
* Line numbers
* Bookmarks
* Advanced edit operations
* Matching braces highlighting
* Autocompletion based on document content
* Marking too long lines with red line
* Rectangular selection and copy-paste

## Building and installation on Linux

Qutepart depends on:

* Python 2.7
* PyQt4 (see *Known problems* section)
* pcre

#### 1. Install [pcre](http://www.pcre.org/) and development files
On Debian, Ubuntu and other Linuxes install package `libpcreX-dev`, where `X` is available in your distribution pcre version.
For other OSes - see instructions on pcre website

#### 2. Install Python development files
On Debian, Ubuntu and other Linuxes install package `python-dev`, on other systems - see Python website

#### 3. Install C compiler
It will probably be gcc

#### 4. Build and install the package
`python setup.py install`

## Building and installation on Windows

* Download and install the [CMake binary](http://www.cmake.org/). Tested with 2.8.12.
* Download and install Microsoft Visual Studio Express Edition 2008 (or the full version). This version MUST be used for Python < 3.3 on Windows. Use MSVC 2010 for Python >= 3.3.
* Create a root directory and place the following as subdirectories in it:
    - Download the [pcre source](http://www.pcre.org/). Tested with v. 8.33.
    - Download the latest Qutepart [release](https://github.com/hlamer/qutepart/releases).

#### Make pcre
    cd <pcre-8.33 source>
    mkdir build
    cd build
    cmake .. -DBUILD_SHARED_LIBS:BOOL=OFF -DPCRE_SUPPORT_UTF:BOOL=ON -DPCRE_SUPPORT_JIT:BOOL=ON -G "Visual Studio 9 2008"
    cmake --build . --config Release

#### Build/install Python modules
    cd qutepart
    python setup.py install --include-dir=../pcre-8.33/build --lib-dir=../pcre-8.33/build/Release

## Qutepart and Katepart
[Kate](http://kate-editor.org/) and Katepart (an editor component) is really cool software. The Kate authors and community have created, probably, the biggest set of highlighters and indenters for programming languages.

* Qutepart uses Kate syntax highlighters (XML files)
* Qutepart contains a port from Javascript to Python of Kate indenters (12% of the code base in version 1.0.0)
* Qutepart doesn't contain Katepart code.

Nothing is wrong with Katepart. Qutepart has been created to enable reusing highlighters and indenters in projects where a KDE dependency is not acceptable.


## Author
Andrei Kopats
[hlamer@tut.by](mailto:hlamer@tut.by)

## Known problems
Some PyQt versions have a bug, due which exceptions about QTextBlockUserData are generated.
The bug reproduces on:

* PyQt 4.9.6 from OpenSUSE 12.3 repository

The bug doesn't reproduce on:

* PyQt 4.10 built from sources on OpenSUSE 12.3
* Any PyQt from Ubuntu repositories

If you have information about other versions - let know the author to update this README.


## Bug reports, patches
[Github page](https://github.com/hlamer/qutepart)

## License
LGPL v2
