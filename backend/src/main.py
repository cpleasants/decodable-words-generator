import filter_words
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

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

@app.post("/filter-words")
async def filter_words_api(criteria: Criteria):
    input_data = criteria.model_dump()
    parsed_input = filter_words.parse_input(input_data)
    data = filter_words.load_data()
    filtered_df = filter_words.filter_words(data, parsed_input)
    result = list(filtered_df.word)
    if not result:
        raise HTTPException(status_code=404, detail="No words found matching the criteria.")
    return {"filtered_words": result}
