
from fastapi import FastAPI, Depends, HTTPException, status, Request, Response, Security
from fastapi.responses import RedirectResponse
from fastapi.security import OAuth2AuthorizationCodeBearer, HTTPBearer
import httpx
from urllib.parse import urlencode
import logging


from .config import get_settings

settings = get_settings()


async def login():
    authorization_url = (
        f"https://{settings.auth0_domain}/authorize"
        f"?response_type=code&client_id={settings.auth0_client_id}"
        f"&redirect_uri={settings.auth0_callback_url}&scope=openid"
    )
    return RedirectResponse(url=authorization_url)


async def logout():
    return_to_url = settings.origins  # "http://127.0.0.1:8000/"  # The URL where the user should be redirected after logout
    return_to_encoded = urlencode({"returnTo": return_to_url})
    logout_url = f"https://{settings.auth0_domain}/v2/logout?client_id={settings.auth0_client_id}&{return_to_encoded}"
    return RedirectResponse(url=logout_url)


async def callback(code:str):
    token_url = f"https://{settings.auth0_domain}/oauth/token"
    token_headers = {"content-type": "application/x-www-form-urlencoded"}
    token_data = {
        "grant_type": "authorization_code",
        "client_id": settings.auth0_client_id,
        "client_secret": settings.auth0_client_secret,
        "code": code,
        "redirect_uri": settings.auth0_callback_url,
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(token_url, headers=token_headers, data=token_data)
    response.raise_for_status()
    return response.json()