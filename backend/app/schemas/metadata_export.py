from pydantic import BaseModel


class ErrorResponse(BaseModel):
    success: bool = False
    message: str
    error: str


class ErrorResponseEnvelope(BaseModel):
    """
    How an ErrorResponse actually reaches the client.

    HTTPException nests whatever it is given under `detail`, so documenting
    ErrorResponse alone would describe a shape no client ever receives.
    """

    detail: ErrorResponse
