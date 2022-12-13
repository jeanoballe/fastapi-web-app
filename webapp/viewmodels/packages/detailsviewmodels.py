import datetime
from webapp.viewmodels.shared.viewmodel import ViewModelBase
from webapp.services import package_service
from webapp.data.release import Release
from starlette.requests import Request

class DetailsViewModel(ViewModelBase):
    def __init__(self, package_name: str, request: Request) -> None:
        super().__init__(request)
        self.package_name = package_name
        self.package = package_service.get_package_by_id(package_name)
        self.latest_release = package_service.get_latest_release_for_packages(package_name)
        self.lastes_version = "0.0.0.0"
        self.is_latest = True
        self.maintainers = []

        if not self.package and not self.latest_release:
            return
    
        self.latest_version = self.latest_release.version
        self.maintainers = self.package.maintainers
