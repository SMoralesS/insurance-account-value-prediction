import app.utils as utils

from app.pydantic_model import Payload
from fastapi import FastAPI

convertion_model = utils.read_model()

app = FastAPI()

@app.put("/predict_account_value")
def read_item(accounts_quotes: Payload):
    accounts_df = utils.preprocess_account_info(accounts_quotes)
    accounts_values = utils.predict_account_value(model=convertion_model, 
                                                  X=accounts_df) 
    return accounts_values