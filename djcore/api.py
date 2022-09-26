from ninja_extra import NinjaExtraAPI
from decouple import config
from users.controllers import UserController, UserTokenController

api = NinjaExtraAPI(
    version=config('VERSION') or '0.1',
    csrf=True,
    title=config("TITLE", default ='Title'),
    description=config("DESCRIPTION", default ='Description')
)
# api.auto_discover_controllers()
api.register_controllers(UserController)
api.register_controllers( UserTokenController)
