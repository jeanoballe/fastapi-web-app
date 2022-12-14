from typing import Optional
from webapp.viewmodels.shared.viewmodel import ViewModelBase
from webapp.services import package_service
from webapp.data.release import Release
from webapp.data.package import Package
from starlette.requests import Request


class DetailsViewModel(ViewModelBase):
    def __init__(self, package_name: str, request: Request):
        super().__init__(request)

        self.package_name = package_name
        self.latest_version = "0.0.0"
        self.is_latest = True
        self.maintainers = []
        self.package: Optional[Package] = None
        self.latest_release: Optional[Release] = None

    async def load(self):
        self.package = await package_service.get_package_by_id(self.package_name)
        self.latest_release = await package_service.get_latest_release_for_package(self.package_name)

        if not self.package or not self.latest_release:
            return

        r = self.latest_release
        self.latest_version = f'{r.major_ver}.{r.minor_ver}.{r.build_ver}'
