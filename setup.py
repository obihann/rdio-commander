from distutils.core import setup

setup(
	name='RdioCommander',
	version='1.0.0',
	author='Jeffrey Hann',
	author_email='jeffhann@gmail.com',
	scripts=['bin/rdio'],
	url='http://obihann.github.io/RdioCommander/',
	license='LICENSE',
	description='A Python and AppleScript tool for monitoring the OSX Rdio application.',
    requires=['urwid'],
    classifiers=[
        'Environment :: Console',
        'Operating System :: MacOS :: MacOS X',
    ],
)