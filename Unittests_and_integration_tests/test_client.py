#!/usr/bin/env python3
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):

    @parameterized.expand([
        ("google", "https://api.github.com/orgs/google"),
        ("abc", "https://api.github.com/orgs/abc"),
    ])
    @patch('client.get_json', return_value={"name": "org_name"})
    def test_org(self, org_name, expected_url, mock_get_json):
        github_client = GithubOrgClient(org_name)
        org_data = github_client.org()

        self.assertEqual(org_data, {"name": "org_name"})
        mock_get_json.assert_called_once_with(expected_url)


if __name__ == '__main__':
    unittest.main()
