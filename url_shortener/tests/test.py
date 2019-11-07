import os
import io
import unittest
from unittest.mock import patch

from .. import (
    UrlShorter, 
    BitLinkUrlShorter, 
    GoogleUrlShorter
)
from ..Interfaces import (
    InterfaceUrlShorter, 
    InterfaceUrlShortenerAdapter
)
from .mocks.url_shortener_mocks import (
    success_mock_google_adapter,
    failed_mock_google_adapter,
    success_mock_bitlink_adapter,
    failed_mock_bitlink_adapter
)

config = dict(
    GOOGLE_API_KEY='GOOGLE_API_KEY',
    BITLINK_ACCESS_TOKEN='BITLINK_ACCESS_TOKEN'
)


class UrlShortenerTests(unittest.TestCase):
    """Test cases of UrlShortener
    """
    user_email = 'urlshortener@domain.com'
    user_pass = 'TestPassword'
    long_url = 'http://mylongurl.me'

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @patch('requests.post', side_effect=success_mock_google_adapter)
    def test_google_adapter(self, mock_post):
        google_api_key = config.get('GOOGLE_API_KEY', 'defaultGoogleApiKey')
        adapter_google = GoogleUrlShorter(google_api_key=google_api_key)
        self.assertIsInstance(adapter_google, InterfaceUrlShorter,
                              'GoogleUrlShorter should be an instance of InterfaceUrlShorter')
        self.assertIsInstance(adapter_google, InterfaceUrlShortenerAdapter,
                              'GoogleUrlShorter should be an instance of InterfaceUrlShortenerAdapter')
        self.assertEqual(adapter_google.google_api_key, google_api_key)
        self.assertRegex(adapter_google.api_path, 'key={}$'.format(google_api_key),
                         'Property `api_path` string must contains the `google_api_key` value ')
        result = adapter_google.get_short_url(long_url=UrlShortenerTests.long_url)
        self.assertIsInstance(result, tuple)
        response_dict, status_code = result
        self.assertEqual(status_code, 201, 'Response status code should be 201')
        self.assertIsInstance(response_dict, dict)
        self.assertRegex(response_dict['id'], '(^http(.)?://goo.gl)')

    @patch('requests.post', side_effect=failed_mock_google_adapter)
    def test_failed_google_adapter(self, mock_post):
        google_api_key = config.get('GOOGLE_API_KEY', 'defaultGoogleApiKey')
        result = GoogleUrlShorter(google_api_key=google_api_key).get_short_url(long_url=UrlShortenerTests.long_url)
        self.assertIsInstance(result, tuple)
        response_dict, status_code = result
        self.assertGreater(status_code, 201, 'Response status code should be greater than 201')
        self.assertIsInstance(response_dict, dict)
        self.assertIsInstance(response_dict['message'], str)
        self.assertIsInstance(response_dict['errors'], list)
        self.assertIsInstance(response_dict['status_code'], int)
        self.assertIsInstance(response_dict['description'], str)

    @patch('requests.post', side_effect=success_mock_bitlink_adapter)
    def test_bitlink_adapter(self, mock_post):
        bitlink_access_token = config.get('BITLINK_ACCESS_TOKEN', 'defaultBitlinkAccessToken')
        adapter_bitlink = BitLinkUrlShorter(access_token=bitlink_access_token)
        self.assertIsInstance(adapter_bitlink, InterfaceUrlShorter,
                              'BitLinkUrlShorter should be an instance of InterfaceUrlShorter')
        self.assertIsInstance(adapter_bitlink, InterfaceUrlShortenerAdapter,
                              'BitLinkUrlShorter should be an instance of InterfaceUrlShortenerAdapter')
        self.assertEqual(adapter_bitlink.access_token, bitlink_access_token)
        self.assertEqual(adapter_bitlink.authorization, 'Bearer {}'.format(bitlink_access_token),
                         'Property `_authorization` string must contains the `bitlink_access_token` value ')
        result = adapter_bitlink.get_short_url(long_url=UrlShortenerTests.long_url)
        self.assertIsInstance(result, tuple)
        response_dict, status_code = result
        self.assertEqual(status_code, 201, 'Response status code should be 201')
        self.assertIsInstance(response_dict, dict)
        self.assertRegex(response_dict['id'], '(^http(.)?://bit.ly)')

    @patch('requests.post', side_effect=failed_mock_bitlink_adapter)
    def test_failed_bitlink_adapter(self, mock_post):
        bitlink_access_token = config.get('BITLINK_ACCESS_TOKEN', 'defaultBitlinkAccessToken')
        result = BitLinkUrlShorter(access_token=bitlink_access_token).get_short_url(long_url=UrlShortenerTests.long_url)
        self.assertIsInstance(result, tuple)
        response_dict, status_code = result
        self.assertGreater(status_code, 201, 'Response status code should be greater than 201')
        self.assertIsInstance(response_dict, dict)
        self.assertIsInstance(response_dict['message'], str)
        self.assertIsInstance(response_dict['errors'], list)
        self.assertIsInstance(response_dict['status_code'], int)
        self.assertIsInstance(response_dict['description'], str)

    @patch('requests.post', side_effect=success_mock_google_adapter)
    def test_url_shorter_with_google_adapter(self, mock_post):
        google_api_key = config.get('GOOGLE_API_KEY', 'defaultGoogleApiKey')
        url_shorter_with_google = UrlShorter(GoogleUrlShorter(google_api_key))
        self.assertIsInstance(url_shorter_with_google, InterfaceUrlShorter)
        response, status_code = url_shorter_with_google.get_short_url(UrlShortenerTests.long_url)
        self.assertEqual(status_code, 201)
        self.assertRegex(response['id'], '(^http(.)?://goo.gl)')

    @patch('requests.post', side_effect=success_mock_bitlink_adapter)
    def test_url_shorter_with_bitlink_adapter(self, mock_post):
        bitlink_access_token = config.get('BITLINK_ACCESS_TOKEN', 'defaultBitlinkAccessToken')
        url_shorter_with_bitlink = UrlShorter(BitLinkUrlShorter(bitlink_access_token))
        self.assertIsInstance(url_shorter_with_bitlink, InterfaceUrlShorter)
        response, status_code = url_shorter_with_bitlink.get_short_url(UrlShortenerTests.long_url)
        self.assertEqual(status_code, 201)
        self.assertRegex(response['id'], '(^http(.)?://bit.ly)')


if __name__ == '__main__':
    unittest.main()
