from fastapi import APIRouter, HTTPException
from app.schemas.schema import VerseNumber, ArabicText
from app.utils.similar_verse import get_similar_verse


router = APIRouter()

@router.post("/")
def get_verse_by_number(number: VerseNumber):
    try:
        response = get_similar_verse(number=number.dict())
        return {
            "Arabic": response[0],
            "EnglishTranslation": response[1],
            "UrduTranslation": response[2],
            "SurahNo": response[3],
            "AyahNo": response[4]
        }
    except IndexError:
        raise HTTPException(status_code=404, detail="Verse not found")

@router.post("/arabic")
def get_verse_by_arabic(arabic: ArabicText):
    response = get_similar_verse(arabic=arabic.arabic)
    if len(response) == 0:
        raise HTTPException(status_code=404, detail="Verse not found")
    return [
        {
            "Arabic": res[0],
            "EnglishTranslation": res[1],
            "UrduTranslation": res[2],
            "SurahNo": res[3],
            "AyahNo": res[4]
        }
        for res in response
    ]