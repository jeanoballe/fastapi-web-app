import fastapi
import uvicorn
import fastapi_chameleon
from fastapi_chameleon import template

app = fastapi.FastAPI()
fastapi_chameleon.global_init('webapp/templates')

@app.get("/")
@template(template_file='index.html')
def index(user: str = 'anon'):
    # return {'user_name': user if user else 'anon'}
    return {'user_name': user}


if __name__ == '__main__':
    uvicorn.run(app)
