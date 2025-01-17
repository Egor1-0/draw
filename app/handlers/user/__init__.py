from aiogram import Router

from handlers.user.common import router as common_router

user_router = Router()

user_router.include_routers(common_router)