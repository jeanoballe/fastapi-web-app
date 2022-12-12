import fastapi
import uvicorn
import fastapi_chameleon
from fastapi_chameleon import template
from starlette.staticfiles import StaticFiles
from webapp.views import account
from webapp.views import home
from webapp.views import packages


app = fastapi.FastAPI()


def main():
    configure()
    uvicorn.run(app, host='127.0.0.1', port=8080)

def configure():
    configure_templates()
    configure_routes()

def configure_templates():
    fastapi_chameleon.global_init('webapp/templates/')

def configure_routes():
    app.mount('/static', StaticFiles(directory='webapp/static'), name='static')
    app.include_router(home.router)
    app.include_router(account.router)
    app.include_router(packages.router)

def configure():
    configure_templates()
    configure_routes()


if __name__ == '__main__':
    main()
else:
    configure()