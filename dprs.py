#!/usr/bin/env python3

"""
Debian Package Repository Statistics (DPRS) Tool

Debian uses *deb packages to deploy and upgrade software.
The packages are stored in repositories and each repository contains the "Contents index".
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

from pkg.main.cli_arg_parser import cli_arg_parser
from pkg.main.main import main

if __name__ == "__main__":
    args = cli_arg_parser()
    main(architecture=args.architecture,
         clean=args.clean,
         mirror_url=args.mirror_url,
         number=args.number,
         output_dir=args.output_dir,
         reuse_contents_file=args.reuse_contents_file,
         sort_descending=args.sort_descending,
         include_udeb=args.include_udeb,
         )
