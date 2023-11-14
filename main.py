# Create a class which represents your family. Class should take your mom,dad,sister ,broters names and ages.
# Create instance methods that would return :
#  - All names and ages as dict data structure
#  - The sum of all ages
#  - Would print the names depending on your relatives(sister,brother etc)
#  - Would list all family members from youngest to oldest (Choose return type by yourself.)

import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename='data.log',
    filemode='a',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%d/%m/%Y %H:%M:%S'
)

class Family:
    def __init__(self, mom_name, mom_age, dad_name, dad_age, sister_name, sister_age, brother_name, brother_age):
        self.mom = {"name": mom_name, "age": mom_age}
        self.dad = {"name": dad_name, "age": dad_age}
        self.sister = {"name": sister_name, "age": sister_age}
        self.brother = {"name": brother_name, "age": brother_age}

    def get_all_names_and_ages(self):
        try:
            all_names_and_ages = {
                self.mom["name"]: self.mom["age"],
                self.dad["name"]: self.dad["age"],
                self.sister["name"]: self.sister["age"],
                self.brother["name"]: self.brother["age"]
            }
            return all_names_and_ages
        except Exception as e:
            logging.info(f"Error occured in get_all_names_and_ages: {e}")
            return all_names_and_ages = {}
    def get_sum_of_ages(self):
        try:
            sum_of_ages = self.mom["age"] + self.dad["age"] + self.sister["age"] + self.brother["age"]
            return sum_of_ages
        except Exception as e:
            logging.info(f"Error occured in get_sum_of_ages: {e}")
            return sum_of_ages = 0

    def print_names(self, relative:str) -> None:
        try:
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
        except Exception as e:
            logging.info(f"Error occured in print_names: {e}")
            
    def list_family_members_by_age(self):
        family_members = [self.mom, self.dad, self.sister, self.brother]
        sorted_members = sorted(family_members, key=lambda member: member["age"])
        return [member["name"] for member in sorted_members]

my_family = Family("Saule", 45, "Saulius", 50, "Simona", 20, "Kurmis", 25)

print(my_family.get_all_names_and_ages())
print(f"Sum of all ages: {my_family.get_sum_of_ages()}")
my_family.print_names("sister")
print(my_family.list_family_members_by_age())

