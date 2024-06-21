from sqlalchemy import Integer
from sqlalchemy.orm import Mapped, mapped_column
from workout_api.contrib.models import BaseModel

class AtletaModel(BaseModel):
    __tablename__ = 'atletas'
    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    
    