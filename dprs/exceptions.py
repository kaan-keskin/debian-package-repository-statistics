#!/usr/bin/env python3


class ArchitectureNotFound(Exception):
    """
    Raised when a user requests a Contents-*.gz file for an unknown architecture.
    """
    # TODO: Add more functionality. Doing nothing for now!


class MirrorURLNotAccessible(Exception):
    """
    Raised when Debian Package Repository URL is not accessible.
    """
    # TODO: Add more functionality. Doing nothing for now!


class ContentsFileURLNotFound(Exception):
    """
    Raised when Contents-*.gz file URL is not found.
    """
    # TODO: Add more functionality. Doing nothing for now!
