#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
import sys
sys.path.insert( 0, '.' )
from olpcgames._version import __version__

from setuptools import setup

setup(
    name = 'OLPCGames',
    version = __version__,
    packages = ['olpcgames'],

    author = "Noah Kantrowitz, Lincoln Quirk, Mike Fletcher",
    author_email = "noah@laptop.org, lincoln@techhouse.org, mcfletch@vrplumber.com",
    description = "Utilities for writing games on the OLPC platform",
    license = "BSD",
    keywords = "olpc games sugar pygame",
    url = "http://wiki.laptop.org/go/Pygame_wrapper",
    classifiers = [
    ],   
)
