from fastapi import FastAPI
from routers import blogs

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to blog API's"}


app.include_router(blogs.routers, prefix='/blogs', tags=['blogs'])
