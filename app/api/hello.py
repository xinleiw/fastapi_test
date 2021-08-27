from fastapi import APIRouter


router = APIRouter()


@router.get("/")
@router.get("")
def hello():
    return "Hello world"
