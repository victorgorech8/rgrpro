from aiogram import Router, F,types
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.types import FSInputFile, URLInputFile, BufferedInputFile
from bot import MyGlobals
from PIL import Image, ImageFont, ImageDraw
router = Router()

# Эти значения далее будут подставляться в итоговый текст, отсюда
# такая на первый взгляд странная форма прилагательных
available_food_names = ["Суши", "Спагетти", "Хачапури"]
available_food_sizes = ["Маленькую", "Среднюю", "Большую"]


class teststate(StatesGroup):
    q1 = State()
    q2 = State()
    q3 = State()
    q4 = State()
    q5 = State()
    q6 = State()
    q7 = State()
    q8 = State()


@router.message(Command("test"))
async def qu1(message: Message, state: FSMContext):
    del MyGlobals.mylist[:]
    
    kb = [
        [
            types.KeyboardButton(text="да"),
            types.KeyboardButton(text="нет")
        ],
     ]
   
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Сделай выбор"
    )
    await message.answer("Вы готовы честно выполнять трудовые свои трудовый часы?(1/4)", reply_markup=keyboard)
    await state.set_state(teststate.q1)

# Этап выбора блюда #


@router.message(teststate.q1)
async def qu2(message: Message, state: FSMContext):
    
    if (message.text.lower()=="да"):
        MyGlobals.mylist.append(1)
    else:
        MyGlobals.mylist.append(0)
    kb = [
        [
            types.KeyboardButton(text="да"),
            types.KeyboardButton(text="нет")
        ],
     ]
   
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Сделай выбор"
    )
   
    await message.answer(
        text="Знаешь английский язык на высоком уровне?(2/4)",
        reply_markup=keyboard
    )
    await state.set_state(teststate.q2)

@router.message(teststate.q2)
async def qu3(message: Message, state: FSMContext):
    if (message.text.lower()=="да"):
        MyGlobals.mylist.append(1)
    else:
        MyGlobals.mylist.append(0)
    kb = [
        [
            types.KeyboardButton(text="да"),
            types.KeyboardButton(text="нет")
        ],
     ]
   
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Правильный выбор сделай,джедай"
    )
    
    await message.answer("Хорошо знаешь язык ООП (или изучаешь Python)?(3/4)", reply_markup=keyboard)
    await message.answer_photo(FSInputFile("meme(1).jpg"))
    await state.set_state(teststate.q3)

@router.message(teststate.q3)
async def qu4(message: Message, state: FSMContext):
    if (message.text.lower()=="да"):
        MyGlobals.mylist.append(1)
    else:
        MyGlobals.mylist.append(0)
    await message.answer("Напиши что тебе еще увлекает помимо этого.(4/4)")
    await state.set_state(teststate.q4)

@router.message(teststate.q4)
async def qu5(message: Message, state: FSMContext):
    MyGlobals.ac=message.text.lower()
    if (MyGlobals.mylist==[0,0,0]):
        await message.answer(f"Рекомендуем труболитейный завод №69 города Челябинска. А вообще стоит хотя бы начать трудиться. Потом можешь поискать на HeadHunter что-то связанное с {MyGlobals.ac}")
        img = Image.open("meme(2).jpg")
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("impact.ttf", 160)

        def drawTextWithOutline(text, x, y):
            draw.text((x-2, y-2), text,(0,0,0),font=font)
            draw.text((x+2, y-2), text,(0,0,0),font=font)
            draw.text((x+2, y+2), text,(0,0,0),font=font)
            draw.text((x-2, y+2), text,(0,0,0),font=font)
            draw.text((x, y), text, (255,255,255), font=font)
            return

        text =message.from_user.full_name
        
        drawTextWithOutline(text, img.width/2-250 , img.height*4/6)
        img.save("out.jpg")
        await message.answer_photo(FSInputFile("out.jpg"))

    kb = [
        [
            types.KeyboardButton(text="да"),
            types.KeyboardButton(text="нет")
        ],
     ]
   
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Жми <да>. Тебе- не сложно, нам-приятно"
    )
    if(MyGlobals.mylist==[0,1,1] or MyGlobals.mylist==[1,1,1] ):
        await message.answer(f" Поздравляю! Ты прошол школу молодого бойца от Дмитрий Глуховского: немецкое посольство в твоем городе уже печатает документы для твоего ПМЖ. ")
    if(MyGlobals.mylist==[0,1,1]  ):
        await message.answer(f"Но тебе стоит приложеить усилия для того, чтобы там остаться. Про свое хобби как {MyGlobals.ac} можешь забыть.")
    if(MyGlobals.mylist==[1,1,1]  ):
        await message.answer(f"Твое трудолюбие тебе сильно поможет. Там еще сильнее разовьешь свое увлечение как {MyGlobals.ac}.")
    if(MyGlobals.mylist==[1,0,0]  ):
        await message.answer(f"Сила есть, ma не надо (мем для физиков). Ваша профессия: грузчик")

    if (MyGlobals.mylist==[0,0,1]):
        await message.answer(f"Ты прав- Python это манна небесная. Твой выбор- фрилансить из Тайланда.")
    if (MyGlobals.mylist==[0,1,0]):
        await message.answer(f"У Вас высокие шансы стать иноагентом. Нельзя же знать только английский. Найдтие еще хобби и пройдите тест заново.")
    if (MyGlobals.mylist==[1,1,0]):
        await message.answer(f"Ваши большие физичесие спосбости и идельное знание языка говорит о многом: может Вам стоит задумать о трудосустройстве в ГРУ.")
    
    if (MyGlobals.mylist==[1,0,1]):
        await message.answer(f"Трудолюбие+Python=TeamLead (зарплата 500к/наносек). Быстрее бегите в офис болььшй IT-компании")
    
    await message.answer(f"Елси понравилась наша глубокая налатика, то советуем подписаться на нашу рассылку",reply_markup=keyboard)
    await state.set_state(teststate.q5)

    
@router.message(teststate.q5)
async def qu6(message: Message, state: FSMContext):
    if (message.text.lower()=="да"):
        MyGlobals.mylist.append(1)
    else:
        MyGlobals.mylist.append(0)
    if (MyGlobals.mylist[-1]==1):
        await message.answer(f"Отлично! Будем держать тебя  в курсе. ")
    else:
     await message.answer(f"Будем совершеннствоваться, чтобы заинтересовать тебя. Пока.")
    await state.set_state(teststate.q6)



# Этап выбора блюда #
'''

@router.message(teststate.q3)
async def qu4(message: Message, state: FSMContext):
    

    kb = [
        [
            types.KeyboardButton(text="да"),
            types.KeyboardButton(text="нет")
        ],
     ]
   
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Сделай выбор"
    )

    await message.answer(
        text="Спасибо. Теперь, пожалуйста, выберите размер порции:",
        reply_markup=keyboard
    )
    await state.set_state(teststate.q4)
    '''