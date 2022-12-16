import fastapi
import asyncio
from fastapi_chameleon import template
from webapp.services import user_service
from webapp.viewmodels.account.account_viewmodel import AccountViewModel
from webapp.viewmodels.account.login_viewmodel import LoginViewModel
from webapp.viewmodels.account.register_viewmodel import RegisterViewModel
from webapp.infraestructure import cookie_auth
from starlette.requests import Request
from starlette import status

router = fastapi.APIRouter()

@router.get('/account')
@template()
async def index(request: Request):
    vm = AccountViewModel(request)
    await vm.load()
    return vm.to_dict()

@router.get('/account/register')
@template()
def register(request: Request):
    vm = RegisterViewModel(request)
    return vm.to_dict()


@router.post('/account/register')
@template()
async def register(request: Request):
    vm = RegisterViewModel(request)
    await vm.load()
    if vm.error:
        return vm.to_dict()

    # TODO: Create the account
    account = await user_service.create_account(vm.name, vm.email, vm.password)
    # TODO: Login user
    response = fastapi.responses.RedirectResponse(url='/account', status_code=status.HTTP_302_FOUND)
    cookie_auth.set_auth(response, account.id)

    return response


@router.get('/account/login')
@template()
def login(request: Request):
    vm = LoginViewModel(request)
    return vm.to_dict()


@router.post('/account/login')
@template(template_file='account/login.pt')
async def login_post(request: Request):

    vm = LoginViewModel(request)
    await vm.load()

    if vm.error:
        return vm.to_dict()

    user = await user_service.login_user(vm.email, vm.password)
    if not user:
        # Si el usurio o pass es incorercto, esperamos 5 seg antes
        # de dar una respuesta
        await asyncio.sleep(5)
        vm.error = "The account does not exist or the password is wrong."
        return vm.to_dict()

    resp = fastapi.responses.RedirectResponse('/account', status_code=status.HTTP_302_FOUND)
    cookie_auth.set_auth(resp, user.id)

    return resp


@router.get('/account/logout')
def logout():
    response = fastapi.responses.RedirectResponse(url='/', status_code=status.HTTP_302_FOUND)
    cookie_auth.logout(response)

    return response
