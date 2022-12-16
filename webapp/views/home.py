import fastapi
from fastapi_chameleon import template
from starlette.requests import Request
from webapp.viewmodels.home.indexviewmodel import IndexViewModel
from webapp.viewmodels.shared.viewmodel import ViewModelBase

router = fastapi.APIRouter()

@router.get('/')
@template()
async def index(request: Request):
    vm = IndexViewModel(request)
    await vm.load()
    return vm.to_dict()
    # return {
    #     'package_count': 274_000,
    #     'release_count': 2_234_847,
    #     'user_count': 73_874,
    #     'packages': [
    #         {'id': 'fastapi', 'summary': "A great web framework."},
    #         {'id': 'uvicorn', 'summary': "Your favorite ASGI server."},
    #         {'id': 'httpx', 'summary': "Request for async world."}
    #     ]
    # }


@router.get('/about')
@template()
def about(request: Request):
    vm = ViewModelBase(request)
    return vm.to_dict()
