"""
    tests/test_login.py
    Method : test_sign_new_user
    Param : default_client: httpx.AsyncClient
"""

import httpx
import pytest

@pytest.mark.asyncio
async def test_sign_new_user(default_client: httpx.AsyncClient) -> None:
    payload = {
        "email": "test3user@packt.com",
        "password": "testpassword",
    }
    # 요청 헤더와 응답을 정의함
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }
    test_response = {
        "message": "User successfully registered"
            # "User created successfully."
    }
    # 요청에 대한 예상 응답을 정의함
    response = await default_client.post("/user/signup", json=payload,
                                         headers=headers)
    # 응답을 비교해서 요청이 성공했는지 확인하는 코드 작성
    assert response.status_code == 200
    assert response.json() == test_response


@pytest.mark.asyncio
async def test_sign_user_in(default_client: httpx.AsyncClient) -> None:
    payload = {
        "username": "test3user@packt.com",
        "password": "testpassword"
    }

    headers = {
        "accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    response = await default_client.post("/user/signin", data=payload, headers=headers)

    assert response.status_code == 200
    assert response.json()["token_type"] == "Bearer"