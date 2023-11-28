# Create the instance attributes fullname and email in the Employee class. Given a person's first and last names:

# Form the fullname by simply joining the first and last name together, separated by a space.
# Form the email by joining the first and last name together with a . in between, and follow it with @company.com at the end. Make sure the entire email is in lowercase.

class Employee:
    def __init__(self, name: str, surname: str) -> None:
        self.name = name
        self.surname = surname

    def get_fullname(self) -> str:
        return self.name + " " + self.surname

    def form_email(self) -> str:
        email = self.name.lower() + "." + self.surname.lower() + "@company.com"
        return email

employee = Employee(name="Mykolas", surname="Jerutis")
print(employee.form_email())

