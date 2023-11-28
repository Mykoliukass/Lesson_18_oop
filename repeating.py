# # # from typing import Dict, List

# # # person = {
# # #     "name": "Vytautas",
# # #     "surname": "Sluckas",
# # #     "ip": "127.0.0.1",
# # #     "programming_language": "python",
# # #     "address": {"Street": "some_street", "House_number": "Some_house_number"},
# # #     "languages":["Lithuanian","English","Norvegian"]
# # # }
# # # person1 = {
# # #     "name": "Tomas",
# # #     "surname": "blablabla",
# # #     "ip": "127.0.0.1",
# # #     "programming_language": "python",
# # #     "address": {"Street": "some_street", "House_number": "Some_house_number"},
# # #     "languages":["Lithuanian","Russian","Spanish"]
# # # }
# # # people = [person, person1]

# # # def get_most_popular_language(people: List[Dict]) -> str:
# # #     language_counts = {}
# # #     for person in people:
# # #         for language in person["languages"]:
# # #             if language in language_counts:
# # #                 language_counts[language] += 1
# # #             else:
# # #                 language_counts[language] = 1
# # #     max_key, max_value = None, None
# # #     for key, value in language_counts.items():
# # #         if max_key == None or max_value < value:
# # #             max_value, max_key = value, key
# # #     return max_key
# # # print(get_most_popular_language(people))


# # # # def get_most_popular_language(people: List[Dict]) ->str:
# # # #     languages_dictionary = {}
# # # #     for person in people:
# # # #         languages = person.get("languages")
# # # #         for language in languages:
# # # #             languages_dictionary[language] = languages_dictionary.get(language, 0) + 1

# # # #     return max(languages_dictionary, key=languages_dictionary.get)

# # # # print(get_most_popular_language(people))

# # from typing import Dict

# # dict_one = {'a': 10, 'b': 20, 'c': 30}
# # dict_two = {'b': 200, 'd': 400}
# #      # if overwrite == True:
# #     #   update first dictioanry with the second one as with dictionary update method
# #     # else:
# #     # do not overwrite values from the first dictionary, only add new values from the second one.

# # def custom_dictionary_update(first_dictionary: Dict, second_dictionary: Dict, overwrite: bool = True) -> Dict:
# #     if overwrite:
# #         first_dictionary.update(second_dictionary)
# #     else:
# #         for key, value in second_dictionary.items():
# #             if key not in first_dictionary:
# #                 first_dictionary[key] = value
# #     return first_dictionary

# # print(custom_dictionary_update(dict_one, dict_two, False))


# # Create a function called calculate_area that takes in the length and width of a rectangle and returns its area.

# from typing import Union

# a = 5
# b = 6
# c = 7
# d = 8


# def calculate_area(
#     length: Union[int, float], width: Union[int, float]
# ) -> Union[int, float]:
#     return length * width


# print(calculate_area(a, b))
# print(calculate_area(a, c))


# def power_value(
#     base: Union[int, float], exponent: Union[int, float] = 2
# ) -> Union[int, float]:
#     return base**exponent


# print(power_value(7, 7))
# print(power_value(4))
# print(power_value(a, d))


# # Function with Variable Number of Arguments
# # Create a function called calculate_sum that takes in any number of arguments and returns their sum.
# def calculate_sum(*args: Union[int, float]) -> Union[int, float]:
#     return sum(args)


# print(calculate_sum(4, 5, 6, 7, 8, 9))
# print(calculate_sum(7, 5.4, 68, 3.2))
# print(calculate_sum(a, b, c, d))

# # Create a function called factorial that takes in a number n and computes its factorial using recursion.


# def factorial(n: int) -> int:
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)


# print(factorial(7))


# Generate a list of tuples where each tuple contains the index and the value of the element from the original list, but exclude elements with a value less than 10.
# from typing import List, Union, Tuple

# original_list = [5, 15, 8, 20, 12, 7, 18]


# def generate_list_of_tuples_with_index(
#     list_of_values: List[int],
# ) -> List[Tuple[int, int]]:
#     return [(index, value) for index, value in enumerate(list_of_values) if value >= 10]

# print(generate_list_of_tuples_with_index(original_list))

# Create a dictionary where keys are the names from one list and
# values are the corresponding ages from another list, but only for names that have lengths greater than 4.
# names = ['Alice', 'Bob', 'Charlie', 'David'] ages = [25, 30, 35, 40]

# from typing import List, Dict, Union

# names = ["Alice", "Bob", "Charlie", "David"]
# ages = [25, 30, 35, 40]

# result = {names[x]: ages[x] for x in range(len(names)) if len(names[x]) > 4}

# print(result)

# Create a function calculate_total_salary that takes in the base salary and
# additional bonuses (as keyword arguments) for an employee. The function
#  should consider a default bonus of 0 if none is provided. Use *args for handling multiple additional bonuses.

# from typing import Union

# def calculate_total_salary(base_salary: Union[int,float], *args, **kwargs) -> Union[int,float]:
#     return base_salary + sum(args) * sum(kwargs.values())


# print(calculate_total_salary(50000))
# print(calculate_total_salary(50000, 2000, 3000))
# print(
#     calculate_total_salary(
#         50000, 2000, 3000, health_insurance=1000, travel_allowance=1500
#     )
# )



# Create a function create_greeting that takes a person's 
# name as a mandatory argument, a message as a default parameter, 
# and any additional information as keyword arguments. The function should return a formatted greeting message.

def create_greeting(name: str, message: str = "Hello", **kwargs) -> str:
    if not kwargs:
        return f"{message}, {name}"
    else:
        additional_info = ", ".join([f"{key} is {value}" for key, value in kwargs.items()])
        return f"{message}, {name}, your {additional_info}"

print(create_greeting("Alice"))  # Test with mandatory argument only
print(create_greeting("Bob", "Hi"))  # Test with default parameter and mandatory argument
print(create_greeting("Charlie", age=30, location="New York"))  # Test with additional keyword arguments


# Create a function generate_shopping_list that accepts a title for the list, defaulting to "My Shopping List,"
#  and any number of items using *args. The function should return a formatted shopping list with the title and items.

def generate_shopping_list(title:str = "My Shopping List", *args) -> str:
    shopping_list = ", ".join([f"{arg}" for arg in args])
    return f"{title}: {shopping_list}"
print(generate_shopping_list("Lidl List", "Cookies", "Bread"))