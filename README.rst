RdioCommander 1.2.1
===================
.. image:: https://travis-ci.org/obihann/RdioCommander.svg?branch=master   :target: https://travis-ci.org/obihann/RdioCommander

A tool for monitoring the Rdio desktop application. Built in Python, and
using OSASCRIPT to handle interaction with Rdio.

-  https://github.com/obihann/RdioCommander/archive/1.2.1.tar.gz

Setup
-----

::

    $ pip install rdiocommander

Usage
-----

::

    $ rdio -h
    RDIO COMMANDER 1.2.1
    https://github.com/obihann/RdioCommander/
    This tool is protected by the GNU General Public License v2.
    Copyright Jeffrey Hann 2014
    ------------------------------------------------------------
    usage: rdio [-h] [-r REFRESH] [-c COLOR]

    optional arguments:
      -h, --help            show this help message and exit
      -r REFRESH, --refresh REFRESH
                            Adjust the number of seconds the app refreshes the
                            screen
      -c COLOR, --color COLOR
                            Specify a light or dark color scheme

Examples
--------

Dark
~~~~

::

    $ rdio

|alt tag| ###Light

::

    $ rdio -c light

.. figure:: https://raw.github.com/obihann/RdioCommander/master/screenshots/light.png
   :alt: alt tag

   alt tag
Changelog
---------

-  1.0: Initial release
-  1.0.1: Bug fixes
-  1.0.2: Fixing loop
-  1.1.0: Rewriting code that handles arguments to use argeparse
-  1.2.0: Bug fixes, adding duration, adding basic conrols
-  1.2.1: Fixing floating point error, ingetrating travis-ci testing

License
-------

This tool is protected by the `GNU General Public License
v2 <http://www.gnu.org/licenses/gpl-2.0.html>`__.

Copyright `Jeffrey Hann <http://jeffreyhann.ca/>`__ 2014

.. |alt tag| image:: https://raw.github.com/obihann/RdioCommander/master/screenshots/dark.png
