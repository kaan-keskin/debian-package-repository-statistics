#!/usr/bin/env python3

from pkg.main.default_variables import DEFAULT_ARCHITECTURE, DEFAULT_MIRROR_URL, DEFAULT_INCLUDE_UDEB
from pkg.main.get_contents_file_list import get_contents_file_list


def get_contents_file_url(architecture: str = DEFAULT_ARCHITECTURE,
                          mirror_url: str = DEFAULT_MIRROR_URL,
                          include_udeb: bool = DEFAULT_INCLUDE_UDEB) -> list:
    """
    Gets the URL(s) of the Contents-* file for the given architecture.
    If the architecture is None it returns all the content indices.

    Arguments:
        architecture: CPU Architecture for the Debian Contents-*.gz file.
        mirror_url: Debian Package Repository Address
        include_udeb: Debian Contents-*.gz file URL

    Returns:
        list: list of URL(s) with the following structure:
        [ "http://ftp.uk.debian.org/debian/dists/stable/main/Contents-amd64.gz" ]
    """
    contents_file_list = get_contents_file_list(mirror_url)
    contents_file_url = []
    for element in contents_file_list:
        element_architecture = element["architecture"]
        element_filename = element["filename"]
        element_url = element["url"]
        is_udeb = element_filename.endswith(f"udeb-{element_architecture}.gz")
        if architecture == element_architecture:
            if is_udeb:
                if include_udeb:
                    contents_file_url.append(element_url)
            else:
                contents_file_url.append(element_url)
    return contents_file_url
