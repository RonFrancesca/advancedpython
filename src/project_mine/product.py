from typing import Tuple

from pydantic import BaseModel, validator

from src.project.errors import CurrencyError

supported_currencies = ["dollar", "eur"]

class Product(BaseModel):

    name: str
    currency: str
    price: float

    @validator("currency")
    @classmethod
    def check_currency_is_supported(cls, value: str, values: dict) -> str:
        if value not in supported_currencies:
            msg = "The currency {value} is not supported by the system"
            raise CurrencyError(value, msg)
        return value

    def to_tuple(self) -> Tuple:
        """Convert Product object to a tuple of the type:

        Returns:
            Tuple: (name, currency, price).
        """
        return (self.name, self.currency, self.price)

