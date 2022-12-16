from typing import Optional
from starlette.requests import Request

from webapp.viewmodels.shared.viewmodel import ViewModelBase
from webapp.services import user_service


class RegisterViewModel(ViewModelBase):
    def __init__(self, request: Request) -> None:
        super().__init__(request)
        self.email: Optional[str] = None
        self.name: Optional[str] = None
        self.password: Optional[str] = None

    async def load(self):
        form = await self.request.form()
        self.name = form.get('name')
        self.password = form.get('password')
        self.email = form.get('email')

        if not self.name or not self.name.strip():
            self.error = "Your name is required."

        if not self.password or len(self.password) < 5:
            self.error = "Your password is required and must be at least 5 characters."

        if not self.email or not self.email.strip():
            self.error = "Your email is required."

        elif await user_service.get_user_by_email(self.email):
            self.error = "That email is already taken. Log in instead?"
