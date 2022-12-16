from starlette.requests import Request
from typing import Optional

from webapp.viewmodels.shared.viewmodel import ViewModelBase
from webapp.data.user import User
from webapp.services import user_service


class AccountViewModel(ViewModelBase):
    def __init__(self, request: Request) -> None:
        super().__init__(request)
        self.user: Optional[User] = None

    async def load(self):
        self.user = await user_service.get_user_by_id(self.user_id)
