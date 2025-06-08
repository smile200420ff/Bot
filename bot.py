
""" 
Bot initialization and configuration 
"""

import os
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from handlers import start, escrow, admin, payment
from utils.database import init_db
from config import BOT_TOKEN

async def create_bot():
    """Create and configure the bot instance"""

    # Initialize bot with default properties
    bot = Bot(
        token=BOT_TOKEN,
        parse_mode=ParseMode.HTML,
        client=DefaultBotProperties()
    )

    # Initialize dispatcher with storage
    storage = MemoryStorage()
    dp = Dispatcher(bot, storage=storage)

    # Register handlers
    dp.include_router(start.router)
    dp.include_router(escrow.router)
    dp.include_router(admin.router)
    dp.include_router(payment.router)

    # Initialize database
    await init_db()

    return bot, dp
