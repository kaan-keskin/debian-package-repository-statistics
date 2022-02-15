#!/usr/bin/env python3

import pathlib
import tempfile
import unittest

from dprs.default_variables import DEFAULT_MIRROR_URL
from dprs.download_contents_file import download_contents_file
from dprs.get_contents_file_url import get_contents_file_url


class TestDownloadContentsFile(unittest.TestCase):
    """
    Test case download_contents_file() method.
    """

    def setUp(self) -> None:
        self.architecture = "amd64"
        self.mirror_url = DEFAULT_MIRROR_URL

    def test_download_contents_file(self):
        """
        Test the application it can download the right Contents-*.gz file
        for given architecture string.
        """

        urls = get_contents_file_url(architecture=self.architecture, mirror_url=self.mirror_url)

        with tempfile.TemporaryDirectory() as temp_directory:
            url = urls[0]
            download_contents_file(contents_file_url=url, output_dir=temp_directory)
            expected_file = pathlib.Path(temp_directory) / f"Contents-{self.architecture}"

            self.assertTrue(
                expected_file.exists(),
                "The requested contents index was not downloaded and unpacked.")

            self.assertTrue(
                expected_file.is_file(),
                "The requested Contents-*.gz file was not downloaded and/or unpacked to a file.")
