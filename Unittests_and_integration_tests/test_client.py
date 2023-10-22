#!/usr/bin/env python3
""" Now we will test the clients.py file """
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from parameterized import parameterized, parameterized_class
from requests import Response
from unittest.mock import Mock, PropertyMock, patch
import unittest


class TestGithubOrgClient(unittest.TestCase):
    """ New class for testing GithubOrgClient """

    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    def test_org(self, org_name):
        """ Test func for .org """
        with patch('client.GithubOrgClient.org') as m_org:
            client = GithubOrgClient(org_name)
            self.assertEqual(client.org.return_value, m_org.return_value)

    def test_public_repos_url(self):
        """ Another test """
        with patch('client.GithubOrgClient.org', new_callable=PropertyMock)\
                as m_org:
            m_org.return_value = {"repos_url": True}
            client = GithubOrgClient("org_name")
            self.assertEqual(client._public_repos_url, True)

    @patch('client.get_json')
    def test_public_repos(self, mock_json):
        """ Method to test client.GithubOrgClient.public_repos """
        with patch('client.GithubOrgClient.public_repos',
                   new_callable=PropertyMock) as m_prop:
            mock_json.return_value = {'repos_url': 'www.randomgenerator.com'}
            client = GithubOrgClient('randomgenerator')
            m_prop.return_value = client.org.get('repos_url')
            self.assertEqual(client.public_repos, 'www.randomgenerator.com')
            m_prop.assert_called_once()
            mock_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """ Method in order to unit-test GithubOrgClient.has_license """
        The_test = GithubOrgClient('org_name')
        self.assertEqual(The_test.has_license(repo, license_key), expected)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ Integration test; inmplementing two methods """

    def setUpClass():
        """ Setup Class; mock requests.get to return example payloads """

    def tearDownClass():
        """ Teardown Class to stop the patcher """
