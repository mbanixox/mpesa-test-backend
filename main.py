from fastapi import FastAPI
from app.mpesa.stk_push import router as stk_router
from app.mpesa.callback import router as callback_router

app = FastAPI()

app.include_router(stk_router, prefix="/mpesa", tags=["mpesa"])
app.include_router(callback_router, prefix="/callback", tags=["callback"])

@app.get("/")
def home():
    return {"message": "M-Pesa API is running!"}