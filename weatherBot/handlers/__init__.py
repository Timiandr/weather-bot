from .callback_current import callback_current_router
from .callback_forecast import callback_forecast_router
from .callback_notify import callback_notify_router
from .form_cancel import cancel_router
from .from_city import from_city_router
from .start import start_router

routers = [start_router, cancel_router, from_city_router, callback_current_router, callback_forecast_router,
           callback_notify_router]

__all__ = ["routers"]
