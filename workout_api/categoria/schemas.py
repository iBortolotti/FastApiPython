from typing import Annotated

from pydantic import Field
from workout_api.contrib.schemas import BaseSchema

class Categoria(BaseSchema):
    name: Annotated[str, Field(description='Categoria', example='Sacele', max_length=10)]