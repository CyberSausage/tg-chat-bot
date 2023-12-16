from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import emoji
city_menu = InlineKeyboardMarkup()
city_menu.add(InlineKeyboardButton(text="A", callback_data="а"),
              InlineKeyboardButton(text="Б", callback_data="б")
              ).add(InlineKeyboardButton(text="В", callback_data="в"),
              InlineKeyboardButton(text="Г", callback_data="г")
              ).add(InlineKeyboardButton(text="Д",callback_data="д"),
              InlineKeyboardButton(text="Е", callback_data="е")
              ).add(InlineKeyboardButton(text="Ж",callback_data="ж"),
              InlineKeyboardButton(text="З", callback_data="з")
              ).add(InlineKeyboardButton(text="И",callback_data="и"),
              InlineKeyboardButton(text="Й", callback_data="й")
              ).add(InlineKeyboardButton(text="К",callback_data="к"),
              InlineKeyboardButton(text="Л", callback_data="л")
              ).add(InlineKeyboardButton(text="М",callback_data="м"),
              InlineKeyboardButton(text="Н", callback_data="н")
              ).add(InlineKeyboardButton(text="О",callback_data="о"),
              InlineKeyboardButton(text="П", callback_data="п")
              ).add(InlineKeyboardButton(text="Р", callback_data="р"),
              InlineKeyboardButton(text="С", callback_data="с")
              ).add(InlineKeyboardButton(text="Т", callback_data="т"),
              InlineKeyboardButton(text="У", callback_data="у")
              ).add(InlineKeyboardButton(text="Ф", callback_data="ф"),
              InlineKeyboardButton(text="Х", callback_data="х")
              ).add(InlineKeyboardButton(text="Ц", callback_data="ц"),
              InlineKeyboardButton(text="Ч", callback_data="ч")
              ).add(InlineKeyboardButton(text="Ш", callback_data="ш"),
              InlineKeyboardButton(text="Щ", callback_data="щ")
              ).add(InlineKeyboardButton(text="Э", callback_data="э"),
              InlineKeyboardButton(text="Ю", callback_data="ю")
              ).add(InlineKeyboardButton(text="Я", callback_data="я"),
              InlineKeyboardButton(text=f"{emoji.emojize(':fast_reverse_button:')} Назад", callback_data="back_main_menu"))