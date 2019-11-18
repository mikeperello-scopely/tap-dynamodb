#!/usr/bin/env python
from setuptools import setup

setup(
    name="tap-dynamodb",
    version="0.0.0",
    description="Singer.io tap for extracting data",
    author="Stitch",
    url="http://singer.io",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    py_modules=["tap_dynamodb"],
    install_requires=[
        'boto3==1.9.57',
        "singer-python==5.9.0",
        'terminaltables==3.1.0',
        'backoff==1.8.0',
    ],
    extras_require={
        'dev': [
            'ipdb',
            'pylint',
            'nose'
        ]
    },
    entry_points="""
    [console_scripts]
    tap-dynamodb=tap_dynamodb:main
    """,
    packages=["tap_dynamodb"],
    package_data = {},
    include_package_data=True,
)