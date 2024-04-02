from telethon.tl.functions.account import UpdateProfileRequest
from telethon import TelegramClient
from datetime import datetime
from telethon import errors
import asyncio
import pytz
import os
import sys

api_id = int(os.environ["API_ID"])
api_hash = os.environ["API_HASH"]

timezone = pytz.timezone(os.environ.get("TIME_ZONE", "Europe/Minsk"))
pattern = os.environ.get("BIO_PATTERN", "my local time is {TIME}")

client = TelegramClient('bio', api_id, api_hash)


def get_text(time: str) -> str:
    return pattern.replace("{TIME}", time)


async def main():
    prev_minute = None
    print("Program started...")

    while True:
        current_time = (datetime.now(timezone)).strftime("%H:%M")

        if current_time != prev_minute:
            prev_minute = current_time
            try:
                await client(UpdateProfileRequest(
                    about=get_text(current_time)
                ))

                print(f"Bio updated at {current_time}")
            except errors.FloodWaitError as e:
                print(f"FloodWaitError, waiting for {e.seconds} seconds")
                await asyncio.sleep(e.seconds)

        else:
            print(f"bio already up-to-date at {current_time}, waiting...")

            await asyncio.sleep(1)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "--session":
            client.start()
    else:
        print("Connecting to client...")
        with client:
            print("Connected successfully!")
            print("Starting main loop...")
            client.loop.run_until_complete(main())
