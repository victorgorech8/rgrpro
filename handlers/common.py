from aiogram import F, Router
from aiogram.filters import Command
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.types import FSInputFile, URLInputFile, BufferedInputFile

router = Router()


@router.message(Command(commands=["start"]))
async def cmd_start(message: Message, state: FSMContext):
    
    await state.clear()
    await message.answer(
        text="Мы начинаем протоинженеринг твоей будущей профессии. Просто положить свои пальцы на ЛКМ и ПКM. Жми (/test) ",
     )
    image_from_pc = FSInputFile("meme.jpg")
    result = await message.answer_photo(
        image_from_pc,
     )


