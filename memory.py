from pympler.asizeof import asizeof


class PointsWithoutSlots:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


class Points:
    __slots__ = ('x', 'y')

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


def main() -> None:
    points_without_slots = [PointsWithoutSlots(i, i) for i in range(1000)]
    points_with_slots = [Points(i, i) for i in range(1000)]

    print(
        f"Total memory (without __slots__): {asizeof(points_without_slots, stats=1)}")
    print(
        f"Total memory (with __slots__): {asizeof(points_with_slots, stats=1)}")


if __name__ == "__main__":
    main()
