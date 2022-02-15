#!/usr/bin/env python3

# Extensible library for opening URLs
# https://docs.python.org/3/library/urllib.request.html
import urllib.request
from urllib.error import URLError

from pkg.main.default_variables import DEFAULT_MIRROR_URL
from pkg.main.exceptions import *


def get_contents_file_list(mirror_url: str = DEFAULT_MIRROR_URL) -> list:
    """
    This function returns a list of dictionaries extracted from Contents-*.gz file
    in the given Debian Package Repository Address.

    Arguments:
        mirror_url: Debian Package Repository Address

    Returns:
        list: List of dictionaries with the following structure:
        [
        {
            "architecture": "amd64",
            "filename": "Contents-amd64.gz",
            "url": http://ftp.uk.debian.org/debian/dists/stable/main/Contents-amd64.gz"
        },
        {
            "architecture": "arm64",
            "filename": "Contents-arm64.gz",
            "url": http://ftp.uk.debian.org/debian/dists/stable/main/Contents-arm64.gz"
        },
        {
            "architecture": "i386",
            "filename": "Contents-i386.gz",
            "url": http://ftp.uk.debian.org/debian/dists/stable/main/Contents-i386.gz"
        },
        ...
        ]
    """
    try:
        with urllib.request.urlopen(mirror_url) as url_opener_response:
            raw_html = url_opener_response.read()
    except URLError:
        # TODO: Add more functionality. Doing nothing for now!
        raise MirrorURLNotAccessible("Debian Package Repository URL is not accessible!")
    html = raw_html.decode()
    """
    HTML content will be similar to the following structure:
        ...
        <a href="Contents-all.gz">Contents-all.gz</a>
        <a href="Contents-amd64.gz">Contents-amd64.gz</a>
        <a href="Contents-arm64.gz">Contents-arm64.gz</a>
        <a href="Contents-i386.gz">Contents-i386.gz</a>
        ...
        <a href="Contents-udeb-all.gz">Contents-udeb-all.gz</a>
        <a href="Contents-udeb-amd64.gz">Contents-udeb-amd64.gz</a>
        <a href="Contents-udeb-arm64.gz">Contents-udeb-arm64.gz</a>
        <a href="Contents-udeb-i386.gz">Contents-udeb-i386.gz</a>
        ...
    """
    contents_file_list = []
    for line in html.split("\r\n"):
        if line.startswith("<a href=\"Contents-"):
            filename = line[line.find("Contents-"):line.find(".gz")+3]
            architecture = filename[filename.rfind("-") + 1:filename.rfind(".gz")]
            url = f"{mirror_url}{filename}" if mirror_url.endswith("/") else f"{mirror_url}/{filename}"
            contents_file_list.append(dict(architecture=architecture, filename=filename, url=url))
    return contents_file_list
