#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from ..Interfaces import InterfaceUrlShortenerAdapter


class BitLinkUrlShorter(InterfaceUrlShortenerAdapter):
    access_token_assert_error = "Parameter `access_token` is required as a string, but you gived `{}`"
    endpoints = dict(
        SHORTEN='shorten'
    )

    def __init__(self, access_token=None, referrer=None):
        """(!string, ?string) -> instance

        Short your long urls by Bitlinks

        :param access_token: Bitlink api access_token
        :param referrer: Headers param
        """
        self.api_path = ''
        self.authorization = ''
        self.referrer = referrer
        self.access_token = access_token

    def get_short_url(self, long_url):
        """
        (string) -> dict
        :param long_url: Long url which is 
        :return: dict
        """
        return self.handle_shorter_response(self.do_shorter_request(long_url))

    def do_shorter_request(self, long_url):
        api_url = self.api_path.format(endpoint=BitLinkUrlShorter.endpoints.get('SHORTEN'))
        post_body = dict(long_url=long_url)
        post_headers = {
            'Content-Type': 'application/json',
            'Authorization': self.authorization
        }
        if self.referrer:
            post_headers['referrer'] = self.referrer
        return requests.post(api_url, json=post_body, headers=post_headers)

    def handle_shorter_response(self, response):
        json_response = response.json()
        if response.status_code in [200, 201]:
            return dict(id=json_response['id']), 201
        return self.handle_shortener_error_response(response), response.status_code

    def handle_shortener_error_response(self, response):
        json_response = response.json()
        return dict(
            message=json_response['message'] if 'message' in json_response else '',
            description=json_response['description'] if 'description' in json_response else '',
            errors=json_response['errors'] if 'errors' in json_response else [],
            status_code=response.status_code
        )

    @property
    def api_path(self):
        return self.__api_path

    @api_path.setter
    def api_path(self, api_path):
        self.__api_path = 'https://api-ssl.bitly.com/v4/{endpoint}'

    @property
    def access_token(self):
        return self.__access_token

    @access_token.setter
    def access_token(self, access_token):
        assert isinstance(access_token, str), BitLinkUrlShorter.access_token_assert_error.format(type(access_token))
        self.__access_token = access_token
        self.authorization = 'Bearer {ACCESS_TOKEN}'.format(ACCESS_TOKEN=access_token)
