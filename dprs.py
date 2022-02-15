#!/usr/bin/env python3

"""
Debian Package Repository Statistics (DPRS) Tool

Debian uses *deb packages to deploy and upgrade software.
The packages are stored in repositories and each repository contains the "Contents Index".
The format of that file is well described here: https://wiki.debian.org/RepositoryFormat#A.22Contents.22_indices

This tool takes the architecture (amd64, arm64, i386 etc.) as an argument,
and downloads the compressed Contents-*.gz file associated with it from a Debian package repository mirror.
The program will parse the file and output the statistics of the top 10 packages that have the most files associated with them.

An example output could be:
./dprs.py amd64

1. <package name 1> <number of files>
2. <package name 2> <number of files>
...
10. <package name 10> <number of files>

The following Debian mirror will be used as a default package repository:
http://ftp.uk.debian.org/debian/dists/stable/main/.

Check the README.md file for more information.

"""

from dprs import cli_main

if __name__ == "__main__":
    cli_main()