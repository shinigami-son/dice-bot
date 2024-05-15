# dice-bot

### Description:

Telegram bot for making dice rolls and searching for information on TTRPG "World of Darkness"

A fairly simple bot that I wrote to study the aiogram library. In the future I plan to expand a number of functions and fully use it.

[Link to the bot](https://t.me/dicerpgbot)

The bot is not active at the moment!


### Commands:

/roll и /r - for dice rolling without reference to any edition (without doubling tens or second throws thereof)

/roll3r и /r3r - for dice rolling according to the rules of Revised Edition (with doubling tens);

/roll4r и /r4r - for dice rolling according to the rules of 20th Edition (with doubling ten);

/search - for search for information. The bot first looks for a specific article on the [Мир Тьмы вики](https://wod.fandom.com/ru/wiki/), if there are no results, then search for similar ones, if there are nothing, then search in Google;

/help и /donate - for information about the bot and the opportunity to thank the author.

All commands for throwing dices require three parameters: the number of dices, the edge and the difficulty of the throw. If there is no need to constantly specify the edge, then you can correct the code so that this parameter is equal to 10 by default.
