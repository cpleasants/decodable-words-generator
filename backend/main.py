from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def form():
    start = """
<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>FastAPI Checkbox Form</title>
        <style>
            .checkbox-group {
                display: flex;
                gap: 10px;
                flex-wrap: wrap;
            }
            .checkbox-group label {
                display: flex;
                align-items: center;
                gap: 5px;
                cursor: pointer;
                padding: 5px 10px;
                border: 1px solid #ccc;
                border-radius: 5px;
                background: #f8f8f8;
                transition: background 0.3s;
            }
            .checkbox-group input[type="checkbox"] {
                display: none; /* Hide default checkbox */
            }
            .checkbox-group label:hover {
                background: #e0e0e0;
            }
            .checkbox-group input[type="checkbox"]:checked + label {
                background: #007bff;
                color: white;
                border-color: #007bff;
            }
        </style>
    </head>
    <body>
        <h2>Select the letters</h2>
        <form action="/submit/" method="post">
            <fieldset>
                <legend>Choose your interests:</legend>
"""
    end = """
                </fieldset>
                <br>
                <button type="submit">Submit</button>
            </form>
        </body>
        </html>
    """

    dv = generate_section_of_checkboxes(['a', 'b', 'c'])
    return f"""
    {start}
        {dv}
    {end}
    """

@app.post("/submit/")
async def submit_form(username: str = Form(...), password: str = Form(...)): # Form(...) extracts form data from POST requests.
    return {"username": username, "password": password}

def generate_section_of_checkboxes(letters:list) -> str:
    div = '<div class="checkbox-group">\n'
    for letter in letters:
        inpt = f"""<input type="checkbox" id="{letter}" name="{', '.join(letters)}" value="{letter}">\n"""
        lbl = f"""<label for="{letter}">{letter}</label><br>\n"""
        div += inpt
        div += lbl
    div += '</div>'
    return div