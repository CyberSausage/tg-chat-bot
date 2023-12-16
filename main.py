from Token import token
from aiogram import Bot, Dispatcher, executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
from data_base import select_description
from Kewboard import city_menu
from RequestS import city_zapros
from Flibusta import main
import emoji

bot = Bot(token=token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: Message):
    await message.answer(f"Привет, {message.chat.first_name}", "html")

main_menu = InlineKeyboardMarkup()
main_menu.add(InlineKeyboardButton(text="Городишки", callback_data="CityMain")
              ).add(InlineKeyboardButton(text="Таро", callback_data="taro_karts"))

@dp.message_handler(text=["Города", "Привет", "Карты", "города", "привет", "карты"])
async def menu(message: Message):
    await message.answer(text=f"Чего тебе?", reply_markup=main_menu)

@dp.callback_query_handler(text="back_main_menu")
async def Back_Main(callback: CallbackQuery):
    await bot.edit_message_text(text="Чего тебе?", chat_id=callback.message.chat.id, message_id=callback.message.message_id, reply_markup=main_menu)

@dp.callback_query_handler(text="CityMain")
async def City_Menu(callback: CallbackQuery):
    await bot.edit_message_text(text="Выберите букву:", chat_id=callback.message.chat.id, message_id=callback.message.message_id, reply_markup=city_menu) # импортируется из Kewboard

taro_menu = InlineKeyboardMarkup()
taro_menu.add(InlineKeyboardButton(text="Старшие тараканы", callback_data="big_tarakan")
              ).add(InlineKeyboardButton(text="Младшие тараканы", callback_data="small_tarakan")
              ).add(InlineKeyboardButton(text=f"{emoji.emojize(':fast_reverse_button:')} Назад", callback_data="back_main_menu"))

@dp.callback_query_handler(text="taro_karts")
async def Taro_Menu(callback: CallbackQuery):
    await bot.edit_message_text(text=f" " + emoji.emojize(':joker:') + ": ", chat_id=callback.message.chat.id, message_id=callback.message.message_id, reply_markup=taro_menu)

@dp.callback_query_handler(text="kards")
async def menu(callback: CallbackQuery):
    await bot.edit_message_text(text=f" " + emoji.emojize(':joker:') + ": ", chat_id=callback.message.chat.id, message_id=callback.message.message_id, reply_markup=taro_menu)

callback_city_list = ["а", "б", "в", "г", "д", "е", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "э", "ю", "я"]

@dp.callback_query_handler(text=callback_city_list)
async def Request(callback: CallbackQuery):
    back = InlineKeyboardMarkup()
    back.add(InlineKeyboardButton(text=f"{emoji.emojize(':fast_reverse_button:')} Назад", callback_data="CityMain"))
    answer, count_str, time_answer = city_zapros(callback.data)
    await bot.edit_message_text(text=answer + time_answer, chat_id=callback.message.chat.id, message_id=callback.message.message_id, reply_markup=back)

@dp.callback_query_handler(text="big_tarakan")
async def big_tarakan_1(callback: CallbackQuery):
    BIG_tarakans = InlineKeyboardMarkup()
    BIG_tarakans.add(InlineKeyboardButton(text=f"МАГ {emoji.emojize(':mage:')}", callback_data="mag"),
                     InlineKeyboardButton(text=f"КОЛЕСНИЦА {emoji.emojize(':shopping_cart:')}", callback_data="kolestnitsa")
                     ).add(InlineKeyboardButton(text=f"ИМПЕРАТРИЦА {emoji.emojize(':princess:')}", callback_data="imperatritsa"),
                     InlineKeyboardButton(text=f"ИМПЕРАТОР {emoji.emojize(':prince:')}", callback_data="imperator")
                     ).add(InlineKeyboardButton(text=f"ЖРИЦА {emoji.emojize(':woman_with_veil:')}", callback_data="zhritsia"),
                     InlineKeyboardButton(text=f"ЖРЕЦ {emoji.emojize(':man_teacher:')}", callback_data="zhrets")
                     ).add(InlineKeyboardButton(text=f"ВЛЮБЛЁННЫЕ {emoji.emojize(':couple_with_heart_woman_man:')}", callback_data="vliublennuie"),
                     InlineKeyboardButton(text=f"ПРАВОСУДИЕ {emoji.emojize(':balance_scale:')}", callback_data="pravosudie")
                     ).add(InlineKeyboardButton(text=f"ОТШЕЛЬНИК {emoji.emojize(':person_with_white_cane:')}", callback_data="otshelnik"),
                     InlineKeyboardButton(text=f"КОЛЕСО СУДЬБЫ {emoji.emojize(':gear:')}", callback_data="koleso_sudbui")
                     ).add(InlineKeyboardButton(text=f"{emoji.emojize(':fast_reverse_button:')} Назад", callback_data="kards"),
                     InlineKeyboardButton(text=f"Далее {emoji.emojize(':fast-forward_button:')}", callback_data="big_tarakan_2"))
    await bot.edit_message_text(text="Страшные тараканы!!!", chat_id=callback.message.chat.id, message_id=callback.message.message_id, reply_markup=BIG_tarakans)

@dp.callback_query_handler(text="big_tarakan_2")
async def big_tarakan_2(callback: CallbackQuery):
    BIG_tarakans = InlineKeyboardMarkup()
    BIG_tarakans.add(InlineKeyboardButton(text=f"СИЛА {emoji.emojize(':flexed_biceps:')}", callback_data="sila"),
                     InlineKeyboardButton(text=f"ПОВЕШЕННЫЙ {emoji.emojize(':chair:')}", callback_data="poveshennui")
                     ).add(InlineKeyboardButton(text=f"СМЕРТЬ {emoji.emojize(':skull_and_crossbones:')}", callback_data="smert"),
                     InlineKeyboardButton(text=f"УМЕРЕННОСТЬ {emoji.emojize(':chocolate_bar:')}", callback_data="umerennost")
                     ).add(InlineKeyboardButton(text=f"ДЬЯВОЛ {emoji.emojize(':smiling_face_with_horns:')}", callback_data="diavol"),
                     InlineKeyboardButton(text=f"БАШНЯ {emoji.emojize(':hindu_temple:')}", callback_data="bashnia")
                     ).add(InlineKeyboardButton(text=f"ЗВЕЗДА {emoji.emojize(':dizzy:')}", callback_data="zvezda"),
                     InlineKeyboardButton(text=f"СУД {emoji.emojize(':man_judge:')}", callback_data="sud")
                     ).add(InlineKeyboardButton(text=f"ЛУНА {emoji.emojize(':new_moon_face:')}", callback_data="luna"),
                     InlineKeyboardButton(text=f"СОЛНЦЕ {emoji.emojize(':sun_with_face:')}", callback_data="solntse")
                     ).add(InlineKeyboardButton(text=f"МИР {emoji.emojize(':globe_showing_Asia-Australia:')}", callback_data="mir"),
                     InlineKeyboardButton(text=f"ШУТ {emoji.emojize(':clown_face:')}", callback_data="shut")
                     ).add(InlineKeyboardButton(text=f"{emoji.emojize(':fast_reverse_button:')} Назад", callback_data="big_tarakan"))
    await bot.edit_message_text(text="Страшные тараканы!!!", chat_id=callback.message.chat.id, message_id=callback.message.message_id, reply_markup=BIG_tarakans)

big_tarakan_list = ["mag", "kolestnitsa", "imperatritsa", "imperator", "zhritsia", "zhrets", "vliublennuie", "pravosudie", "otshelnik", "koleso_sudbui", "sila", "poveshennui",
                                 "smert", "umerennost", "diavol", "bashnia", "zvezda", "sud", "luna", "solntse", "mir", "shut"]

@dp.callback_query_handler(text=big_tarakan_list)
async def description_big_tar(callback: CallbackQuery):
    message_answer = str(select_description(callback.data)).replace("('", "").replace("',)", "")
    btn_back = InlineKeyboardMarkup()
    btn_back.add(InlineKeyboardButton(text=f"{emoji.emojize(':fast_reverse_button:')} Назад", callback_data="big_tarakan"))

    await bot.edit_message_text(text=message_answer, chat_id=callback.message.chat.id,
                                message_id=callback.message.message_id, reply_markup=btn_back)

@dp.message_handler()
async def anime(message: Message):
    text_message = message.text.lower()
    if (text_message.find("скачать книгу:") != -1):
        name = text_message.replace("скачать книгу", "").replace(": ", "")
        if (main(name).find("Файл скачен") != -1 ):
            with open(f'{name}.fb2', 'rb') as file:
                await message.reply_document(file)
        else:
            await message.answer(text="Бот наебнулся(или сайт лёг, но скорее всего всё-таки бот)")
    else:
        pass

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)