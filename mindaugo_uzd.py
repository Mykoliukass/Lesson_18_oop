# Create a program that user enters name, surname, email_provider, age (example: Thom, Nelson, gmail, 12 )
# Program should list options to choose:
#  - Generate some email variants from all data provided
#  - Get year of birth
#  - Return all personal info (including generic email and year of birth)


# Must use class for dealing with data. Error handling, types. Input should be invoked as a script (if __name__ ....)
class Person:
    __CURRENT_YEAR: int = 2023

    def __init__(self, name: str, surname: str, email_provider: str, age: int) -> None:
        self.name = name
        self.surname = surname
        self.email_provider = email_provider
        self.age = age

    def email_generator(self) -> str:
        return f"Some email variants for you:\n{self.name.lower()}.{self.surname.lower()}@{self.email_provider.lower()}\n{self.surname.lower()}.{self.age}.{self.name.lower()}@{self.email_provider.lower()}"

    def get_year_of_birth(self) -> int:
        return self.__CURRENT_YEAR - self.age

    def get_personal_info(self) -> str:
        return f"Name: {self.name}\nSurname: {self.surname}\nEmail: {self.name.lower()}.{self.surname.lower()}@{self.email_provider.lower()}\nAge: {self.age}"


def main_menu(person_info: str) -> None:
    person_info_list = person_info.replace(" ", "").split(",")
    name = person_info_list[0]
    surname = person_info_list[1]
    email_provider = person_info_list[2]
    age = int(person_info_list[3])

    person = Person(
        name=name,
        surname=surname,
        email_provider=email_provider,
        age=age,
    )
    menu_entries: str = "\n1. Generate some email variants\n2. Get year of birth\n3. Return all personal info\n4. End program.\nPlease enter number of your selection: "

    while True:
        menu_select: str = input(menu_entries)
        print()

        if menu_select.isnumeric() == True:
            if menu_select == "1":
                print(person.email_generator())
            elif menu_select == "2":
                print(person.get_year_of_birth())
            elif menu_select == "3":
                print(person.get_personal_info())
            elif menu_select == "4":
                print("Bye")
                break
            else:
                print("There is no such selection.")
        else:
            print(
                "Please enter number from list provided without any symbols and spaces."
            )


if __name__ == "__main__":
    person_info: str = input(
        "Enter name, surname, email_provider, age (example: Thom, Nelson, gmail, 12 ): "
    )

    try:
        main_menu(person_info)
    except Exception as err:
        print(f"You've got an {err} error.")