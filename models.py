from pydantic import BaseModel, ConfigDict

class Products (BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id : int 
    name : str
    description : str
    price : float
    qty : int 