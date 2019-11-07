#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod


class InterfaceUrlShorter(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_short_url(self, long_url):
        """
        Get short url from long_url
        :param {!str} long_url: Your long url
        :return {str}: Short url
        """
        pass


class InterfaceUrlShortenerAdapter(InterfaceUrlShorter):
    __metaclass__ = ABCMeta

    @abstractmethod
    def do_shorter_request(self, long_url):
        """
        Make shorter request
        :param {!str} long_url: Your long url
        :return {Response}: HttpResponse
        """
        pass

    @abstractmethod
    def handle_shorter_response(self, response):
        """
        `self.do_shorter_request` response handler
        :param {HttpResponse} response:
        :return: {tuple}: (dict, int)
        if its successful then:
            `dict` value will contains `id` key
            and `int` value will equals `201`
        else:
            `dict` will be descripted in `handle_shortener_error_response` check it out,
            and `int` value will be greater than 201
        """
        pass

    @abstractmethod
    def handle_shortener_error_response(self, response):
        """
        If `self.do_shorter_request` returned with errors then prepare a standard error dict
        :param response: Should be an HttpResponse
        :return: dict(
            message='ERROR_MESSAGE_TITLE'
            description='ERROR_MESSAGE_DESCRIPTION'
            errors=[{},{}],
            status_code=400 # response.status_code
        )
        """
        pass

    @property
    @abstractmethod
    def api_path(self):
        pass

    @api_path.setter
    @abstractmethod
    def api_path(self, value):
        pass
