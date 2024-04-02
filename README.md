# Telegram bio time Bot

Telegram userbot based on 'telethon' library that change your bio every minute by pattern

## Install

Download repo

```bash
git clone https://github.com./farneser/tg-bio-time-bot
cd tg-bio-time-bot
```

Create telegram session by login to your telegram account using telethon login

```bash
./generate-session.sh
```

Run bot with docker-compose

```bash
docker-compose up -d --build
```

## Configuration

1. `TIME_ZONE` - your timezone like Europe/Minsk
2. `BIO_PATTERN` - pattern of your bio with `{TIME}` variable (example: "my local time is {TIME}")

