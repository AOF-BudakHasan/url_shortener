#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="url-shortener",
    version="0.0.6",
    author="Hasan Budak",
    author_email="budak.hasan.apc@gmail.com",
    description="Get shorted url from a long url string.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AOF-BudakHasan/url_shortener",
    packages=setuptools.find_packages(exclude=['tests', 'test.*']),
    package_dir={"url_shortener": "url_shortener"},
    python_requires='>=3.0',
    test_suite='tests',
    setup_requires=['wheel'],
    install_requires=[
        'requests>=2.0',
    ],
    include_package_data=True,
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.0",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)
