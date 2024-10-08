from pydantic import BaseModel
from typing import Optional

class VerseNumber(BaseModel):
    SurahNo: Optional[int] = None
    AyahNo: Optional[int] = None

class ArabicText(BaseModel):
    arabic: str