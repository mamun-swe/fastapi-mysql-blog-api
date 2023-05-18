from fastapi import APIRouter
from schema import blog

routers = APIRouter()


# List of resource
@routers.get('/')
async def index():
    return {"status": True, "message": "Blog list.", "data": []}


# Get specific resource
@routers.get('/{id}')
async def show(id: int):
    return {"status": True, "message": "Blog information.", "data": {id}}


# Store new resource
@routers.post('/')
async def store(documents: blog.BlogCreate):
    return {"status": True, "message": "Blog created.", "data": documents}


# Update specific resource
@routers.put('/{id}')
async def store(id: int, documents: blog.BlogCreate):
    return {"status": True, "message": "Blog updated.", "data": documents}


# Destroy specific resource
@routers.put('/{id}')
async def destroy(id: int):
    return {"status": True, "message": "Blog deleted.", "data": None}
