#!/usr/bin/env python3

import unittest

from dprs.default_variables import DEFAULT_MIRROR_URL
from dprs.get_contents_file_url import get_contents_file_url


class TestGetContentsFileURL(unittest.TestCase):
    """
    Test case get_contents_file_url() method.
    """

    def setUp(self) -> None:
        self.architecture = "amd64"
        self.mirror_url = DEFAULT_MIRROR_URL

    def test_get_contents_file_url(self):
        """
        Test the application it can get the Contents-*.gz file url
        for given architecture and check UDEB files are needed.
        """

        urls = get_contents_file_url(mirror_url=self.mirror_url, architecture=self.architecture)

        self.assertIsInstance(
            urls, list,
            "Output typr of the function was expected to be a list.")

        self.assertEqual(
            len(urls), 1,
            "Only one url is expected when udeb isn't requested.")

        self.assertTrue(urls[0].endswith(
            f"{self.architecture}.gz"),
            "Output URL should end with the `architecture`.gz .")

        self.assertFalse(
            "udeb" in urls[0],
            "URL should not contain the udeb link when it is not requested.")

    def test_get_contents_file_url_with_udeb(self):
        """
        Test the application can get the Contents-*.gz file url
        for both the base architecture contents file as well as the udeb file
        """

        urls = get_contents_file_url(mirror_url=self.mirror_url, architecture=self.architecture, include_udeb=True)

        self.assertIsInstance(
            urls, list,
            "When the UDEB is requested, the output is a list.")

        found_udeb = False
        for url in urls:
            self.assertTrue(url.endswith(
                f"{self.architecture}.gz"), "URL should end with `architecture`.gz .")
            if not found_udeb:
                found_udeb = url.endswith(f"udeb-{self.architecture}.gz")

        self.assertTrue(found_udeb,
            "UDEB file URL was not returned.")
