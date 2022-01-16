## `token`

A string containing a discord token, if you don't have one or don't know how to find it [this guide from discord-irc can help you](https://github.com/reactiflux/discord-irc/wiki/Creating-a-discord-bot-&-getting-a-token)

e.g
```json
"token": "Mzc4NzIxNjAxMjIwMzMxMTcw.HstE0T.jhqBRYy10FN3iwdsOXtLkeoKCrD"
```

!!! Note

    This is not a real token, just an example of how one might look.


## `prefix`

A string that contains the prefix before the command, for example

```json
"prefix": "g!"
```

will require that `g!` comes before every command, e.g `g!userinfo <username>`


## `status_channel`

!!! note

    If you don't know how to find your channel id then
    [Discord has a good support article on it](https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID-)

This is a integer that contains a discord channel id where the message will be sent
when the bot goes online, this will no longer be required soon but if you don't
want it for obvious reasons you can remove it from the code manually.

example

```json
"status_channel": 821457809722834985
```
