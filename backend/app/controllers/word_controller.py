from services.word_service import generate_words

def get_words(input_data: str):
    # Call the service layer to generate words based on input
    return generate_words(input_data)