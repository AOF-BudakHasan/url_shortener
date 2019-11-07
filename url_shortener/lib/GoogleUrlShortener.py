#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from ..Interfaces import InterfaceUrlShortenerAdapter


class GoogleUrlShorter(InterfaceUrlShortenerAdapter):
    api_key_assert_error = "Parameter `google_api_key` is required as a string, but you gived `{}`"

    def __init__(self, google_api_key=None, referrer=None):
        self.google_api_key = google_api_key
        self.api_path = ''
        self.referrer = referrer

    def get_short_url(self, long_url):
        return self.handle_shorter_response(self.do_shorter_request(long_url))

    def do_shorter_request(self, long_url):
        post_body = dict(longUrl=long_url)
        post_headers = {'Content-Type': 'application/json'}
        if self.referrer:
            post_headers['referrer'] = self.referrer
        return requests.post(self.api_path, json=post_body, headers=post_headers)

    def handle_shorter_response(self, response):
        json_response = response.json()
        if response.status_code in [200, 201]:
            return dict(id=json_response['id']), 201
        return self.handle_shortener_error_response(response), response.status_code

    def handle_shortener_error_response(self, response):
        json_response = response.json()
        return dict(
            message=json_response['error']['message'],
            description='',
            errors=json_response['error']['errors'],
            status_code=response.status_code
        )

    @property
    def google_api_key(self):
        return self.__google_api_key

    @google_api_key.setter
    def google_api_key(self, google_api_key):
        assert isinstance(google_api_key, str), GoogleUrlShorter.api_key_assert_error.format(type(google_api_key))
        self.__google_api_key = google_api_key

    @property
    def api_path(self):
        return self.__api_path.format(key=self.google_api_key)

    @api_path.setter
    def api_path(self, api_path):
        self.__api_path = 'https://www.googleapis.com/urlshortener/v1/url?key={key}'
