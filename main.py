import asyncio
from telethon import TelegramClient

API_ID = 2040
API_HASH = "b18441a1ff607e10a989891a5462e627"
SESSION_NAME = "railway_session"
PROXY = None


async def main():
    client = TelegramClient(SESSION_NAME, API_ID, API_HASH, proxy=PROXY)
    try:
        await client.start()
        me = await client.get_me()
        print(f"OK logged in as {me.id} ({me.phone})", flush=True)
    except Exception as e:
        print(f"NOT_LOGGED: {type(e).__name__}: {e}", flush=True)

    while True:
        try:
            me = await client.get_me()
            print(".", flush=True)
        except Exception as e:
            print(f"ERR: {type(e).__name__}: {e}", flush=True)
        await asyncio.sleep(60)


asyncio.run(main())