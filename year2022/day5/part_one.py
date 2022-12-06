import itertools
import re
import sys
import typing
from collections import deque

MOVE_PATTERN = re.compile(r"move (\d+) from (\d+) to (\d+)")


def read(file_path: str) -> typing.Generator[str, None, None]:
    with open(file_path) as f:
        for line in f:
            yield line


def build_stacks(lines: typing.Generator[str, None, None]) -> list[deque[str]]:
    # one stack is represented by 3 caracters + 1 space (except the last one).
    # hence the stacks number is: (length of line + 1) / 4
    try:
        first_line = next(lines)
        n_stacks = int((len(first_line.strip()) + 1) / 4)
    except StopIteration:
        raise EOFError("Empty file")

    stacks = [deque() for _ in range(n_stacks)]
    for line in itertools.chain([first_line], lines):
        if line.startswith(" 1 "):
            break
        for n_stack in range(len(stacks)):
            item = line[4 * n_stack + 1]
            if ord("A") <= ord(item) <= ord("Z"):
                stacks[n_stack].appendleft(item)
    return stacks


def read_moves(
    lines: typing.Generator[str, None, None]
) -> typing.Generator[tuple[int, int, int], None, None]:
    for line in lines:
        if res := MOVE_PATTERN.search(line):
            quantity, source, target = res.groups()
            yield int(quantity), int(source), int(target)


def apply_move(quantity: int, source: int, target: int, stacks: list[deque]) -> None:
    for _ in range(quantity):
        item = stacks[source - 1].pop()
        stacks[target - 1].append(item)


def main(file_path: str):
    reader = read(file_path)
    stacks = build_stacks(reader)
    for move in read_moves(reader):
        apply_move(*move, stacks)
    print("".join(stack[-1] for stack in stacks))


if __name__ == "__main__":
    main(sys.argv[1])
