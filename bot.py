from aiogram import Bot, Dispatcher, executor, types 

bot = Bot(token="5294410598:AAEQEVJoFk1hlZod8Wuos6rLVUE8hc_YXkQ", parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

def keyboard_making(keybrd):
    keybrd.add(types.KeyboardButton(text="Проведать пенсионера"))
    keybrd.add(types.KeyboardButton(text="Данные о пенсионере"))

@dp.message_handler(commands="start")
async def start(message:types.Message): 
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard_making(keyboard)
    await message.answer("Привет, я систа <b>Retiree-Care</b>. Мы позволяем людям <i>всегда</i> быть на связе со своими пожилыми родственниками.", reply_markup=keyboard)
    print("start")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates = True)