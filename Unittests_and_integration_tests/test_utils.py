import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient  # Import the GithubOrgClient class from your client file

class TestGithubOrgClient(unittest.TestCase):
    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json', return_value={"org_name": "dummy_org"})
    def test_org(self, org_name, mock_get_json):
        client = GithubOrgClient(org_name)
        result = client.org()

        mock_get_json.assert_called_once_with(GithubOrgClient.ORG_URL.format(org=org_name))
        self.assertEqual(result, {"org_name": "dummy_org"})
