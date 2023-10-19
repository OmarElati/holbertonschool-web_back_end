#!/usr/bin/evn python3
""" Parameterize and patch as decorators """
from client import GithubOrgClient
from unittest import TestCase, mock
from unittest.mock import patch, Mock
from parameterized import parameterized


class TestGithubOrgClient(TestCase):
    """ testing GithubOrgClient """

    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_json):
        """ Test method returns correct output """
        client = GithubOrgClient(org_name)
        client.org()
        mock_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
            )
