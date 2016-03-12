# ezzybot [![Codacy Badge](https://api.codacy.com/project/badge/grade/6f9c84a479754bbb945d6ac4cf4cdbb1)](https://www.codacy.com/app/me_64/ezzybot)

EzzyBot is a IRC bot framework built in python.

Example of use:

```
import ezzybot

mybot = ezzybot.bot()

def hello(info=None, conn=None):
    return "Hello!"

mybot.assign(function=hello, help_text="Returns 'Hello!'", commandname="hello")
mybot.run({"channels":["#ezzybot"], "host": "irc.freenode.net", "port": 6697, "ssl": True, "nick": "EzzyBot"})
```



Devs are: zz, Bowserinator, BWBellairs

Wanna know more? (IRC) Freenode: #ezzybot
[![Visit our IRC Chat!](https://kiwiirc.com/buttons/chat.freenode.net/ezzybot.png)](https://kiwiirc.com/client/chat.freenode.net/?nick=ezzy|?&theme=cli#ezzybot)