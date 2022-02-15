#!/usr/bin/env python3

# Miscellaneous operating system interfaces
# https://docs.python.org/3/library/os.html
import os

# Object-oriented filesystem paths
# https://docs.python.org/3/library/pathlib.html
import pathlib

# URL handling modules
# https://docs.python.org/3/library/urllib.html
import urllib

# Support for gzip files
# https://docs.python.org/3/library/gzip.html
import gzip

from pkg.main.exceptions import ContentsFileURLNotFound


def download_contents_file(contents_file_url: str = None,
                           output_dir: str = os.getcwd()+os.sep+"outputs",
                           reuse_contents_file: bool = True) -> str:
    """
    This function takes a Debian Contents-*.gz file and extracts it to the output folder.

    Arguments:
        contents_file_url: Debian Contents-*.gz file URL
        output_dir: Output directory where the file will be downloaded and extracted.
        reuse_contents_file: Reuse a previously downloaded Debian Contents-*.gz file.

    Returns:
        str: path of the content index file that was downloaded and extracted.
    """
    # Check URL list length
    if len(contents_file_url) == 0:
        raise ContentsFileURLNotFound("Contents-*.gz file URL is not found!")

    # Check output directory address
    if output_dir is None:
        output_dir = os.getcwd()+os.sep+"outputs"

    # Check output directory and create it
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    basename = os.path.basename(contents_file_url)
    file_name = os.path.splitext(basename)[0]

    # Contents-*.gz file path
    output_gz_file = pathlib.Path(output_dir) / basename

    # Extracted Contents-*.gz file path
    output_file = pathlib.Path(output_dir) / file_name

    # If Contents-*.gz file exists check reuse flag
    if output_file.exists():
        if reuse_contents_file:
            return output_file

    # Download the Contents-*.gz file
    with urllib.request.urlopen(contents_file_url) as response:
        data = response.read()
    with open(output_gz_file, "wb") as buffer:
        buffer.write(data)

    # Extract the Contents-*.gz file
    with gzip.open(output_gz_file, "rb") as buffer:
        data = buffer.read()
    with open(output_file, "wb") as buffer:
        buffer.write(data)

    return output_file
