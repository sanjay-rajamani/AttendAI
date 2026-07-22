from pydantic import BaseModel


class TextImport(BaseModel):
    text: str