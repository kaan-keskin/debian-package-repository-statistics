#!/usr/bin/env python3

from collections import defaultdict


def parse_contents_file(contents_file: str) -> dict:
    """
    This function parses a given Debian Contents-*.gz file and
    returns a dictionary with the package names and their associated files.

    Arguments:
        contents_file: Debian Contents-*.gz file path.

    Returns:
        dict: Dictionary containing the packages as keys and
              a list of associated files as the values.
    """
    with open(contents_file) as buffer:
        package_dict = defaultdict(list)
        for line in buffer:
            line = line.strip()
            if line == "":
                # Skip empty lines
                continue
            file_name, packages = line.rsplit(" ", maxsplit=1)
            packages = packages.split(",")
            for package in packages:
                if file_name != "EMPTY_PACKAGE":
                    package_dict[package].append(file_name)
    return package_dict
