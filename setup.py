#!/usr/bin/env python

from distutils.core import setup

setup(
	name = "rottentomatoes",
	packages = ["rottentomatoes"],
	version = "1.0.3",
	description = "A Python 3 interface to the Rotten Tomatoes API",
	author = "Casey Vega",
	author_email = "casey.vega@gmail.com",
	url = "https://github.com/cvega/WWW-RottenTomatoes-Python"
	download_url = "git@github.com:cvega/WWW-RottenTomatoes-Python.git"
	keywords = ["rest", "api", "json"],
	classifiers = [
		"Programming Language :: Python",
		"Programming Language :: Python :: 3",
		"Development Status :: 5 - Production/Stable",
		"License :: OSI Approved :: GNU General Public License (GPL)",
		"Environment :: Web Environment",
		"Intended Audience :: Developers",
		"Operating System :: OS Independent",
		"Topic :: Software Development :: Libraries :: Python Modules",
		"Topic :: Internet :: WWW/HTTP :: Dynamic Content"
		],
	long_description=open('README').read(),
)
