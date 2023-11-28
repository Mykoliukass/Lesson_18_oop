# create a class, which representst a car.


class Car:
    def __init__(
        self, model: str, date_of_manufacturing: int, engine_capacity: float) -> None:
        self.model = model
        self.date_of_manufacturing = date_of_manufacturing
        self.engine_capacity = engine_capacity

    def get_car_name(self) -> str:
        return self.model

car = Car(model="Mercedes", date_of_manufacturing=2014, engine_capacity=2.3)

print(car.get_car_name())
