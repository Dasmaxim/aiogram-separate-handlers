from aiogram import types
from misc import dp


@dp.message_handler(commands=['cancel'])
async def cmd_cancel(message: types.Message):
    await message.reply("Cancel")
