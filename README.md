# ezzybot [![Build Status](https://travis-ci.org/ezzybot/ezzybot.svg?branch=master)](https://travis-ci.org/ezzybot/ezzybot) [![Codacy Badge](https://api.codacy.com/project/badge/grade/6f9c84a479754bbb945d6ac4cf4cdbb1)](https://www.codacy.com/app/me_64/ezzybot) [![PyPI](https://img.shields.io/pypi/dm/ezzybot.svg)](https://pypi.python.org/pypi/ezzybot) [![Stories in Ready](https://badge.waffle.io/ezzybot/ezzybot.png?label=ready&title=Ready)](https://waffle.io/ezzybot/ezzybot)
EzzyBot is a IRC bot framework built in python.
```
from ezzybot import bot

mybot = bot()

config = {  
   "nick":"EzzyBot",
   "channels":["#ezzybot", "#ezzybot-debug", "#ezzybot-bots"],
   "port":6667,
   "SSL":False,
   "SASL":True,
   "do_auth": False,
   "auth_user": "ezzybot",
   "auth_pass": "<password>",
   "quit_message":"Default quit reason",
   "permissions": {
       "admin": ["*!ident@host"]
    },
    "log_channel": "#ezzybot-debug"
}

mybot.run(config)
```

Installation
```
sudo pip install ezzybot
```

Or, install the development version

```
sudo pip install git+https://github.com/ezzybot/ezzybot
```

#[Wiki](https://github.com/ezzybot/ezzybot/wiki)

Developer Links:
* [Travis](https://travis-ci.org/ezzybot/ezzybot)
* [Cloud9](https://ide.c9.io/itslukej/ezzybot)

Devs are:
* zz DOGE: DEzzyGgAyHwkAPbWTnyZFJQC19R1ZLUv3s
* BWBellairs
* IndigoTiger
Wiki team:
* iovoid DOGE: DBvRFywkgZ6EyCN6mWHv8ypeoDHaaxed5C
Wanna know more? (IRC) Freenode: #ezzybot

[![Visit our IRC Chat!](https://kiwiirc.com/buttons/chat.freenode.net/ezzybot.png)](https://kiwiirc.com/client/chat.freenode.net/?nick=ezzy|?&theme=cli#ezzybot)
