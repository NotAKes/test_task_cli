from dataclasses import dataclass
from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def __str__(self) -> str:
        pass


@dataclass
class Point(Shape):
    x: float
    y: float

    def __str__(self) -> str:
        return f'Точка с координатами ({self.x}, {self.y})'


@dataclass
class Line(Shape):
    start: Point
    end: Point

    def __str__(self) -> str:
        return f'Отрезок с координатами начала ({self.start.x}, {self.start.y}) и конца ({self.end.x}, {self.end.y})'


@dataclass
class Circle(Shape):
    center: Point
    radius: float

    def __str__(self) -> str:
        return f'Круг с радиусом {self.radius} и координатами центра ({self.center.x}, {self.center.y})'


@dataclass
class Square(Shape):
    bottom_left: Point
    side: float

    def __str__(self) -> str:
        return f'Квадрат с координатами нижнего левого угла ({self.bottom_left.x}, {self.bottom_left.y}) и длиной стороны {self.side}'
