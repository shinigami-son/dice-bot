# dice-bot

Описание:

Телеграм-бот для совершения бросков дайсов и поиска информации по НРИ "Мир Тьмы"

Достаточно простенький бот, который я написала с целью изучения библиотеки aiogram. В будущем планирую расширить ряд функций и полноценно его использовать.


Список команд:

/roll и /r - для бросков кубов без привязки к редакциям (без удвоения десяток или повторых бросков таковых);

/roll3r и /r3r - для бросков кубов по редакции Revised Edition (с повторными бросками десяток);

/roll4r и /r4r - для бросков кубов по редакции 20th Edition (с удвоением десяток);

/search - для поиска информации. Бот сначала ищет конкретную статью на сайте "https://wod.fandom.com/ru/wiki/", если там нет результатов, то ищет похожие, если нет ничего, то ищет в гугле;

/help и /donate - для получения информации о боте и возможности отблагодарить автора.

Все команды для бросков дайсов запрашивают на ввод три параметра: количество дайсов, грань и сложность броска. Если нет нужды постоянно указывать грань, то можно подправить код, чтобы этот параметр по умолчанию был равен 10.

Description:

Telegram bot for making dice rolls and searching for information on TTRPG "World of Darkness"

A fairly simple bot that I wrote to study the aiogram library. In the future I plan to expand a number of functions and fully use it.

List of commands:

/roll и /r - for dice rolling without reference to any edition (without doubling tens or second throws thereof)

/roll3r и /r3r - for dice rolling according to the rules of Revised Edition (with doubling tens);

/roll4r и /r4r - for dice rolling according to the rules of 20th Edition (with doubling ten);

/search - for search for information. The bot first looks for a specific article on the site "https://wod.fandom.com/ru/wiki/", if there are no results, then search for similar ones, if there are nothing, then search in Google;

/help и /donate - for information about the bot and the opportunity to thank the author.

All commands for throwing dices require three parameters: the number of dices, the edge and the difficulty of the throw. If there is no need to constantly specify the edge, then you can correct the code so that this parameter is equal to 10 by default.
