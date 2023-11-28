# # class Employee:
# #     def __init__(self, name: str, surname: str, age: int) -> None:
# #         self.name = name
# #         self.surname = surname
# #         self.age = age

# #     def get_employees_info(self) -> str:
# #         return f"{self.name} {self.surname} is {self.age} years old"


# # class Engineers(Employee):
# #     def __init__(self, position: str, name: str, surname: str, age: int):
# #         super().__init__(name=name, surname=surname, age=age)
# #         self.position = position

# #     def get_engineer_position(self) -> str:
# #         return self.position


# # engineers = Engineers(
# #     position="Senior Developer", name="Mindaugas", surname="Rudzevicius", age=32
# # )
# # print(engineers.get_employees_info())


# class Animal:
#     def __init__(self, name: str, latin_name: str, discovered_by: str) -> None:
#         self.name = name
#         self.latin_name = latin_name
#         self.discovered_by = discovered_by

#     def get_animal_info(self) -> str:
#         return f"{self.name} with latin name '{self.latin_name}' was discovered by {self.discovered_by}"


# class Mammals(Animal):
#     def __init__(
#         self,
#         type_of_birth: str,
#         feet_type: str,
#         name: str,
#         latin_name: str,
#         discovered_by: str,
#     ):
#         super().__init__(name=name, latin_name=latin_name, discovered_by=discovered_by)
#         self.type_of_birth = type_of_birth
#         self.feet_type = feet_type

#     def get_type_of_birth(self) -> str:
#         return f"{self.type_of_birth}"


# platypus = Mammals(
#     type_of_birth="lays eggs",
#     feet_type="webbed feet",
#     name="Platypus",
#     latin_name="Ornithorhynchus anatinus",
#     discovered_by="John Doe",
# )

# print(platypus.get_animal_info())
# print(platypus.get_type_of_birth())


# class Star:
#     def __init__(self, name: str, constellation: str, discovered_by: str) -> None:
#         self.name = name
#         self.constellation = constellation
#         self.discovered_by = discovered_by

#     def get_star_info(self) -> str:
#         return f"{self.name} in the constellation {self.constellation} was discovered by {self.discovered_by}"


# class Sun(Star):
#     def __init__(
#         self,
#         temperature: int,
#         luminosity: float,
#         name: str,
#         constellation: str,
#         discovered_by: str,
#     ):
#         super().__init__(
#             name=name, constellation=constellation, discovered_by=discovered_by
#         )
#         self.temperature = temperature
#         self.luminosity = luminosity

#     def get_sun_info(self) -> str:
#         return f"The Sun, named {self.name}, is the star at the center of our Solar System. It was discovered by {self.discovered_by}."


# our_sun = Sun(
#     temperature=5778,
#     luminosity=3.828e26,
#     name="Sol",
#     constellation="Sollar System",
#     discovered_by="Humans",
# )

# print(our_sun.get_star_info())
# print(our_sun.get_sun_info())


# Create a base class called Book with attributes like title, author, and publication_year. This class should have a method called display_info that prints basic information about the book.

# Create two subclasses of Book called Fiction and NonFiction. Add an additional attribute to each subclass,
#  such as genre for Fiction and subject for NonFiction.
# Create two more subclasses, Mystery and History, that inherit from Fiction and NonFiction,
# respectively. Add specific attributes to each of these subclasses
#  (e.g., detective for Mystery and time_period for History).
# Add in each sub class methods to retreive provided data.


class Book:
    def __init__(self, title: str, author: str, publication_year: int) -> None:
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def display_info(self) -> str:
        return f"{self.title} was written by {self.author} and published in {self.publication_year} year. "


class Fiction(Book):
    def __init__(
        self, genre: str, title: str, author: str, publication_year: int
    ) -> None:
        super().__init__(title=title, author=author, publication_year=publication_year)
        self.genre = genre

    def get_genre(self) -> str:
        return self.genre


class NonFiction(Book):
    def __init__(
        self, subject: str, title: str, author: str, publication_year: int
    ) -> None:
        super().__init__(title=title, author=author, publication_year=publication_year)
        self.subject = subject

    def get_subject(self) -> str:
        return self.subject


class Mystery(Fiction):
    def __init__(
        self, detective: str, genre: str, title: str, author: str, publication_year: int
    ) -> None:
        super().__init__(
            genre=genre, title=title, author=author, publication_year=publication_year
        )
        self.detective = detective

    def get_detective(self) -> str:
        return self.detective


class History(NonFiction):
    def __init__(
        self,
        time_period: str,
        subject: str,
        title: str,
        author: str,
        publication_year: int,
    ) -> None:
        super().__init__(
            subject=subject,
            title=title,
            author=author,
            publication_year=publication_year,
        )
        self.time_period = time_period

    def get_time_period(self) -> str:
        return self.time_period


da_vinci_code = Mystery(
    detective="Robert Langdon",
    genre="Mystery",
    title="The Da Vinci Code",
    author="Dan Brown",
    publication_year=2003,
)
mein_kampf = History(
    time_period="Interwar Period",
    subject="Political History",
    title="Mein Kampf",
    author="Adolf Hitler",
    publication_year=1925,
)

print(da_vinci_code.display_info())
print(da_vinci_code.get_genre())
print(da_vinci_code.get_detective())

print(mein_kampf.display_info())
print(mein_kampf.get_subject())
print(mein_kampf.get_time_period())
