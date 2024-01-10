# TODO Написать 3 класса с документацией и аннотацией типов
from    typing import Union


class Company:
    def __init__(self, number_of_stocks: int, stock_cost: Union[int,float]):
        """
        Создание и подготовка к работе объекта "Youtube"

        :param number_of_stocks: количество акций
        :param stock_cost: Стоимость одной акции в $

        Примеры:
        >>> сompany = Company(500, 3555.5)  # инициализация экземпляра класса
        """
        # Атрибутам присваиваются значения аргументов конструктора объекта
        if not isinstance(number_of_stocks, int):
            raise TypeError("Количество акций должно быть типа int")
        if not isinstance(stock_cost, (int, float)):
            raise TypeError("Стоимость акции должна быть типа int или float")
        self.number_of_stocks = number_of_stocks
        self.stock_cost = stock_cost
        self.market_cap = stock_cost * number_of_stocks


    def method_market_cap(self, market_cap: Union[int,float]):
        self.market_cap = market_cap
        """
        Функция которая вычисляет рыночную капитализацию компании

        :return: Рыночная стоимость компании

        Примеры:
        >>> сompany = Company(500, 0)
        >>> сompany.method_market_cap()
        """
    def method_multiply(self, stock_cost: Union[int,float]):
        """
        Функция которая умножает стоимость акции на определённое число

        :return: Новая стоимость акции

        Примеры:
        >>> сompany = Company(500, 3.5)
        >>> сompany.method_multiply(1.5)
        """

class Table:
    """
    Создание и подготовка к работе объекта "table"

    :param legs: Количество ножек у стола (должно превышать 3шт)
    :param surface: Площадь поверхности стола (больше 0)

    Примеры:
    >>> table = Table(500, 3555.5)  # инициализация экземпляра класса
    """
    def __init__(self, legs: int, surface: Union[int,float]):
        # Атрибутам присваиваются значения аргументов конструктора объекта
        if not isinstance(legs, int):
            raise TypeError("Количество ножек стола должно быть типа int или float")
        if not isinstance(surface, (int, float)):
            raise TypeError("Площадь поверхности стола должны быть типа int или float")
        if not surface > 0:
            raise TypeError("Площадь поверхности стола и число ножек должны быть больше 0")
        if not legs >= 3:
            raise TypeError("Площадь поверхности стола и число ножек должны быть больше 0")
        self.legs = legs
        self.surface = surface

    def method_multiply_surface(self, surface: Union[int,float]):
        self.surface = surface

    """
            Функция которая увеличивает поверхность стола в определённое количество раз

            :return: Новое площадь стола

            Примеры:
            >>> table = Table(500, 3.5)
            >>> table.method_multiply_surface()
            """
    def method_ad_legs(self, legs: int):
        self.legs = legs
        """
        Функция которая добавляет ещё одну ножку столу

        :return: Новое число ножек у стола

        Примеры:
        >>> table = Table(500, 3.5)
        >>> table.method_ad_legs()
        """

class PC:
    """
        Создание и подготовка к работе объекта "table"

        :param memory: Память компьютера (должно превышать 0)
        :param processor: Процессор пк (str)
        :param graphic_card: Видеокарта (str)

        Примеры:
        >>> pc = PC(3.5, "Intelcore i5","GeforceGtx 960")  # инициализация экземпляра класса
        """
    def __init__(self, memory: Union[int,float], processor: str, graphic_card: str):
        # Атрибутам присваиваются значения аргументов конструктора объекта
        if not isinstance(memory, (int,float)):
            raise TypeError("Память компьютера должна быть типа int или float")
        if not isinstance(processor, (str)):
            raise TypeError("Процессор должен быть типа str")
        if not isinstance(graphic_card, (str)):
            raise TypeError("Видеокарта должен быть типа str")
        if not memory > 0:
            raise TypeError("Память компьютера должна быть больше 0")
        self.memory = memory
        self.processor = processor
        self.graphic_card = graphic_card

    def memory_add(self, memory: Union[int,float]):

        """
        Функция которая увеличивает память компьютера

        :return: Добавляет

        Примеры:
        >>> pc = PC(3.5, "Old processor", "old processor")
        >>> pc.memory_add(3)
        """
    def processor_change(self, processor: str):
        """
        Функция которая заменяет процессор на новый

        :return: Новый процессор

        Примеры:
        >>> pc = PC(3.5, "Old processor", "old processor")
        >>> pc.processor_change("new processor")
        """

    def graphic_card_change(self, graphic_card: str):
        """
        Функция которая заменяет видеокарту на новую

        :return: Новая видеокарта

        Примеры:
        >>> pc = PC(3.5, "Old processor", "old processor")
        >>> pc.graphic_card_change("New card")
        """


if __name__ == "__main__":
    import doctest


    doctest.testmod()  # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
