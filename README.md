![Python 3.5](https://img.shields.io/badge/python-3.5-blue.svg) ![License](https://img.shields.io/github/license/mashape/apistatus.svg)
# python-telegram-bot
Telegram Bot written in Python


# Getting started

First download the source with:

    $ git clone https://github.com/BotDevGroup/python-telegram-bot

You can install this bot with:

    $ python setup.py develop
    
    
To start the bot:

    $ ./marvind start
    
To stop the bot:

    $ ./marvind stop
    
To tail the logs:

    $ ./marvind celery_log

If you want a shell and a great debugger:
    
    $ pip install ipython ipdb
    $ ./marvind shell


How to setup your Bot

1. Go ahead and talk to [@BotFather](https://telegram.me/BotFather) to generate your bot token.
2. Now that you have your token already generated go to settings.json and now add your token to "telegram_token": "Your Token Goes Here"
3. Make shure you have rabbitmq and memcached installed in your system. 
4. Go to the directory of the bot in your terminal and type ./marvind start the bot will be started, you'll know because the message "OK". 
5. Now go to your bot and say '/hello' to your bot :)




Other references:
- [Telegram API documentation](https://core.telegram.org/bots/api)
- [python-telegram-bot documentation](https://pythonhosted.org/python-telegram-bot/)


# Contributing

Contributions of all sizes are welcome. Please review our [contribution guidelines](https://github.com/BotDevGroup/python-telegram-bot/blob/master/CONTRIBUTING.md) to get started. You can also help by [reporting bugs](https://github.com/BotDevGroup/python-telegram-bot/issues/new).
