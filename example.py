# class Calculator:
#     def __init__(self) -> None:
#         print("Kazkas")

#     def add_two_numbers(self, first_num:int,second_num:int) -> int:
#         return first_num + second_num

#     def divide_two_numbers(self, first_num:int,second_num:int) -> int:
#         return first_num / second_num

#     def multiply_two_numbers(self, first_num:int,second_num:int) -> int:
#         return first_num * second_num

#     def substract_two_numbers(self, first_num:int,second_num:int) -> int:
#         return first_num - second_num

# calculator = Calculator()

# # print(calculator.add_two_numbers(7,6))
# # print(calculator.divide_two_numbers(7,6))
# # print(calculator.multiply_two_numbers)

class People:
    def __init__(self, name:str, surname:str) -> None:
        self.name = name 
        self.surname = surname
    def get_name_and_surname(self) -> str:
        return self.name + " " + self.surname

person = People(name = "Silveris", surname = "Kazkas")

print(person.name)
print(person.get_name_and_surname())