import sys
import typing
from functools import reduce

from part_one import get_priority, read_rucksacks


def find_badge(rucksacks: list[str]) -> str:
    return reduce(set.intersection, map(set, rucksacks)).pop()


def group(
    rucksacks: typing.Generator[str, None, None], n: int
) -> typing.Generator[list[str], None, None]:
    accumulator = []
    for rucksack in rucksacks:
        accumulator.append(rucksack)
        if len(accumulator) == n:
            yield accumulator
            accumulator = []


def main(input_path: str):
    total_priorities = sum(
        get_priority(find_badge(rucksacks))
        for rucksacks in group(read_rucksacks(input_path), 3)
    )
    print(total_priorities)


if __name__ == "__main__":
    main(sys.argv[1])
