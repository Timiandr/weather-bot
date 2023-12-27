import asyncio
import logging

import handlers
from bot import dp, bot, database, notify

logger = logging.getLogger('TGBot')


async def main() -> None:
    database.create()
    loop = asyncio.get_event_loop()
    loop.create_task(notify())
    dp.include_routers(*handlers.routers)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
    except Exception as ex:
        import traceback

        logger.warning(traceback.format_exc())
    finally:
        
        database.close()
