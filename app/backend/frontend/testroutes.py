import os
from typing import Annotated

from fastapi import APIRouter, HTTPException, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.requests import Request

from utils.entries.otp_manager import manager as otp_manager
from schemas.otp import OTPRead, OTPCreate, OTPUse


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static")

# Configure Jinja2 templates directory
templates = Jinja2Templates(directory=f"{BASE_DIR}/templates")
router = APIRouter(prefix="/tests")

@router.post("/otp/generate")
async def create_otp(request: Request, otp: Annotated[OTPCreate, Form()]):
    return otp_manager.generate_otp(otp)

@router.get("/otp/list")
async def create_otp(request: Request):
    return otp_manager.get_list()

@router.post("/otp/use")
async def use_otp(request: Request, otp: Annotated[OTPUse, Form()]):
    if not otp_manager.verify_otp(otp):
        raise HTTPException(status_code=400, detail="Invalid OTP")
    return otp_manager.consume_otp(otp)

@router.get("/otp/ui", response_class=HTMLResponse)
async def otp_input(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("otp_input.j2", {"request": request})