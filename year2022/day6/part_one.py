import collections
import itertools
import sys
import typing


def read(file_path: str) -> typing.Generator[str, None, None]:
    with open(file_path) as f:
        yield from f.readline()


def sliding_window(
    characters: typing.Generator[str, None, None], chunk_size: int
) -> typing.Generator[tuple[str, str, str, str], None, None]:
    it = iter(characters)
    window = collections.deque(itertools.islice(it, chunk_size), maxlen=chunk_size)
    if len(window) == chunk_size:
        yield tuple(window)
    for x in it:
        window.append(x)
        yield tuple(window)


def find_marker(
    characters_gen: typing.Generator[tuple[str, str, str, str], None, None],
    chunk_size: int,
) -> int | None:
    for i, characters in enumerate(characters_gen):
        if len(set(characters)) == len(characters):
            return i + chunk_size
    raise ValueError


def main(file_path: str, chunk_size: int):
    try:
        marker = find_marker(sliding_window(read(file_path), chunk_size), chunk_size)
        print(marker)
    except (ValueError, StopIteration) as e:
        raise ValueError("Could not find any start-of-packet marker") from e


if __name__ == "__main__":
    main(sys.argv[1], 4)
