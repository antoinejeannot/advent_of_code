import sys
import typing


def read_assignments(
    input_path: str,
) -> typing.Generator[tuple[tuple[int, int]], None, None]:
    with open(input_path) as f:
        for line in f:
            yield (
                [int(section) for section in sections.split("-")]
                for sections in line.strip().split(",")
            )


def is_entire_overlap(
    assignement_1: tuple[int, int], assignement_2: tuple[int, int]
) -> bool:
    start_section_1, end_section_1 = assignement_1
    start_section_2, end_section_2 = assignement_2
    return (
        (end_section_2 >= end_section_1) and (start_section_2 <= start_section_1)
    ) or ((end_section_1 >= end_section_2) and (start_section_1 <= start_section_2))


def main(input_path: str):
    overlapping_assignments = sum(
        is_entire_overlap(*assignements_pair)
        for assignements_pair in read_assignments(input_path)
    )
    print(overlapping_assignments)


if __name__ == "__main__":
    main(sys.argv[1])
