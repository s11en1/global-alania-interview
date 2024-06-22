from fastapi import FastAPI, Request

from routers import auth_router, users_router, devices_router, terminals_router

app = FastAPI()

app.include_router(auth_router, prefix='/auth', tags=['auth'])
app.include_router(users_router, prefix='/users', tags=['users'])
app.include_router(devices_router, prefix='/devices', tags=['devices'])
app.include_router(terminals_router, prefix='/terminals', tags=['terminals'])


@app.get("/headers")
async def read_headers(request: Request):
    headers = request.headers
    return {"headers": dict(headers)}