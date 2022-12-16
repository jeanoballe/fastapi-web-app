from starlette.requests import Request
from typing import List
from webapp.viewmodels.shared.viewmodel import ViewModelBase
from webapp.services import package_service
from webapp.services import user_service
from webapp.data.package import Package


class IndexViewModel(ViewModelBase):
    def __init__(self, request: Request) -> None:
        super().__init__(request)

        self.release_count: int = 0
        self.user_count: int = 0
        self.package_count: int = 0
        self.packages: List = []

    async def load(self):
        self.release_count: int = await package_service.release_count()
        self.user_count: int = await user_service.user_count()
        self.package_count: int = await package_service.package_count()
        self.packages: List[Package] = await package_service.latest_packages(limit=7)