#RdioCommander 1.2.0

A tool for monitoring the Rdio desktop application. Built in Python, and using OSASCRIPT to handle interaction with Rdio.

- https://github.com/obihann/RdioCommander/archive/1.2.0.tar.gz
- SHA1: 0d6a16727b45013b0690cc8aea2a798fe97bb9a5  

##Setup
``` 
$ python setup.py install
```

##Usage
```
$ rdio -h
RDIO COMMANDER 1.2.0
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
```

##Examples
###Dark
```
$ rdio
```
![alt tag](https://raw.github.com/obihann/RdioCommander/master/screenshots/dark.png)
###Light
```
$ rdio -c light
```
![alt tag](https://raw.github.com/obihann/RdioCommander/master/screenshots/light.png)


##Changelog
- 1.0: Initial release
- 1.0.1: Bug fixes
- 1.0.2: Fixing loop
- 1.1.0: Rewriting code that handles arguments to use argeparse
- 1.2.0: Bug fixes, adding duration, adding basic conrols


##License
This tool is protected by the [GNU General Public License v2](http://www.gnu.org/licenses/gpl-2.0.html).

Copyright [Jeffrey Hann](http://jeffreyhann.ca/) 2014
