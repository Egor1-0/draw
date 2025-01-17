from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart

import keyboards.user as user_kb
import database.queries as db
from keyboards.user import DeleteWordFactory
from states.states import GetWord

router = Router()


@router.message(CommandStart())
async def start(message: Message):
    await db.add_user(tg_id=message.from_user.id)
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
        await message.answer('Слово должно быть СЛОВОМ. Введите заново или нажмите "отмена"', reply_markup=user_kb.cancel)
        return

    user = await db.get_user(message.from_user.id)
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
async def wait_for_word_ro_delete(callback: CallbackQuery,
                                  callback_data: DeleteWordFactory):
    await db.delete_word(word_id=callback_data.word_id)
    await callback.message.answer('Слово удалено')
    await callback.answer()