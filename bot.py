import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

# файл config_reader.py можно взять из репозитория
# пример — в первой главе
from handlers import common, ordering_food


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )

    # Если не указать storage, то по умолчанию всё равно будет MemoryStorage
    # Но явное лучше неявного =]
    dp = Dispatcher(storage=MemoryStorage())
    bot = Bot(token="6692392922:AAETK8Zp5xafcOkRsFxGzM7NDkF2TetPfpo")

    dp.include_router(common.router)
    dp.include_router(ordering_food.router)
    # сюда импортируйте ваш собственный роутер для напитков

    await dp.start_polling(bot)
    
class MyGlobals(object):
     mylist = list()
     ac=""

if __name__ == '__main__':
    
    asyncio.run(main())