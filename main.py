if __name__ == "__main__":
class Vehicle:
    def __init__(self, brand: str, model: str, year: int):
        """
        Базовый класс для транспортных средств.

        :param brand: Марка транспортного средства.
        :param model: Модель транспортного средства.
        :param year: Год выпуска.
        """
        self.brand = brand
        self.model = model
        self.year = year

    def start_engine(self):
        """
        Метод для запуска двигателя.

        :return: Результат запуска двигателя.
        """
        return f"{self.brand} {self.model} двигатель запущен."

    def move(self, destination: str):
        """
        Метод для перемещения к указанному месту.

        :param destination: Место, куда необходимо переместить транспорт.
        :return: Результат перемещения.
        """
        return f"{self.brand} {self.model} движется в сторону {destination}."

    def __str__(self) -> str:
        return f"{self.year} {self.brand} {self.model}"

    def __repr__(self) -> str:
        return f"Vehicle(brand={self.brand}, model={self.model}, year={self.year})"


class Car(Vehicle):
    def __init__(self, brand: str, model: str, year: int, num_doors: int):
        """
        Дочерний класс для легковых автомобилей.

        :param brand: Марка автомобиля.
        :param model: Модель автомобиля.
        :param year: Год выпуска.
        :param num_doors: Количество дверей.
        """
        super().__init__(brand, model, year)
        self.num_doors = num_doors

    def start_engine(self):
        """
        Перегруженный метод для запуска двигателя легкового автомобиля.

        :return: Результат запуска двигателя.
        """
        return f"{self.num_doors}-дверный {super().start_engine()}"

    def move(self, destination: str):
        """
        Перегруженный метод для перемещения легкового автомобиля.

        :param destination: Место, куда необходимо переместить автомобиль.
        :return: Результат перемещения.
        """
        return f"{self.num_doors}-дверный {super().move(destination)} (легковой автомобиль)."



    pass
