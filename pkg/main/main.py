#!/usr/bin/env python3

# Miscellaneous operating system interfaces
# https://docs.python.org/3/library/os.html
import os

# High-level file operations
# https://docs.python.org/3/library/shutil.html
import shutil

from pkg.main.default_variables import DEFAULT_ARCHITECTURE, DEFAULT_MIRROR_URL, DEFAULT_NUMBER, DEFAULT_OUTPUT_DIR, \
    DEFAULT_REUSE_CONTENTS_FILE, DEFAULT_SORT_DESCENDING, DEFAULT_INCLUDE_UDEB
from pkg.main.download_contents_file import download_contents_file
from pkg.main.get_contents_file_list import get_contents_file_list
from pkg.main.get_contents_file_url import get_contents_file_url
from pkg.main.parse_contents_file import parse_contents_file
from pkg.main.exceptions import *


def main(architecture: str = DEFAULT_ARCHITECTURE,
         clean: bool = False,
         mirror_url: str = DEFAULT_MIRROR_URL,
         number: int = DEFAULT_NUMBER,
         output_dir: str = DEFAULT_OUTPUT_DIR,
         reuse_contents_file: bool = DEFAULT_REUSE_CONTENTS_FILE,
         sort_descending: bool = DEFAULT_SORT_DESCENDING,
         include_udeb: bool = DEFAULT_INCLUDE_UDEB) -> None:
    """
    This is the main function that manages this application.

    Arguments:
        architecture: CPU Architecture for the Debian Contents-*.gz file.
        clean: If clean option set, output directory will be removed.
        mirror_url: Debian Package Repository Address
        number: Number of the top packages to show.
        output_dir: Output directory where the file will be downloaded and extracted.
        reuse_contents_file: Reuse a previously downloaded Debian Contents-*.gz file.
        sort_descending:Sort package statistics by descending order.
        include_udeb: Debian Contents-*.gz file URL.

    Returns:
      None: Returns None.
    """

    # If clean option set, output directory will be removed.
    if clean:
        # Check output directory if exists
        if os.path.exists(output_dir):
            shutil.rmtree(DEFAULT_OUTPUT_DIR)
        exit(0)

    # Get a list of Contents-*.gz file(s) URL(s)
    contents_file_url = get_contents_file_url(architecture=architecture, mirror_url=mirror_url, include_udeb=include_udeb)

    if len(contents_file_url) == 0:
        # If the application couldn't find given architecture,
        # output an error with a list of architectures.
        contents_file_list = get_contents_file_list(mirror_url)
        found_architectures = sorted({item["architecture"] for item in contents_file_list})
        found_architectures = ", ".join(found_architectures)
        # Raise a custom ArchitectureNotFound exception
        raise ArchitectureNotFound(
            f"Architecture: {architecture} was not found in the given Debian Package Repository. "
            f"Available architectures are: {found_architectures}"
        )

    complete_package_data = {}
    for url in contents_file_url:
        contents_file = download_contents_file(
            contents_file_url=url,
            output_dir=output_dir,
            reuse_contents_file=reuse_contents_file)
        print(contents_file)
        package_data = parse_contents_file(contents_file)
        complete_package_data.update(**package_data)

    package_list = complete_package_data.keys()
    # Sort them in the descending order of the number of packages
    # Unless the user wants the ascending order
    package_list = sorted(package_list, key=lambda x: len(complete_package_data[x]), reverse=not sort_descending)

    # Print the output
    for ix, package in enumerate(package_list):
        if ix == 0:
            print(f"{'Order':<10}\t{'Package Name':<40}\t{'Number of Files':>20}")
        print(f"{ix+1:<10}\t{package:<40}\t{len(complete_package_data[package]):>20}")
        if ix+1 == number:
            break
