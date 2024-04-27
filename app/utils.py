import pandas as pd
import datetime
from app.pydantic_model import Payload
from dython.nominal import identify_nominal_columns
from sentence_transformers import SentenceTransformer 
from catboost import CatBoostClassifier

def read_model(
    model_path: str = './app/static_data/conversion_model.cbm'
    ) -> CatBoostClassifier:
    convertion_model = CatBoostClassifier()
    convertion_model.load_model(model_path, format='cbm')
    return convertion_model


def preprocess_account_info(
    accounts_quotes: Payload, 
    sentence_model_path='bert-base-nli-mean-tokens') -> pd.DataFrame:
    accounts_dict_list = [account.dict() for account in accounts_quotes.accounts]
    accounts_df = pd.DataFrame(accounts_dict_list)
    quotes_dict_list = [quote.dict() for quote in accounts_quotes.quotes]
    quotes_df = pd.DataFrame(quotes_dict_list)
    accounts_quotes_df = accounts_df.merge(quotes_df, how='left', on='account_uuid')
    nominal_columns = identify_nominal_columns(accounts_quotes_df)
    nominal_columns.remove('account_uuid')

    for col in nominal_columns:
        accounts_quotes_df[col] = accounts_quotes_df[col].fillna('nan')
    
    sentence_model = SentenceTransformer(sentence_model_path, truncate_dim=5)
    encoded_data_subindustry = sentence_model.encode(
        accounts_quotes_df.loc[
            ~accounts_quotes_df['subindustry'].isna(), 
            'subindustry'].values, 
        show_progress_bar=True
    )
    
    accounts_quotes_df[[f'subindustry_enc_{i}' for i in range(5)]] = 0., 0., 0., 0., 0.
    accounts_quotes_df.loc[
        ~accounts_quotes_df['subindustry'].isna(), 
        [f'subindustry_enc_{i}' for i in range(5)]] = encoded_data_subindustry
    accounts_quotes_df['years_in_business'] = datetime.datetime.now().year - \
                                              accounts_quotes_df['year_established']
    accounts_quotes_df = accounts_quotes_df.drop('year_established', axis=1)
    return accounts_quotes_df

def predict_account_value(model: CatBoostClassifier, X: list[dict]):
    X = pd.DataFrame(X)
    X_accounts = X.groupby('account_uuid')
    account_values = []
    for account, account_df in X_accounts:
        account_df = account_df.loc[:, [
            col 
            for col in X.columns 
            if col not in ['account_uuid', 'convert']
            ]]
        premium_values = account_df['premium']
        if account == '00143506-a4ba9-6d4d-558b4-28e36e9ee4':
            print(account_df.to_dict())
        convert_probabilities = model.predict_proba(account_df)[:, 1]
        expected_values = premium_values * convert_probabilities
        account_value = sum(expected_values, 0)
        account_values.append({
            'account_uuid': account,
            'account_value': account_value,
        })
    return account_values