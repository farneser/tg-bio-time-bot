from telethon.tl.functions.account import UpdateProfileRequest
from telethon import TelegramClient
import asyncio
from datetime import datetime, timedelta
from telethon import errors

api_id = 123456
api_hash = 'abcdefg12345'

client = TelegramClient('bio', api_id, api_hash)


async def main():
    prev_minute = None
    print("Program started...")

    while True:
        current_time = (datetime.now() + timedelta(hours=1)).strftime("%H:%M")

        if current_time != prev_minute:
            prev_minute = current_time
            try:
                await client(UpdateProfileRequest(
                    about=f'my local time is {current_time} (utc+3)'
                ))

                print(f"Bio updated at {current_time}")
            except errors.FloodWaitError as e:
                print(f"FloodWaitError, waiting for {e.seconds} seconds")
                await asyncio.sleep(e.seconds)

        else:
            print(f"bio already up-to-date at {current_time}, waiting...")

            await asyncio.sleep(1)


print("Connecting to client...")
with client:
    print("Connected successfully!")
    print("Starting main loop...")
    client.loop.run_until_complete(main())
