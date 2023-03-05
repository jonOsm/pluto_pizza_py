from fastapi import APIRouter

router = APIRouter(prefix="/addresses", tags=['addresses'])

@router.get("/user/{user_id}")
def get_all_user_addresses(user_id:str):
    pass

@router.post("/user/{user_id}/create")
def store_new_address(user_id):
    pass