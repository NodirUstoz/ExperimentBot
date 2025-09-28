import asyncio
from aiogram import Router, F, Bot
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram.enums import ChatAction
import app.keyboards as kb

router = Router()



@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.bot.send_chat_action(chat_id=message.from_user.id, action=ChatAction.TYPING)
    await asyncio.sleep(1)
    await message.reply(f"Hello, {message.from_user.full_name}!", reply_markup=kb.Reply1)


