from pathlib import Path
import fastapi
import uvicorn
import fastapi_chameleon
from fastapi_chameleon import template
from starlette.staticfiles import StaticFiles
from webapp.views import account
from webapp.views import home
from webapp.views import packages
from webapp.data import db_session
from webapp.bin import load_data


app = fastapi.FastAPI(docs_url=None, redoc_url=None)


def main():
    configure(dev_mode=True)
    uvicorn.run(app, host='127.0.0.1', port=8080)


def configure(dev_mode: bool):
    configure_templates(dev_mode)
    configure_routes()
    configure_db(dev_mode)
    # load_data.main()


def configure_db(dev_mode: bool):
    file = (Path(__file__).parent / 'db' / 'pypi.sqlite').absolute()
    db_session.global_init(file.as_posix())


def configure_templates(dev_mode: bool):
    fastapi_chameleon.global_init('webapp/templates/')


def configure_routes():
    app.mount('/static', StaticFiles(directory='webapp/static'), name='static')
    app.include_router(home.router)
    app.include_router(account.router)
    app.include_router(packages.router)


if __name__ == '__main__':
    main()
else:
    configure(dev_mode=False)