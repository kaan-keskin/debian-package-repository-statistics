#!/usr/bin/env python3

# Miscellaneous operating system interfaces
# https://docs.python.org/3/library/os.html
import os

# Default Variable Assignments
DEFAULT_ARCHITECTURE_OPTIONS = ['amd64', 'arm64', 'armel', 'armhf', 'i386', 'mips64el', 'mipsel', 'ppc64el', 's390x', None]
DEFAULT_ARCHITECTURE = None
DEFAULT_MIRROR_URL = "http://ftp.uk.debian.org/debian/dists/stable/main/"
DEFAULT_OUTPUT_DIR = os.getcwd()+os.sep+"outputs"
DEFAULT_NUMBER = 10
DEFAULT_REUSE_CONTENTS_FILE = True
DEFAULT_SORT_DESCENDING = True
DEFAULT_INCLUDE_UDEB = False
