import word_decoder
import utils

decoded_dict = {}
for word in utils.simplified_cmudict:
    decoder = word_decoder.WordDecoder(word)
    decoded_dict[word] = decoder.decode()
        
        