from fastapi import APIRouter, HTTPException, Query
from app.schemas.schema import VerseNumber, ArabicText
from app.utils.similar_verse import get_similar_verse, get_verses_by_surah


router = APIRouter()

@router.post("/")
def get_verse_by_number(number: VerseNumber):
    response = get_similar_verse(number=number.dict())
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


@router.get("/surah/{surah_no}")
def get_verses_by_surah_no(surah_no: int, page: int = Query(1, ge=1), page_size: int = Query(5, ge=1, le=100)):
    response = get_verses_by_surah(surah_no)
    total_verses = len(response)
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    if start_index >= total_verses:
        raise HTTPException(status_code=404, detail="Page not found")

    paginated_response = response[start_index:end_index]

    return {
        "total_verses": total_verses,
        "page": page,
        "page_size": page_size,
        "verses": [
            {
                "Arabic": res[0],
                "EnglishTranslation": res[1],
                "UrduTranslation": res[2],
                "SurahNo": res[3],
                "AyahNo": res[4]
            }
            for res in paginated_response.values
        ]
    }