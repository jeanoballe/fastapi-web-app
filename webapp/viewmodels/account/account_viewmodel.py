from webapp.viewmodels.shared.viewmodel import ViewModelBase
from webapp.data.user import User
from starlette.requests import Request


class AccountViewModel(ViewModelBase):
    def __init__(self, request: Request) -> None:
        super().__init__(request)
        self.user = User('Jean', 'jcoballe@gmail.com', 'qdqqfe')
