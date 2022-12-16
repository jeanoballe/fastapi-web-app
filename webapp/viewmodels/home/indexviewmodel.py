from starlette.requests import Request
from typing import List
from webapp.viewmodels.shared.viewmodel import ViewModelBase
from webapp.services import package_service
from webapp.services import user_service


class IndexViewModel(ViewModelBase):
    def __init__(self, request: Request) -> None:
        super().__init__(request)

        self.release_count: int = package_service.release_count()
        self.user_count: int = user_service.user_count()
        self.package_count: int = package_service.package_count()
        self.packages: List = package_service.latest_packages(limit=7)