import sys
from collections import deque

from part_one import build_stacks, read, read_moves


def apply_move(quantity: int, source: int, target: int, stacks: list[deque]) -> None:
    buffer = deque([])
    for _ in range(quantity):
        buffer.append(stacks[source - 1].pop())
    for _ in range(quantity):
        stacks[target - 1].append(buffer.pop())


def main(file_path: str):
    reader = read(file_path)
    stacks = build_stacks(reader)
    for move in read_moves(reader):
        apply_move(*move, stacks)
    print("".join(stack[-1] for stack in stacks))


if __name__ == "__main__":
    main(sys.argv[1])
