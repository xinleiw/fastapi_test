from fastapi import APIRouter

from app.api import hello, product


api_router = APIRouter()
api_router.include_router(hello.router, prefix="/hello", tags=["hello"])
api_router.include_router(product.router, prefix="/product", tags=["product"])
