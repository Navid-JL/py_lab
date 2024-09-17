import pydantic
from typing import Literal


class Person(pydantic.BaseModel):
    name: str
    age: int
    email: str
    job: Literal["Farmer", "Statesman"]
    is_homeless: bool


def main() -> None:
    data = {
        "name": "Kate Gilbert",
        "age": 72,
        "email": "pag@gotso.bj",
        "job": "Farmer",
        "is_homeless": False
    }

    person = Person(**data)

    print(person)


if __name__ == "__main__":
    main()
