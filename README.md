# SimilarVerse-Backend

**SimilarVerse-Backend** is a RESTful API backend that is designed to manage and serve Quranic verses, their translations, and corresponding audio files. Built using FastAPI, it provides a scalable solution for handling verse retrieval, similarity searches, and audio playback.

## Features

- Retrieve Quranic verses with translations in English and Urdu
- Search for similar verses based on Arabic text or verse number
- Play audio for all verses
- Pagination support for verse retrieval

## Project Structure

```bash
SimilarVerse-Backend/
│
├── app/
│   ├── middleware/
│   │   └── cors.py             # CORS handling
│   ├── routers/
│   │   └── routes.py           # API route definitions
│   ├── schemas/
│   │   └── schema.py           # Pydantic models
│   └── utils/
│       ├── data_ingestion.py    # Script for data ingestion
│       ├── data_preprocessing.py# Script for data preprocessing
│       └── similar_verse.py     # Core logic for similar verse matching
│
├── data/
│   ├── audio/                   # Quranic audio files
│   └── QuranCompiled.csv        # CSV file containing Quranic verses
│
├── main.py                      # Main FastAPI app
└── README.md                    # Project documentation
```
## Installation

### Prerequisites
- Python 3.8+

### Setup Instructions

1. **Clone the Repository**
2. **Create a new Virtual Environment**
```python -m venv venv ```
``` venv\Scripts\activate ```
3. **Install Required Libraries Install dependencies from requirements.txt**
   ```pip install -r requirements.txt```
4. **Download the Audio Dataset if you want to play the audio recition from here ```https://www.kaggle.com/datasets/omartariq612/quran-reciters``` and extract the .mp3 files of your favourite recitor in data/audio ***
5. **Run the Application Start the FastAPI server with Uvicorn:**
   ```uvicorn app.main:app --reload```


### API Endpoints
** Search For Similar Verses **
- To search by verse number pass the verse as {"Surah_No" : 5, "Ayah_No" : 2} in the body in JSON

``` POST : / ```

- To search by Arabic pass the arabic text as {
    "arabic" : "ٱلطَّيِّبَـٰتُ ۙ وَمَا عَلَّمْتُم مِّنَ ٱلْجَوَارِحِ مُكَلِّبِينَ"
} in JSON

``` POST : /arabic```

- To play the verse pass the surah number and ayah number

``` GET : /play/5/2 ``` 
