from __future__ import annotations
from typing import List, Union
from dataclasses import dataclass

@dataclass
class EmployeeDTO:
    first_name: str
    last_name: str
    work_email: str
    mobile_number: int
    managers: Union[List[str], List[EmployeeDTO]]

    @classmethod
    def from_dict(cls, args_dict: dict) -> EmployeeDTO:
        return cls(**args_dict)

if __name__ == "__main__":
    args_dict = {
        "first_name": "John",
        "last_name": "Doe",
        "work_email": "john@company.com",
        "mobile_number": 12345,
        "managers": ["Max", "Frodo"]
    }
    
    employee = EmployeeDTO.from_dict(args_dict)
    print(employee)
