from pydantic import BaseModel, Field
import datetime

class Post(BaseModel):
  id: int = None
  korisnik: str = Field(..., max_length=20)
  tekst: str = Field(..., max_length=280)
  vrijeme: datetime.datetime = Field(default_factory=datetime.datetime.now)

class PostResponse(BaseModel):
  id: int
  korisnik: str
  tekst: str
  vrijeme: datetime.datetime
