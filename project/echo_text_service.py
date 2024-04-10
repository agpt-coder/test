from pydantic import BaseModel


class EchoTextOutput(BaseModel):
    """
    The response model for echoing text, containing the same text that was received in the request. This ensures the echo functionality is accurately executed.
    """

    text: str


def echo_text(text: str) -> EchoTextOutput:
    """
    Receives a text input from the user and echoes it back.

    Args:
    text (str): The text input from the user that needs to be echoed back.

    Returns:
    EchoTextOutput: The response model for echoing text, containing the same text that was received in the request. This ensures the echo functionality is accurately executed.

    Example:
        text = "Hello, World!"
        echo_response = echo_text(text)
        print(echo_response.text)
        > Hello, World!
    """
    return EchoTextOutput(text=text)
