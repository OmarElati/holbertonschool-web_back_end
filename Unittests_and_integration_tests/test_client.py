#!/usr/bin/env python3
import unittest
from unittest import mock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):

    @parameterized.expand([
        "google",
        "abc"
    ])
    @mock.patch.object(GithubOrgClient, "get_json")
    def test_org(self, org, get_json_mock):
        get_json_mock.return_value = {"name": org}
        client = GithubOrgClient()
        self.assertEqual(client.org(org), org)
        get_json_mock.assert_called_once_with(f"https://api.github.com/orgs/{org}")
