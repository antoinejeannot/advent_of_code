import heapq
import sys
import typing


def calories_reader(file_path: str) -> typing.Generator[int, None, None]:
    with open(file_path) as f:
        elf_calories = 0
        for line in f:
            if line := line.strip():
                elf_calories += int(line)
            else:
                yield elf_calories
                elf_calories = 0


def main(file_path: str):
    top_n = heapq.nlargest(3, calories_reader(file_path))
    print(sum(top_n))


if __name__ == "__main__":
    main(sys.argv[1])
