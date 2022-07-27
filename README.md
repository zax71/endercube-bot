# Endercube-bot

Endercube's custom Discord bot.

## Features

Current features:

* `/ping` - responds with pong to show bots online status
* `/timeout <user> <time> <reason>` times out a user

## Setup

A small amount of setup is required to use the bot, steps are described below

### Configuration

`config.yml`

```yml
bot_token: <Token to use the bot with>
guild_ID: <Server to register commands in>
```

### Modules

Required python modules, all can be installed with `pip install <name>`

* py-cord
* DateTime
* humanfriendly
* PyYAML
* termcolor
