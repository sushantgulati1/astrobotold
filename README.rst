Telegram Astro Mystery Bot
===========================
Telegram bot that sends daily horoscope updates from several popular websites and asks for feedback regarding correctness of the prediction.

Disclaimer
----------
We don't take horoscopes seriously. This is an experiment.

Usage
-----
| Find this bot on Telegram, at https://t.me/astro_mystery_bot
| Start with the commands listed below.

Setup (for development)
-----------------------
| Get a new bot by talking to the BotFather bot in Telegram.
| Clone the repo inside a virtual env.
| Make sure redis-server is up and running.
| Run these in a terminal

- ``pip install -e .``
- ``export first_bot_token='the_api_token_you_got_from_the_botfather'``
- ``astro_bot``

Telegram Bot Commands
---------------------
| ``/start`` - start the bot
| ``/stop`` - stop the bot
| ``/set zodiac`` - subscribe to daily updates of a zodiac sign
| ``/reset`` - unsubscribe to daily updates
| ``/help`` - print complete help and about message

Contributors
------------
| Ramit Mittal - https://ramitmittal.com - https://github.com/ramitmittal
| Sushant Gulati - https://github.com/sushantgulati1

How to Contribute
-----------------
| Contributions are welcome, specially new-comers.
| You don't just have to write code. You can help out by writing documentation, tests, or even by giving feedback about this work.
| Email at ``ramitmittal.k@gmail.com`` or start a pull request or file an issue.

Meta
----
| Built in India, with love, using Telepot.
| Distributed under GNU GPLv3. See ``LICENSE`` for more information.
