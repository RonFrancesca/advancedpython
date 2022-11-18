from __future__ import annotations
from typing import Union, List, Dict, Any

from pydantic import BaseModel, validator

class EmployeeDTO(BaseModel):

    first_name: str
    last_name : str
    work_email: str
    mobile_number: int
    managers:  Union[List[str], List[EmployeeDTO]]
    full_name: str = None

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.full_name = f"{self.first_name} {self.last_name}"

    @validator("mobile_number")
    @classmethod
    def mobile_phone_6_digit(cls, value: int) -> int:
        min_number_digits = 6
        num_digits = len(str(value))
        if num_digits < min_number_digits:
            message = f"the mobile phone is not correctly formatted:  {value}. 6 digit needed."
            raise ValueError(message)
        else:
            return value

    @validator("work_email")
    @classmethod
    def check_email(cls, 
                    value: str, 
                    values: Dict[str, Any]) -> str:
        if values["first_name"].lower() not in(value):
            raise ValueError(f"The email does not contain the first name")
        else:
            return value

    @classmethod
    def from_dict(cls, args_dict: dict) -> EmployeeDTO:
        return cls(**args_dict)


if __name__ == "__main__":
    
    
    args_dict = {
        "first_name": "John",
        "last_name": "Doe",
        "work_email": "john@company.com",
        "mobile_number": 123456,
        "managers": ["Max", "Frodo"]
    }

    employee = EmployeeDTO.from_dict(args_dict)
    print(employee)