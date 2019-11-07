#!/usr/bin/env python
# -*- coding: utf-8 -*-


from .Interfaces import InterfaceUrlShorter

__all__ = ['UrlShorter']


class UrlShorter(InterfaceUrlShorter):
    """Get shorted url from a long url string

    @example: ```
    # Choose your adapter [GoogleUrlShorter, BitLinkUrlShorter]

    ===> Usage with `GoogleUrlShorter` adapter
    adapter_google = GoogleUrlShorter('YOUR_GOOGLE_API_KEY')
    shorted_url = UrlShorter(adapter_google).get_short_url('YOUR_LONG_URL_STRING')

    ===> Usage with `BitLinkUrlShorter` adapter
    adapter_bitlink = BitLinkUrlShorter('YOUR_BITLINK_ACCESS_TOKEN')
    shorted_url = UrlShorter(adapter_bitlink).get_short_url('YOUR_LONG_URL_STRING')

    Success response for all adapters will return as tuple
        ({'id': 'SHORTED_URL_STRING'}, 201)
    Error response for all adapters will return as tuple
        (dict(
            message='ERROR_MESSAGE_TITLE'
            description='ERROR_MESSAGE_DESCRIPTION'
            errors=[{},{}],
            status_code=400 # response.status_code
        ), status_code)
    ```
    """
    adapter_assert_error = "Parameter `adapter` must be an instance of InterfaceUrlShorter, but you gived `{}`"

    def __init__(self, adapter=None):
        self.adapter = adapter

    def get_short_url(self, long_url):
        return self.adapter.get_short_url(long_url)

    @property
    def adapter(self):
        return self.__adapter

    @adapter.setter
    def adapter(self, adapter):
        assert isinstance(adapter, InterfaceUrlShorter), UrlShorter.adapter_assert_error.format(type(adapter))
        self.__adapter = adapter
