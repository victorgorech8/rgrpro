import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage


from handlers import common, testsetf


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )

   
    dp = Dispatcher(storage=MemoryStorage())
    bot = Bot(token="6692392922:AAETK8Zp5xafcOkRsFxGzM7NDkF2TetPfpo")

    dp.include_router(common.router)
    dp.include_router(testsetf.router)
   
    await dp.start_polling(bot)
    
class MyGlobals(object):
     mylist = list()
     ac=""

if __name__ == '__main__':
    
    asyncio.run(main())
