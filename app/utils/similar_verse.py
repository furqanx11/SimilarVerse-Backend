import pandas as pd

quran_compiled = pd.read_csv('data/QuranCompiled.csv')

def get_similar_verse(number=None, arabic=None):
    if number:
        response = quran_compiled[(quran_compiled['SurahNo'] == number['SurahNo']) & (quran_compiled['AyahNo'] == number['AyahNo'])][['Arabic', 'EnglishTranslation', 'UrduTranslation', 'SurahNo', 'AyahNo']].values[0]
        return response
    elif arabic:
        # Debugging: Print the Arabic text being searched
        print(f"\nSearching for Arabic text: {arabic}")
        response = quran_compiled[quran_compiled['Arabic'].str.contains(arabic, na=False)][['Arabic', 'EnglishTranslation', 'UrduTranslation', 'SurahNo', 'AyahNo']].values
        return response
