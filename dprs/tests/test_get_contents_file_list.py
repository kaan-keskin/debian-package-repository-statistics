#!/usr/bin/env python3

import unittest

from dprs.default_variables import DEFAULT_MIRROR_URL
from dprs.get_contents_file_list import get_contents_file_list


class TestGetContentsFileList(unittest.TestCase):
    """
    Test case get_contents_file_list() method.
    """

    def setUp(self) -> None:
        self.architecture = "amd64"
        self.mirror_url = DEFAULT_MIRROR_URL

    def test_lists_architectures(self):
        """
        Test the application it can list the architectures
        in the provided Debian Package Repository.
        """

        result = get_contents_file_list(self.mirror_url)

        self.assertTrue(
            result is not None,
            "The function returned a None value where a non-empty list was expected.")

        self.assertTrue(
            isinstance(result, list),
            "The function failed to return a list.")

        self.assertTrue(
            len(result) > 0,
            "An empty list was returned. Either the code is broken, or the url has no Content Indices!")

        result_contains_dicts = all(isinstance(item, dict) for item in result)
        self.assertTrue(
            result_contains_dicts,
            "Each item in the result should be a dictionary.")

        result_contains_keys = all("filename" in item.keys() and "url" in item.keys() for item in result)
        self.assertTrue(
            result_contains_keys,
            "Each item in the result should contain a filename and a url value.")
