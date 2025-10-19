from __future__ import annotations


class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int | float) -> Distance:
        distance1 = self.km
        distance2 = other.km if isinstance(other, Distance) else other
        return Distance(distance1 + distance2)

    def __iadd__(self, other: Distance | int | float) -> Distance:
        distance1 = self.km
        distance2 = other.km if isinstance(other, Distance) else other
        self.km = distance1 + distance2
        return self

    def __mul__(self, other: Distance | int | float) -> Distance:
        distance1 = self.km
        distance2 = other
        return Distance(distance1 * distance2)

    def __truediv__(self, other: Distance | int | float) -> Distance:
        distance1 = self.km
        distance2 = other
        return Distance(round((distance1 / distance2), 2))

    def __lt__(self, other: Distance | int | float) -> bool:
        distance1 = self.km
        distance2 = other
        return distance1 < distance2

    def __gt__(self, other: Distance | int | float) -> bool:
        distance1 = self.km
        distance2 = other
        return distance1 > distance2

    def __eq__(self, other: Distance | int | float) -> bool:
        distance1 = self.km
        distance2 = other
        return distance1 == distance2

    def __le__(self, other: Distance | int | float) -> bool:
        distance1 = self.km
        distance2 = other
        return distance1 <= distance2

    def __ge__(self, other: Distance | int | float) -> bool:
        distance1 = self.km
        distance2 = other
        return distance1 >= distance2
