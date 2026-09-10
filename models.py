from pydantic import AliasChoices, BaseModel, ConfigDict, Field

class Products (BaseModel):
    model_config = ConfigDict(from_attributes=True, populate_by_name=True)

    id : int 
    name : str
    description : str
    price : float
    qty : int = Field(
        validation_alias=AliasChoices("qty", "quantity"),
        serialization_alias="quantity",
    )

    @property
    def quantity(self):
        return self.qty
