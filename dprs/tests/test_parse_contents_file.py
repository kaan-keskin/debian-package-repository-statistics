#!/usr/bin/env python3

import tempfile
import unittest

from dprs.default_variables import DEFAULT_MIRROR_URL
from dprs.download_contents_file import download_contents_file
from dprs.get_contents_file_url import get_contents_file_url
from dprs.parse_contents_file import parse_contents_file


class TestDownloadContentsFile(unittest.TestCase):
    """
    Test case parse_contents_file() method.
    """

    def setUp(self) -> None:
        self.architecture = "amd64"
        self.mirror_url = DEFAULT_MIRROR_URL

    def test_gets_package_data_from_contents(self):
        """
        Test the application it can get the package data from a Contents-*.gz file.
        Test the application when the UDEB files are added, the package gets extended.
        """

        urls = get_contents_file_url(architecture=self.architecture, mirror_url=self.mirror_url, include_udeb=True)

        with tempfile.TemporaryDirectory() as temp_directory:
            # Merge UDEB and DEB information, if required.
            complete_package_data = {}
            total_keys = 0
            for url in urls:
                contents_file = download_contents_file(contents_file_url=url, output_dir=temp_directory)
                package_dict = parse_contents_file(contents_file=contents_file)

                self.assertIsInstance(
                    package_dict, dict,
                    "Type of package metadata should be a dictionary.")

                self.assertTrue(
                    len(package_dict.keys()) > 0,
                    "Package list is not empty.")

                complete_package_data.update(**package_dict)
                total_keys += len(package_dict)

            self.assertEqual(
                total_keys, len(complete_package_data),
                "The two package files were not added together.")
