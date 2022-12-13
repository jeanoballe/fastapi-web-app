import fastapi
from fastapi_chameleon import template
from webapp.viewmodels.account.account_viewmodel import AccountViewModel
from webapp.viewmodels.account.login_viewmodel import LoginViewModel
from webapp.viewmodels.account.register_viewmodel import RegisterViewModel
from starlette.requests import Request

router = fastapi.APIRouter()

@router.get('/account')
def index(request: Request):
    vm = AccountViewModel(request)
    return vm.to_dict()

@router.get('/account/register')
def register(request: Request):
    vm = RegisterViewModel(request)
    return vm.to_dict()

@router.get('/account/login')
def login(request: Request):
    vm = LoginViewModel(request)
    return vm.to_dict()

@router.get('/account/logout')
def logout():
    return {}
