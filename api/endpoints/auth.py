from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from core.config import settings
from db.session import get_db
from schemas.token import Token
from schemas.user import LoginForm
from schemas.user import User as UserSchema
from schemas.user import UserCreate
from services.auth import authenticate_user, create_access_token
from services.user import create_user, get_user_by_email

router = APIRouter()

@router.post("/register", response_model=UserSchema)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    try:
        db_user = get_user_by_email(db, email=user.email)
        if db_user:
            raise HTTPException(status_code=400, detail="Email already registered")
        return create_user(db=db, user=user)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while registering the user: {str(e)}"
        )

@router.post("/sign-in", response_model=Token)
async def sign_in(
    form_data: LoginForm,
    db: Session = Depends(get_db)
):
    try:
        user = authenticate_user(db, form_data.email, form_data.password)
        
        if not user:
            valid_user = get_user_by_email(db, form_data.email)
            if not valid_user:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="User not found",
                )
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect password",
            )

        # Now, check if the password matches
        if not authenticate_user(db, form_data.email, form_data.password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect password",
            )

        access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": user.email, "role": user.role},
            expires_delta=access_token_expires
        )
        return {"access_token": access_token, "role": user.role.value,"email": user.email}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while signing in: {str(e)}"
        )

@router.post("/sign-out")
async def sign_out():
    try:
        # In a stateless JWT-based auth system, signing out is typically handled client-side
        # by removing the token. Here we'll just return a success message.
        return {"message": "Successfully signed out"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while signing out: {str(e)}"
        )
