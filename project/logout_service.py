import prisma
import prisma.models
from pydantic import BaseModel


class LogoutResponseModel(BaseModel):
    """
    A simple model to confirm the successful invalidation of the user's authentication token, effectively logging them out.
    """

    message: str


async def logout(token: str) -> LogoutResponseModel:
    """
    Terminates the user's authenticated session by invalidating the provided authentication token.

    Args:
        token (str): The authentication token of the user that needs to be invalidated for logging out.

    Returns:
        LogoutResponseModel: A simple model to confirm the successful invalidation of the user's authentication token, effectively logging them out.

    Example:
        logout("sometoken123")
        > LogoutResponseModel(message="User successfully logged out.")
    """
    api_key = await prisma.models.ApiKey.prisma().find_unique(
        where={"key": token}, include={"User": True}
    )
    if api_key:
        await prisma.models.ApiKey.prisma().delete(where={"id": api_key.id})
        return LogoutResponseModel(message="User successfully logged out.")
    else:
        return LogoutResponseModel(message="Invalid token or already logged out.")
