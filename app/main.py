class Distance:
    def __init__(self, distance: int) -> None:
        self.distance = distance
        self.km = distance
        return

    def __str__(self) -> str:
        return f"Distance: {self.distance} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.distance})"

    def __add__(*argc) -> "Distance":
        distance1 = argc[0].km if isinstance(argc[0], Distance) else argc[0]
        distance2 = argc[1].km if isinstance(argc[1], Distance) else argc[1]
        return Distance(distance1 + distance2)

    def __iadd__(*argc) -> "Distance":
        distance1 = argc[0].km if isinstance(argc[0], Distance) else argc[0]
        distance2 = argc[1].km if isinstance(argc[1], Distance) else argc[1]
        argc[0].distance = distance1 + distance2
        argc[0].km = distance1 + distance2
        return argc[0]

    def __mul__(*argc) -> "Distance":
        distance1 = argc[0].km if isinstance(argc[0], Distance) else argc[0]
        distance2 = argc[1]
        return Distance(distance1 * distance2)

    def __truediv__(*argc) -> "Distance":
        distance1 = argc[0].distance
        distance2 = argc[1]
        return Distance(round((distance1 / distance2), 2))

    def __lt__(*argc) -> bool:
        distance1 = argc[0].km if isinstance(argc[0], Distance) else argc[0]
        distance2 = argc[1].km if isinstance(argc[1], Distance) else argc[1]
        return distance1 < distance2

    def __gt__(*argc) -> bool:
        distance1 = argc[0].km if isinstance(argc[0], Distance) else argc[0]
        distance2 = argc[1].km if isinstance(argc[1], Distance) else argc[1]
        return distance1 > distance2

    def __eq__(*argc) -> bool:
        distance1 = argc[0].km if isinstance(argc[0], Distance) else argc[0]
        distance2 = argc[1].km if isinstance(argc[1], Distance) else argc[1]
        return distance1 == distance2

    def __le__(*argc) -> bool:
        distance1 = argc[0].km if isinstance(argc[0], Distance) else argc[0]
        distance2 = argc[1].km if isinstance(argc[1], Distance) else argc[1]
        return distance1 <= distance2

    def __ge__(*argc) -> bool:
        distance1 = argc[0].km if isinstance(argc[0], Distance) else argc[0]
        distance2 = argc[1].km if isinstance(argc[1], Distance) else argc[1]
        return distance1 >= distance2
