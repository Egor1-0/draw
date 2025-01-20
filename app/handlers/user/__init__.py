from aiogram import Router

from handlers.user.add_key import router as common_router
from handlers.user.common import router as add_key_router


user_router = Router()

user_router.include_routers(add_key_router, common_router)