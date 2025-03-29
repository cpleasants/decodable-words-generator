import filter_words
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


# FastAPI application to handle requests for filtering words based on user criteria.
# This application allows CORS from a specified origin to enable interaction with a local frontend.

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allow React app's origin
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
)

class Criteria(BaseModel):
    hard_consonants: list[str]
    soft_consonants: list[str]
    short_vowels: list[str]
    long_vowels: list[str]
    vowel_teams: list[str]
    digraphs: list[str]
    double_letters: list[str]
    prefix_digraphs: list[str]
    prefix_blends: list[str]
    suffix_blends: list[str]
    common_endings: list[str]
    allow_silent_e: bool
    allow_vc: bool
    allow_cvc: bool
    allow_cvce: bool
    allow_cvcvc: bool
    decodable_only: bool
    sight_words: list[str]

@app.post("/filter-words")
async def filter_words_api(criteria: Criteria):
    """API endpoint to filter words based on given criteria.

    Args:
        criteria (Criteria): The criteria object containing phoneme information.

    Returns:
        List[str]: A list of filtered words that match the criteria.

    Raises:
        HTTPException: If no words match the criteria.
    """
    input_data = criteria.model_dump()
    parsed_input = filter_words.parse_input(input_data)
    print(parsed_input)
    data = filter_words.load_data()
    filtered_df = filter_words.filter_words(data, parsed_input)
    result = list(filtered_df.word)
    if not result:
        raise HTTPException(status_code=404, detail="No words found matching the criteria.")
    return {"filtered_words": result}
