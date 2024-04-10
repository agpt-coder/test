import logging
from contextlib import asynccontextmanager

import project.echo_text_service
import project.login_service
import project.logout_service
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import Response
from prisma import Prisma

logger = logging.getLogger(__name__)

db_client = Prisma(auto_register=True)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await db_client.connect()
    yield
    await db_client.disconnect()


app = FastAPI(
    title="test",
    lifespan=lifespan,
    description="Based on the provided user feedback, the task involves creating an API that echoes back any text it receives. This requirement signifies the need for a simple yet functional API endpoint that accepts text input from the user and returns the same text as the output. Utilizing the specified tech stack, which includes Python as the programming language, FastAPI for the API framework, PostgreSQL for the database, and Prisma as the Object Relational Mapping (ORM) tool, the implementation will focus on setting up a RESTful API Service. The FastAPI framework will be utilized to set up the API routes, taking advantage of its asynchronous request handling and its automatic interactive API documentation. Since the core functionality is to echo back received text, the use of PostgreSQL and Prisma might only come into play if there's a need to store the requests or responses for logging or monitoring purposes. To summarize, the API will be a straightforward implementation focusing primarily on request handling and response mechanism to fulfill the echo functionality desired.",
)


@app.post("/echo", response_model=project.echo_text_service.EchoTextOutput)
async def api_post_echo_text(
    text: str,
) -> project.echo_text_service.EchoTextOutput | Response:
    """
    Receives a text input from the user and echoes it back.
    """
    try:
        res = project.echo_text_service.echo_text(text)
        return res
    except Exception as e:
        logger.exception("Error processing request")
        res = dict()
        res["error"] = str(e)
        return Response(
            content=jsonable_encoder(res),
            status_code=500,
            media_type="application/json",
        )


@app.post("/auth/logout", response_model=project.logout_service.LogoutResponseModel)
async def api_post_logout(
    token: str,
) -> project.logout_service.LogoutResponseModel | Response:
    """
    Terminates the user's authenticated session.
    """
    try:
        res = await project.logout_service.logout(token)
        return res
    except Exception as e:
        logger.exception("Error processing request")
        res = dict()
        res["error"] = str(e)
        return Response(
            content=jsonable_encoder(res),
            status_code=500,
            media_type="application/json",
        )


@app.post("/auth/login", response_model=project.login_service.LoginOutput)
async def api_post_login(
    username: str, password: str
) -> project.login_service.LoginOutput | Response:
    """
    Handles user login, issuing tokens for authenticated sessions.
    """
    try:
        res = await project.login_service.login(username, password)
        return res
    except Exception as e:
        logger.exception("Error processing request")
        res = dict()
        res["error"] = str(e)
        return Response(
            content=jsonable_encoder(res),
            status_code=500,
            media_type="application/json",
        )
