from __future__ import annotations
from mimetypes import init
from traceback import print_tb
from typing import Union, List
from dataclasses import dataclass, field


@dataclass
class EmployeeDTO:
    first_name: str
    last_name: str
    work_email: str
    mobile_number: int
    managers: Union[List[str], List[EmployeeDTO]]
    complete_name: str = field(init=False)

    # the post init will allow me to post initialize something, but automatically without me needed to do it
    def __post_init__(self)-> None:
        self.complete_name = f"{self.first_name} {self.last_name}"
    

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
    print(employee.complete_name)