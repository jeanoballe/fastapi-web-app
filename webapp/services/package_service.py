import datetime
from typing import Optional, List
from webapp.data.package import Package
from webapp.data.release import Release
from webapp.data import db_session
import sqlalchemy.orm


def release_count() -> int:
    session = db_session.create_session()
    try:
        return session.query(Release).count()
    finally:
        session.close()

def package_count() -> int:
    session = db_session.create_session()
    try:
        return session.query(Package).count()
    finally:
        session.close()

def latest_packages(limit: int = 5) -> List[Package]:
    session = db_session.create_session()

    try:
        releases = session.query(Release) \
            .options(
            sqlalchemy.orm.joinedload(Release.package)
        ) \
            .order_by(Release.created_date.desc()) \
            .limit(limit) \
            .all()
    finally:
        session.close()

    return list({r.package for r in releases})


def get_package_by_id(package_name: str) -> Optional[Package]:
    package = Package(
        package_name, "This is a summary", "Full details here!",
        "https://fastapi.tiangolo.com/", "MIT", "Sebastian Ramirez"
    )
    return package

def get_latest_release_for_packages(package_name: str) -> Optional[Release]:
    return Release("1.2.0", datetime.datetime.now())