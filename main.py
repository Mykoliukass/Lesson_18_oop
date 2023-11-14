# Create a class which represents your family. Class should take your mom,dad,sister ,broters names and ages.
# Create instance methods that would return :
#  - All names and ages as dict data structure
#  - The sum of all ages
#  - Would print the names depending on your relatives(sister,brother etc)
#  - Would list all family members from youngest to oldest (Choose return type by yourself.)
# Keys should be - dad, mom, sister, brother. 

import logging
from typing import Dict, Union, List

logging.basicConfig(
    level=logging.ERROR,
    filename='family_data.log',
    filemode='a',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%d/%m/%Y %H:%M:%S'
)

class Family:
    def __init__(
        self,
        mom_name: str,
        mom_age: int,
        dad_name: str,
        dad_age: int,
        sister_name: str,
        sister_age: int,
        brother_name: str,
        brother_age: int) -> None:
        self.mom = {"name": mom_name, "age": mom_age}
        self.dad = {"name": dad_name, "age": dad_age}
        self.sister = {"name": sister_name, "age": sister_age}
        self.brother = {"name": brother_name, "age": brother_age}

    def get_all_names_and_ages(self) -> Dict[str, Dict[str, Union[str, int]]]:
        all_names_and_ages: Dict[str, Dict[str, Union[str, int]]] = {
            "mother": self.mom,
            "father": self.dad,
            "sister": self.sister,
            "brother": self.brother
        }
        return all_names_and_ages

    def get_sum_of_ages(self) -> int:
        try:
            sum_of_ages = self.mom["age"] + self.dad["age"] + self.sister["age"] + self.brother["age"]
            return sum_of_ages
        except Exception as e:
            logging.error(f"Error occurred in get_sum_of_ages: {e}")

    def print_names(self, relative: str) -> None:
        if relative.lower() == "mom":
            print(f"Mom's name is {self.mom['name']}")
        elif relative.lower() == "dad":
            print(f"Dad's name is {self.dad['name']}")
        elif relative.lower() == "sister":
            print(f"Sister's name is {self.sister['name']}")
        elif relative.lower() == "brother":
            print(f"Brother's name is {self.brother['name']}")
        else:
            print("Invalid relative name")

    def get_age(self, member):
        return member["age"]

    def list_family_members_by_age(self) -> List[str]:
        try:
            family_members = [self.mom, self.dad, self.sister, self.brother]
            sorted_members = sorted(family_members, key=self.get_age)
            return [member["name"] for member in sorted_members]
        except Exception as e:
            logging.error(f"Error occurred in list_family_members_by_age: {e}")
            return []

my_family = Family("Saule", 45, "Saulius", 50, "Simona", 20, "Silvestras", 25)

print(my_family.get_all_names_and_ages())
print(f"Sum of all ages: {my_family.get_sum_of_ages()}")
my_family.print_names("sister")
print(my_family.list_family_members_by_age())

