from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from telethon import TelegramClient

import keyboards.user as user_kb
import database.queries as db
from filters import HasPremissonsFilter
from keyboards.user import DeleteWordFactory, DeleteChatFactory
from states.states import GetWord, GetChat
from utils.get_chat_url import get_telegram_link
from utils.join_channel import join_channel_and_get_info

from utils.redis_serv import redis_serv

router = Router()

router.message.filter(HasPremissonsFilter())


@router.message(CommandStart())
async def start(message: Message):
    await message.answer('Приветственный текст', reply_markup=user_kb.start_kb)


@router.callback_query(F.data == 'cancel')
async def cancel(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.message.answer('Отменено')
    await callback.answer()


@router.message(F.text == 'Мои слова')
async def add_word(message: Message):
    user = await db.get_user(message.from_user.id)

    if user.words:
        text = 'Ваши ключевые слова: ' + ', '.join([word.word for word in user.words])
    else:
        text = 'У вас нет ключевых слов'

    await message.answer(text)


@router.message(F.text == 'Добавить ключевое слово')
async def add_word(message: Message, state: FSMContext):
    await state.set_state(GetWord.word)
    await message.answer('Введите ключевое слово или нажмите "отмена"', reply_markup=user_kb.cancel)


@router.message(GetWord.word)
async def wait_for_word(message: Message, state: FSMContext):
    if len(message.text.split()) != 1:
        await message.answer('Слово должно быть СЛОВОМ. Введите заново или нажмите "отмена"',
                             reply_markup=user_kb.cancel)
        return

    user = await db.get_user(message.from_user.id)
    await redis_serv.set_keyword(message.text, user.tg_id)
    await db.add_word(tg_id=user.id, word=message.text)
    await state.clear()
    await message.answer('Слово добавлено')


@router.message(F.text == 'Удалить ключевое слово')
async def delete_keyword(message: Message):
    user = await db.get_user(message.from_user.id)
    if not user.words:
        await message.answer('У вас нет ключевых слов')
        return

    await message.answer('Нажмите на слово, чтобы удалить его',
                         reply_markup=user_kb.delete_keyword_kb(user.words))


@router.callback_query(DeleteWordFactory.filter())
async def wait_for_word_to_delete(callback: CallbackQuery,
                                  callback_data: DeleteWordFactory):
    kw = await db.get_keyword_by_id(callback_data.word_id)
    await db.delete_word(word_id=callback_data.word_id)
    await redis_serv.remove_keyword(kw.value)
    await callback.message.answer('Слово удалено')
    await callback.answer()


@router.message(F.text == 'Добавить чат (канал)')
async def add_word(message: Message, state: FSMContext):
    await state.set_state(GetChat.chat)
    await message.answer('Отправьте ссылку на чат (канал) или нажмите "отмена"', reply_markup=user_kb.cancel)


@router.message(GetChat.chat)
async def wait_for_chat(message: Message, state: FSMContext, userbot: TelegramClient):
    url = get_telegram_link(message)
    if not url:
        await message.answer('Ссылка должна быть ССЫЛКОЙ. введите заново или нажмите "отмена"',
                             reply_markup=user_kb.cancel)
        return

    await state.clear()

    info = await join_channel_and_get_info(userbot, url)
    if not info:
        await message.answer('Произошла ошибка')
        return

    await redis_serv.set_chat(chat_id=info['tg_id'], user_id=message.from_user.id)
    user = await db.get_user(message.from_user.id)
    await db.add_chat(user_id=user.id,
                      link=info['link'],
                      tg_id=info['tg_id'],
                      name=info['name'])
    await message.answer('Чат добавлен')


@router.message(F.text == 'Удалить чат (канал)')
async def delete_keyword(message: Message):
    user = await db.get_user(message.from_user.id)
    if not user.chats:
        await message.answer('У вас нет чатов (каналов)')
        return

    await message.answer('Нажмите на чат (канал), чтобы удалить его',
                         reply_markup=user_kb.delete_chat_kb(user.chats))


@router.callback_query(DeleteChatFactory.filter())
async def wait_for_chat_to_delete(callback: CallbackQuery,
                                  callback_data: DeleteChatFactory):
    chat = await db.get_chat_by_id(chat_id=callback_data.chat_id)
    await db.delete_chat(chat_id=callback_data.chat_id)
    await redis_serv.remove_chat(chat.tg_id)
    await callback.message.answer('Чат (канал) удален')
    await callback.answer()


@router.message(F.text == 'Мои чаты (каналы)')
async def add_word(message: Message):
    user = await db.get_user(message.from_user.id)

    if user.words:
        text = 'Ваши чаты (канал): ' + ', '.join([f'{chat.name} ({chat.link})' for chat in user.chats])
    else:
        text = 'У вас нет чатов (каналов)'

    await message.answer(text)