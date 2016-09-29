![Python 3.5](https://img.shields.io/badge/python-3.5-blue.svg) ![License](https://img.shields.io/github/license/mashape/apistatus.svg)
# Marvin
Telegram Bot written in Python

# Requirements

- [Python 3.5](https://www.python.org/downloads/release/python-352/)
- [RabbitMQ](https://www.rabbitmq.com/download.html)
- Memcached ([Windows](https://commaster.net/content/installing-memcached-windows)/[Ubuntu](https://memcached.org/downloads))
- [MySQL](http://dev.mysql.com/downloads/)/[MariaDB](https://downloads.mariadb.org/)

# Getting started

Download the source with:

    $ git clone git@github.com:BotDevGroup/marvin.git

Install the bot with:

    $ python setup.py develop
    
Copy `default_settings.json` and rename it to `settings.json` (Open `settings.json` to customize it).
Remember to set your Telegram bot token on `telegram_token`, as well as the urls for memcached/rabbitmq.
This is also a good time to add any plugins.

    $ cp default_settings.json settings.json
    
To start the bot:

    $ ./marvind start
    
To stop the bot:

    $ ./marvind stop
    
To tail the logs:

    $ ./marvind celery_log

If you want a shell and a great debugger:
    
    $ pip install ipython ipdb
    $ ./marvind shell


####How to setup your Bot

1. Go ahead and talk to [@BotFather](https://telegram.me/BotFather) to generate your bot token key.
2. Now that you have your token already generated go to settings.json and add your token to `"telegram_token": "Your Token Goes Here"`
3. Make sure you have rabbitmq and memcached installed in your system. 
4. Go to the directory of the bot in your terminal and type `./marvind start`, once the bot has started, you'll see a message saying "OK". 
5. Now open Telegram, go to your bot and say '/hello' :)




Other references:
- [Telegram API documentation](https://core.telegram.org/bots/api)
- [python-telegram-bot documentation](https://pythonhosted.org/python-telegram-bot/)


# Contributing

Contributions of all sizes are welcome. Please review our [contribution guidelines](https://github.com/BotDevGroup/python-telegram-bot/blob/master/CONTRIBUTING.md) to get started. You can also help by [reporting bugs](https://github.com/BotDevGroup/python-telegram-bot/issues/new).
