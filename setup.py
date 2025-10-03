# -*- coding: utf-8 -*-
# Imports ###########################################################

import os
from setuptools import setup


# Main ##############################################################

setup(
    name='epec_oauth_login',
    version='1.0',
    description='EPEC backend Oauth 2.0',
    packages=['epec_oauth_login'],
    install_requires=[
        'Django',
    ],
)
