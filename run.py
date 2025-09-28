import os
import asyncio
from aiogram import Bot, Dispatcher

from dotenv import load_dotenv
from app.handlers import router


async def main():
    load_dotenv()
    bot = Bot(token=os.getenv("BOT_TOKEN"))
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        print("Bot started!")
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot stopped!")