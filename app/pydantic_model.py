from typing import Union, List
from pydantic import BaseModel

class Account(BaseModel):
    account_uuid: str = "093c3652-16ab8-caf4-8f940-ad7e3ee4e9"
    state: Union[str, None] = "VA"
    industry: Union[str, None] = "Other Services"
    subindustry: Union[str, None] = "Appliance Repair and Maintenance"
    year_established: Union[int, None] = 2018
    annual_revenue: Union[float, None] = 8000
    total_payroll: Union[float, None] = None
    business_structure: Union[str, None] = "Individual"
    num_employees: Union[int, None] = None

class Quotes(BaseModel):
    account_uuid: str = "093c3652-16ab8-caf4-8f940-ad7e3ee4e9"
    product: Union[str, None] = "Business_Owners_Policy_BOP"
    premium: float = 501
    carrier_id: Union[int, None] = 60

class Payload(BaseModel):
    accounts: List[Account]
    quotes: List[Quotes]