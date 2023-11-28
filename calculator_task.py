import logging
from typing import List, Union

logging.basicConfig(
    level=logging.ERROR,
    filename='calculator_data.log',
    filemode='a',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%d/%m/%Y %H:%M:%S'
)

class Calculator:
    def get_users_input(self) -> List[Union[int, float]]:
        while True:
            try:
                input_str = input("Please provide two numbers separated by a comma: ")
                logging.info(f"User input: {input_str}")

                user_values = [float(value.strip()) for value in input_str.split(",")]

                if len(user_values) != 2:
                    raise ValueError("Input should be two numbers separated by a comma.")

                return user_values

            except ValueError as e:
                logging.error(f"Error occurred in getting users input: {e}. Please try again.")

    def add_two_numbers(self) -> Union[float, int]:
        user_input = self.get_users_input()
        return sum(user_input)

    def subtract_two_numbers(self) -> Union[float, int]:
        user_input = self.get_users_input()
        return user_input[0] - user_input[1]

    def multiply_two_numbers(self) -> Union[float, int]:
        user_input = self.get_users_input()
        return user_input[0] * user_input[1]

    def divide_two_numbers(self) -> Union[float, int]:
        while True:
            try:
                user_input = self.get_users_input()
                result = user_input[0] / user_input[1]
                return result
            except ZeroDivisionError as e:
                logging.error(f"Error in divide_two_numbers: {e}")
                print("Cannot divide by zero. Please try again.")

calc = Calculator()

print("Adding two numbers:", calc.add_two_numbers())
print("Subtracting two numbers:", calc.subtract_two_numbers())
print("Multiplying two numbers:", calc.multiply_two_numbers())
print("Dividing two numbers:", calc.divide_two_numbers())







# from typing import Type

# class Country:
#     def compare_pd(self, other_country: "Country") -> str:
#         country.area ir t.t.

# result = usa.compare_pd(china)
# print(result)
