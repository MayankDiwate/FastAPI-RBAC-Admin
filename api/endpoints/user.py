from fastapi import APIRouter, Depends, HTTPException

from db.models import User
from schemas.user import User as UserSchema
from services.auth import get_current_active_user

router = APIRouter()

@router.get("/", response_model=UserSchema)
async def read_users(current_user: User = Depends(get_current_active_user)):
    try :   
        return current_user
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

