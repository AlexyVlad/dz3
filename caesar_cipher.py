from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN_API

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

@dp.message_handler()
async def echo(message: types.Message):
    ans = ''
    for i in range(len(message.text)):
        ans += chr(ord(str(message.text)[i]) + 1)
    await message.answer(ans)

if __name__ == '__main__':
    executor.start_polling(dp)
