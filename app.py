# 1. Library imports
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
import mspresidio

class TextModel(BaseModel):
    text: str

# 2. Create the app object
app = FastAPI()


@app.post('/anonymize', response_model=str,tags=['anonymize'])
def tokenize(text : str):
    anon = mspresidio.anonymize(text)
    anon = mspresidio.hide_dates(anon, '<DATE>')
    anon = mspresidio.hide_names(anon, '<PERSON>')
    return anon

# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)