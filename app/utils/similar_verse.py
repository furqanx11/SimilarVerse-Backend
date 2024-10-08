import pandas as pd
import unicodedata
from app.utils.data_preprocessing import normalize_searchtext

quran_compiled = pd.read_csv('data/QuranCompiled.csv')


def get_similar_verse(number=None, arabic=None):
    if number:
        verse = quran_compiled[(quran_compiled['SurahNo'] == number['SurahNo']) & (quran_compiled['AyahNo'] == number['AyahNo'])][['Arabic']].values[0]
        return get_similar_verse(arabic=verse[0])
    elif arabic:
        quran_compiled['ArabicEncoded'] = quran_compiled['Arabic'].apply(normalize_searchtext)
        # Debugging: Print the Arabic text being searched
        arabic = normalize_searchtext(arabic)
        print(f"\nSearching for Arabic text: {arabic}")
        response = quran_compiled[quran_compiled['ArabicEncoded'].str.contains(arabic, na=False)][['Arabic', 'EnglishTranslation', 'UrduTranslation', 'SurahNo', 'AyahNo']].values
        return response

def get_verses_by_surah(surah_no: int):
    return quran_compiled[quran_compiled['SurahNo'] == surah_no][['Arabic', 'EnglishTranslation', 'UrduTranslation', 'SurahNo', 'AyahNo']]
    