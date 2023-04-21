import json
import os

import aiofiles
import aiohttp

from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN_API

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


@dp.message_handler()
async def echo(message: types.Message):
    async with aiohttp.ClientSession() as session:
        async with session.get('https://random.dog/woof.json') as resp:
            img_pas = json.loads(str(await resp.text())).get('url')
            ext = str(img_pas).split('.')[len(str(img_pas).split('.')) - 1]

    async with aiohttp.ClientSession() as session:
        async with session.get(img_pas) as resp:
            if resp.status == 200:
                f = await aiofiles.open('dog' + f'.{ext}', mode='wb')
                await f.write(await resp.read())
                await f.close()
    f = open('dog' + f'.{ext}', 'rb')
    await message.reply_document(f)
    os.remove(f.name)

if __name__ == '__main__':
    executor.start_polling(dp)
