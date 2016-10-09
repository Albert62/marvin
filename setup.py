#!/usr/bin/env python

from distutils.core import setup
from setuptools import find_packages


REQUIREMENTS = [
    'python-telegram-bot==5.1.0',
    'blinker',
    'python-dateutil',
    'dogpile.cache==0.6.2',
    'mongoengine==0.10.6',
    'polling',
    'pytz',
    'ipython',
    'ipdb',
    'requests'
]


setup(name='marvinbot',
      version='0.3',
      description='Super Duper Telegram Bot - MK. III',
      author='BotDevGroup',
      author_email='',
      packages=find_packages(),
      zip_safe=False,
      include_package_data=True,
      package_data={'': ['*.ini']},
      # namespace_packages=["telegrambot",],
      install_requires=REQUIREMENTS,
      dependency_links=[

      ],)
