from aiogram import Router

from handlers.admin.common import router as common_router


admin_router = Router()

admin_router.include_routers(common_router)