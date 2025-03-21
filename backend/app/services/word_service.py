# import word_decoder
import word
import utils
import pandas as pd
import json

def generate_words(input_data:str):
    criteria = parse_input(input_data)
    all_features = []
    for wrd in utils.simplified_cmudict:
        w = word.Word(wrd)
        all_features.append(w.features)
    df = pd.DataFrame(all_features)

def parse_input(input_data:str):
    input_json = json.loads(input_data)
    input_json['letters'] = np.array()
    criteria = {
        "decodable_only" : input_json['']
    }
    return criteria

w = word.Word("stake")
w.features

decoded_dict = {}
for word in utils.simplified_cmudict:
    decoder = word_decoder.WordDecoder(word)
    decoded_dict[word] = decoder.decode()
        
        