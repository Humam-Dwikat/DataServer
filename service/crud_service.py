from fastapi import APIRouter

router = APIRouter(prefix='/v1')


@router.get("/")
def get_data(_id: str):
    pass
