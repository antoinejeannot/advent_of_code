import sys
import typing


def read_rucksacks(input_path: str) -> typing.Generator[str, None, None]:
    with open(input_path) as f:
        for line in f:
            yield line.strip()


def get_shared_item(rucksack: str) -> str:
    half = len(rucksack) // 2
    return (set(rucksack[:half]) & set(rucksack[half:])).pop()


def get_priority(item: str) -> int:
    if item.islower():
        return ord(item) - ord("a") + 1
    else:
        return ord(item) - ord("A") + 27


def main(input_path: str):
    total_priorities = sum(
        get_priority(get_shared_item(rucksack))
        for rucksack in read_rucksacks(input_path)
    )
    print(total_priorities)


if __name__ == "__main__":
    main(sys.argv[1])
