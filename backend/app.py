import utils
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse


app = FastAPI()

@app.get("/", response_class=HTMLResponse)

# # Predefined responses
# responses = {
#     "hello": "Hello there! Welcome to the local API.",
#     "goodbye": "Goodbye! Have a great day!",
#     "status": "API is running smoothly!",
#     "joke": "Why don't programmers like nature? It has too many bugs!"
# }

# @app.get("/")
# def read_root():
#     return {"message": "Welcome to the Local API! Try /response/{query}"}

# @app.get("/response/{query}")
# def get_response(query: str):
#     return {"response": responses.get(query.lower(), "I don't have a response for that.")}

# # Run with: uvicorn main:app --reload


# Initialize Streamlit app
st.title("Decodable Word Generator")
test = st.checkbox("test", key = "test")

letter_sets = [
    ['m', 's', 'r', 't', 'n', 'p', 'o', 'c', 'a', 'd'],
    ['g', 'f', 'b', 'k', 'i', 'l', 'h', 'w'],
    ['e', 'v', 'j', 'u', 'y', 'z', 'x', 'q'],
]

digraph_sets = [
    ['ck', 'sh', 'th', 'ch', 'wh', 'qu'],
]

blend_sets = [
    ['bl-', 'cl-', 'fl-', 'gl-', 'pl-', 'sl-'],
    ['br-', 'cr-', 'dr-', 'fr-', 'gr-', 'pr-', 'tr-'],
    ['sc-', 'shr-', 'sk-', 'sm-', 'sn-', 'sp-', 'squ-', 'st-', 'sw-'],
    ['ay', 'ow', 'oy'],
]

suffix_sets = [
    ['-lp', '-st', '-ct', '-pt', '-sk', '-lk', '-lf', '-xt', '-ft', '-nd', '-mp', '-st', '-lt', '-nch'],
    ['-ing', '-ang', '-ong', '-ung', '-ank', '-ink', '-onk', '-unk'],
    ['-ild', '-old', '-ind', '-olt', '-ost'],
]

other_sets = [
    ['wr-', 'kn-', 'ph-', 'gh-', 'gn-', '-mb', '-tch', '-dge']
]

vowel_team_sets = [
    list(utils.vowel_teams.values())
]

def change_all(letter_set:list, checkbox_key):
    for letter in letter_set:
        st.session_state[letter] = st.session_state[checkbox_key]

def any_selected(letter_set:list, checkbox_key):
    if not any([st.session_state[letter] for letter in letter_set]):
        st.session_state[checkbox_key] = False


## TODO: make sure I include everything else in the "other" or in the final set of blends

letter_checkboxes = {}
for i, letter_set in enumerate(letter_sets):
    for letter in letter_set:
        letter_checkboxes[letter] = st.checkbox(
            label = letter,
            value = True,
            key = letter,
            on_change = any_selected,
            args = (letter_sets[i])
        )


letter_set_checkboxes = [''] * len(letter_sets)
for i, letter_set in enumerate(letter_sets):
    letter_set_checkboxes[i] = st.checkbox(
        label = f"Letters ({i + 1}): {', '.join(letter_set)}",
        value = True,
        key = f'letters{i}',
        on_change = change_all,
        args = (letter_sets[i], f'letters{i}')
    )

# One-syllable, VC/CVC words 
## option to select every letter, or by group, or select/deselect whichever letters
## only short vowel sounds -- is this even necessary? But yes by default
## Option to include digraphs, select all or some
## Option to add in blends, select all or by group
## Option to add in ing/ang/ong, select all or by group

# Open/closed syllable types (ends in vowel)

# Multiple syllable, VC/CV pattern

# -ed

# CVCE (magic e)
# TODO: Should we consider CVCEs?


# Word frequency

