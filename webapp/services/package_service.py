import datetime
from typing import Optional
from webapp.data.package import Package
from webapp.data.release import Release

def release_count() -> int:
    return 2_234_847

def package_count() -> int:
    return 274_000

def latest_releases(limit: int=5) -> int:
    return [
        {'id': 'fastapi', 'summary': "A great web framework."},
        {'id': 'uvicorn', 'summary': "Your favorite ASGI server."},
        {'id': 'httpx', 'summary': "Request for async world."}
    ][:limit]


def get_package_by_id(package_name: str) -> Optional[Package]:
    package = Package(
        package_name, "This is a summary", "Full details here!",
        "https://fastapi.tiangolo.com/", "MIT", "Sebastian Ramirez"
    )
    return package

def get_latest_release_for_packages(package_name: str) -> Optional[Release]:
    return Release("1.2.0", datetime.datetime.now())