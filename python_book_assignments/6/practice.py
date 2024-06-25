from typing import Dict, Union, TypedDict

PersonType = TypedDict(
                'PersonType',
                    {
                        "first_name": str,
                        "last_name": str,
                        "age": str,
                        "city": str,
                    }
                )

person1: PersonType = {
    "first_name": "Jawwad",
    "last_name": "Ahmad",
    "age": 26,
    "city": "Bahawalnagar"
}

person2: PersonType = {
    "first_name": "Sufyan",
    "last_name": "Farooq",
    "age": 26,
    "city": "Lahore"
}

person3: PersonType = {
    "first_name": "Hammad",
    "last_name": "Ahmad",
    "age": 26,
    "city": "Karachi"
}

print(person1, person2, person3)